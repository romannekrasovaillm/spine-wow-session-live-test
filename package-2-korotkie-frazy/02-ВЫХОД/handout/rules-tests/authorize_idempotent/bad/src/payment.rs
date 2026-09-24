//! Нарушение §4.1: authorize не принимает ключ идемпотентности.

pub struct Payment {
    authorized: bool,
}

impl Payment {
    pub fn authorize(&mut self) {
        self.authorized = true;
    }
}
