//! Соблюдение §3.2: доменные ошибки — собственный тип.

#[derive(Debug, PartialEq, Eq)]
pub enum PaymentError {
    NonPositiveAmount,
}

pub fn settle(amount: i64) -> Result<(), PaymentError> {
    if amount <= 0 {
        return Err(PaymentError::NonPositiveAmount);
    }
    Ok(())
}
