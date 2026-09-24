//! Пример selftest (good): идемпотентность реализована — inbox по ключу возвращает исход первого вызова.
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
    inbox: HashMap<String, Payment>,
}

impl PaymentProcessor {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn authorize(&mut self, payment: Payment, idempotency_key: &str) -> Result<Payment, PayError> {
        if let Some(first) = self.inbox.get(idempotency_key) {
            return Ok(first.clone());
        }
        let done = payment.authorize(idempotency_key)?;
        self.inbox.insert(idempotency_key.to_string(), done.clone());
        Ok(done)
    }
}
