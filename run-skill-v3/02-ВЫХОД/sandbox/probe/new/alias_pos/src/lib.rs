// должен ловиться: anyhow подключён под другим именем
use anyhow as a;

pub fn settle() -> a::Result<()> {
    Ok(())
}
