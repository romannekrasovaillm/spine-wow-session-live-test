pub struct Payment {
    pub amount_minor: i64,
}

pub fn authorize(payment_id: &str, p: &Payment) -> Result<(), String> {
    let _ = (payment_id, p);
    Ok(())
}
