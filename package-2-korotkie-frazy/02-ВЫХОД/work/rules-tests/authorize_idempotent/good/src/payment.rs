//! Соблюдение §4.1: authorize идемпотентен по ключу.

use std::collections::HashMap;

#[derive(Default)]
pub struct PaymentProcessor {
    inbox: HashMap<String, bool>,
}

impl PaymentProcessor {
    pub fn authorize(&mut self, idempotency_key: &str) -> bool {
        if let Some(result) = self.inbox.get(idempotency_key) {
            return *result;
        }
        self.inbox.insert(idempotency_key.to_owned(), true);
        true
    }
}
