#[derive(Debug, thiserror::Error)]
pub enum PaymentError {
    #[error("invalid transition")]
    InvalidTransition,
}

pub fn load() -> Result<(), PaymentError> {
    Ok(())
}
