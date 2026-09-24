use std::fmt;

#[derive(Debug)]
pub enum PaymentError {
    InvalidTransition,
}

impl fmt::Display for PaymentError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "invalid transition")
    }
}

impl std::error::Error for PaymentError {}
