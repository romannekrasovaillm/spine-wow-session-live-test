//! Пример selftest (bypass): формальный обход — в API есть ключ идемпотентности и класс
//! `IdempotencyInbox`, слово `idempotency` видно правилу must_contain, но inbox не читается:
//! поведения нет. Контрактный тест такой обход ловит.
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

/// Объявлен для красоты: не читается и не пишется.
#[derive(Debug, Default)]
pub struct IdempotencyInbox;

#[derive(Debug, Default)]
pub struct PaymentProcessor {
    seen_keys: HashMap<String, usize>,
    inbox: IdempotencyInbox,
}

impl PaymentProcessor {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn authorize(&mut self, payment: Payment, idempotency_key: &str) -> Result<Payment, PayError> {
        let done = payment.authorize(idempotency_key)?;
        *self.seen_keys.entry(idempotency_key.to_string()).or_insert(0) += 1;
        Ok(done)
    }
}
