// должен ловиться: суффиксный литерал
pub fn scaled(minor: u64) -> u64 {
    let factor = 1.5f64;
    minor + (factor as u64)
}
