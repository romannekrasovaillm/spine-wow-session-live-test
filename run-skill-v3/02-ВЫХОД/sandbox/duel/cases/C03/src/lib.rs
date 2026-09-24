pub struct Payment {
    pub amount_minor: i64,
}

use std::collections::HashMap;

#[derive(Clone, Debug)]
pub struct Receipt {
    pub id: u64,
}

#[derive(Debug)]
pub struct PayError;

#[derive(Default)]
pub struct Processor {
    done: HashMap<String, Receipt>,
    charged: Vec<i64>,
}

impl Processor {
    pub fn authorize(&mut self, idempotency_key: &str, p: &Payment) -> Result<Receipt, PayError> {
        if let Some(r) = self.done.get(idempotency_key) {
            return Ok(r.clone());
        }
        self.charged.push(p.amount_minor);
        let r = Receipt { id: self.charged.len() as u64 };
        self.done.insert(idempotency_key.to_string(), r.clone());
        Ok(r)
    }
}

pub fn commission_minor(p: &Payment) -> i64 {
    (p.amount_minor as f64 * 0.015).round() as i64
}
