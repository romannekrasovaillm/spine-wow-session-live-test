//! Нарушение §2.1 (ред. 2026.2): арифметика с плавающей точкой для денег.

pub fn discounted(total_minor: i64) -> i64 {
    let rate = 0.985;
    total_minor / 100 * (rate * 100.0) as i64
}
