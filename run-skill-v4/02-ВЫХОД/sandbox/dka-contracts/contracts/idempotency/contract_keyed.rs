// Контрактный тест ДКА §4.1 «Идемпотентность авторизации» — вариант для API с ключом.
// Проверяет поведение: повторный вызов с тем же ключом возвращает исход первого и не
// выполняет новое списание; разные ключи — разные операции. Принадлежит ДКА.
use payments_core::{Currency, Payment, PaymentEvent, PaymentProcessor};

#[test]
fn same_key_returns_first_outcome() {
    let mut processor = PaymentProcessor::new();

    let first = processor
        .authorize(Payment::new(1_000, Currency::Rub).unwrap(), "dka-key-1")
        .expect("первый вызов authorize завершился ошибкой");

    let second = processor
        .authorize(Payment::new(2_000, Currency::Usd).unwrap(), "dka-key-1")
        .expect("повторный вызов authorize завершился ошибкой");

    assert_eq!(first, second, "повторный вызов с тем же ключом выполнил новое списание");
    let authorizations = second
        .events()
        .iter()
        .filter(|e| matches!(e, PaymentEvent::Authorized { .. }))
        .count();
    assert_eq!(authorizations, 1, "авторизация записана в журнал дважды");
}

#[test]
fn different_keys_are_different_operations() {
    let mut processor = PaymentProcessor::new();

    let a = processor
        .authorize(Payment::new(1_000, Currency::Rub).unwrap(), "dka-key-a")
        .expect("вызов authorize завершился ошибкой");
    let b = processor
        .authorize(Payment::new(1_000, Currency::Rub).unwrap(), "dka-key-b")
        .expect("вызов authorize завершился ошибкой");

    assert_ne!(a.events(), b.events(), "разные ключи дали один и тот же исход — операции склеены");
}
