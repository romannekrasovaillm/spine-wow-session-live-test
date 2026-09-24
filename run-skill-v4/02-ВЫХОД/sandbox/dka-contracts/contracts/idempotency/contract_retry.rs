// Контрактный тест ДКА §4.1 «Идемпотентность авторизации» — вариант для API без ключа.
// Если интерфейс не принимает ключ идемпотентности, требование проверяется на безопасность
// ретрая: повторная авторизация того же платежа не должна создавать второе списание и не
// должна отклоняться. Принадлежит ДКА.
use payment_core::{Currency, Payment, PaymentEventType};

#[test]
fn repeated_authorize_does_not_authorize_twice() {
    let mut payment = Payment::new("dka-pay-1", 1_000, Currency::USD).expect("платёж создан");

    payment.authorize().expect("первая авторизация завершилась ошибкой");

    let retry = payment.authorize();
    assert!(retry.is_ok(), "повторная авторизация отклонена — ретрай клиента не безопасен");

    let authorizations = payment
        .events()
        .iter()
        .filter(|e| e.event_type() == PaymentEventType::Authorized)
        .count();
    assert_eq!(authorizations, 1, "авторизация записана в журнал дважды");
}
