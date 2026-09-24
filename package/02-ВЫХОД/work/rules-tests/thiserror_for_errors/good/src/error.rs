use thiserror::Error;

#[derive(Debug, Error)]
pub enum PaymentError {
    #[error("invalid transition")]
    InvalidTransition,
}
