// То же нарушение (ручное описание ошибки), но тип не оканчивается на `Error`,
// поэтому шаблон правила, привязанный к имени типа, его не видит.
use std::fmt;

#[derive(Debug)]
pub enum PaymentFailure {
    InvalidTransition,
}

impl fmt::Display for PaymentFailure {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "invalid transition")
    }
}

impl std::error::Error for PaymentFailure {}
