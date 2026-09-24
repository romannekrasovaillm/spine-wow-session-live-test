//! Формальный обход: абсолютный путь к модулю — тип ошибки всё равно стёрт.
//! Паттерн по `std::error::Error` мог не поймать ведущее `::`.

pub fn load(path: &str) -> Result<String, Box<dyn ::std::error::Error>> {
    let body = std::fs::read_to_string(path)?;
    Ok(body)
}
