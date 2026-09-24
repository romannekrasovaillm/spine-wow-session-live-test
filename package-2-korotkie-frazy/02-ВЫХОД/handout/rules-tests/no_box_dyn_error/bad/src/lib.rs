//! Нарушение §3.2: тип ошибки стёрт через Box<dyn Error>.

pub fn load(path: &str) -> Result<String, Box<dyn std::error::Error>> {
    let body = std::fs::read_to_string(path)?;
    Ok(body)
}
