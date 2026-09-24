//! Формальный обход: ключа нет, но слово idempotency есть в комментарии.
//! Повторный вызов повторит операцию — требование §4.1 нарушено,
//! проверка «слово есть в src» может пройти.

// TODO(TASK-9): добавить idempotency key перед продуктива.

pub struct Payment {
    authorized: bool,
}

impl Payment {
    pub fn authorize(&mut self) {
        self.authorized = true;
    }
}
