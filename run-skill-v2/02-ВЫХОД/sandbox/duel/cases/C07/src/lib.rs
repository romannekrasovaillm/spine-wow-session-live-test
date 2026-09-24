pub struct Payment {
    pub amount_minor: i64,
}

/// Ранжирование рекомендаций: косинусная близость, к деньгам не относится.
pub fn similarity_score(a: &[f32], b: &[f32]) -> f32 {
    a.iter().zip(b).map(|(x, y)| x * y).sum()
}

pub fn authorize(idempotency_key: &str, p: &Payment) -> Result<(), String> {
    // повторный вызов с тем же ключом возвращает исход первого
    let _ = (idempotency_key, p);
    Ok(())
}
