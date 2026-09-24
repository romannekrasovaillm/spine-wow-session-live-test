//! Нарушение §3.2: anyhow для доменных ошибок.

use anyhow::Result;

pub fn settle(amount: i64) -> Result<()> {
    if amount <= 0 {
        anyhow::bail!("amount must be positive");
    }
    Ok(())
}
