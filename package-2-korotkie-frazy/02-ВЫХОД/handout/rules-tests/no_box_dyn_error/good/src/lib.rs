//! Соблюдение §3.2: тип ошибки сохранён.

#[derive(Debug)]
pub enum PaymentError {
    Unreadable(String),
}

pub fn load(path: &str) -> Result<String, PaymentError> {
    std::fs::read_to_string(path).map_err(|e| PaymentError::Unreadable(e.to_string()))
}
