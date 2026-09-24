//! Пример selftest (bad): ключ принимается, но дедупликации нет — каждый вызов авторизует заново.
use std::collections::HashMap;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Currency {
    Rub,
    Usd,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum PaymentEvent {
    Created,
    Authorized { idempotency_key: String },
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Payment {
    amount: i64,
    currency: Currency,
    events: Vec<PaymentEvent>,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct PayError;

impl Payment {
    pub fn new(amount: i64, currency: Currency) -> Result<Self, PayError> {
        if amount <= 0 {
            return Err(PayError);
        }
        Ok(Self { amount, currency, events: vec![PaymentEvent::Created] })
    }

    pub fn events(&self) -> &[PaymentEvent] {
        &self.events
    }

    fn authorize(mut self, idempotency_key: &str) -> Result<Self, PayError> {
        self.events.push(PaymentEvent::Authorized { idempotency_key: idempotency_key.to_string() });
        Ok(self)
    }
}

#[derive(Debug, Default)]
pub struct PaymentProcessor {
    seen: HashMap<String, usize>,
}

impl PaymentProcessor {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn authorize(&mut self, payment: Payment, idempotency_key: &str) -> Result<Payment, PayError> {
        let done = payment.authorize(idempotency_key)?;
        *self.seen.entry(idempotency_key.to_string()).or_insert(0) += 1;
        Ok(done)
    }
}
