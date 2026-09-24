// Контрактный тест ДКА, стандарт платёжного ядра §4.1 «Идемпотентность авторизации».
// Проверяет поведение, а не текст: повторный вызов с тем же ключом возвращает исход первого
// вызова и не выполняет новое списание. Принадлежит ДКА; продукт его не видит и не меняет.
//
// Контракт API (часть стандарта): Processor: Default, Payment: Default,
// Processor::authorize(&mut self, key: &str, p: &Payment) -> Result<Receipt, E>, Receipt { pub id }.
use dka_contract_target::{Payment, Processor};

#[test]
fn same_key_returns_first_outcome() {
    let mut p = Processor::default();
    let pay = Payment::default();
    let first = p.authorize("dka-key-1", &pay).expect("первый вызов authorize завершился ошибкой");
    let second = p.authorize("dka-key-1", &pay).expect("повторный вызов authorize завершился ошибкой");
    assert_eq!(first.id, second.id, "повторный вызов с тем же ключом выполнил новое списание");
}

#[test]
fn different_keys_are_different_operations() {
    let mut p = Processor::default();
    let pay = Payment::default();
    let a = p.authorize("dka-key-a", &pay).expect("вызов authorize завершился ошибкой");
    let b = p.authorize("dka-key-b", &pay).expect("вызов authorize завершился ошибкой");
    assert_ne!(a.id, b.id, "разные ключи дали один и тот же исход — операции склеены");
}
