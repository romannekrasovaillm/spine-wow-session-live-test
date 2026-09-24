use thiserror::Error;

#[derive(Debug, Error)]
pub enum PaymentError {
    #[error("amount must be greater than zero")]
    ZeroAmount,
}

pub fn settle(amount: u64) -> Result<(), PaymentError> {
    if amount == 0 {
        return Err(PaymentError::ZeroAmount);
    }
    Ok(())
}
