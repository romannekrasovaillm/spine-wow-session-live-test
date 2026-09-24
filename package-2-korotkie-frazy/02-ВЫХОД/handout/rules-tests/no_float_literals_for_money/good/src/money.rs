//! Соблюдение §2.1: только целые минорные единицы.

pub fn discounted(total_minor: i64) -> i64 {
    total_minor - total_minor * 15 / 1000
}
