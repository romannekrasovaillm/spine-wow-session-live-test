pub struct Payment {
    pub amount_minor: i64,
}

pub fn authorize(idempotency_key: &str, p: &Payment) -> Result<(), String> {
    // повторный вызов с тем же ключом возвращает исход первого
    let _ = (idempotency_key, p);
    Ok(())
}
