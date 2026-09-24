pub struct Payment {
    pub amount_minor: i64,
}

// idempotency: TODO — добавить ключ в следующем релизе
pub fn authorize(payment_id: &str, p: &Payment) -> Result<(), String> {
    let _ = (payment_id, p);
    Ok(())
}
