// обход: тот же float, но записан суффиксом литерала
pub fn scaled(minor: u64) -> u64 {
    let factor = 1.5f64;
    minor + (factor as u64)
}
