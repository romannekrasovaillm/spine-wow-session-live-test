// не должен ловиться: типизированные ошибки без anyhow
use thiserror::Error;

#[derive(Debug, Error)]
pub enum PaymentError {
    #[error("amount must be greater than zero")]
    ZeroAmount,
}
