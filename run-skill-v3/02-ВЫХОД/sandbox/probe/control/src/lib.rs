// контроль: тип написан отдельным токеном — правило обязано сработать
pub fn scaled(minor: u64) -> u64 {
    let factor: f64 = 1.5;
    (minor as u64) + (factor as u64)
}
