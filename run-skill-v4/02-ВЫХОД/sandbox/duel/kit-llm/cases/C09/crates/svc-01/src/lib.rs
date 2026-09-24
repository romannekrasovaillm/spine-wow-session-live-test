#[derive(Default)]
pub struct Payment {
    pub amount_minor: i64,
}

use std::collections::HashMap;

#[derive(Clone, Debug)]
pub struct Receipt {
    pub id: u64,
}

#[derive(Debug)]
pub struct PayError;

#[derive(Default)]
pub struct Processor {
    done: HashMap<String, Receipt>,
    charged: Vec<i64>,
}

impl Processor {
    pub fn authorize(&mut self, idempotency_key: &str, p: &Payment) -> Result<Receipt, PayError> {
        if let Some(r) = self.done.get(idempotency_key) {
            return Ok(r.clone());
        }
        self.charged.push(p.amount_minor);
        let r = Receipt { id: self.charged.len() as u64 };
        self.done.insert(idempotency_key.to_string(), r.clone());
        Ok(r)
    }
}
pub fn op_1_1(x: i64) -> i64 { x * 1 + 1 }
pub fn op_1_2(x: i64) -> i64 { x * 2 + 1 }
pub fn op_1_3(x: i64) -> i64 { x * 3 + 1 }
pub fn op_1_4(x: i64) -> i64 { x * 4 + 1 }
pub fn op_1_5(x: i64) -> i64 { x * 5 + 1 }
pub fn op_1_6(x: i64) -> i64 { x * 6 + 1 }
pub fn op_1_7(x: i64) -> i64 { x * 7 + 1 }
pub fn op_1_8(x: i64) -> i64 { x * 8 + 1 }
pub fn op_1_9(x: i64) -> i64 { x * 9 + 1 }
pub fn op_1_10(x: i64) -> i64 { x * 10 + 1 }
pub fn op_1_11(x: i64) -> i64 { x * 11 + 1 }
pub fn op_1_12(x: i64) -> i64 { x * 12 + 1 }
pub fn op_1_13(x: i64) -> i64 { x * 13 + 1 }
pub fn op_1_14(x: i64) -> i64 { x * 14 + 1 }
pub fn op_1_15(x: i64) -> i64 { x * 15 + 1 }
pub fn op_1_16(x: i64) -> i64 { x * 16 + 1 }
pub fn op_1_17(x: i64) -> i64 { x * 17 + 1 }
pub fn op_1_18(x: i64) -> i64 { x * 18 + 1 }
pub fn op_1_19(x: i64) -> i64 { x * 19 + 1 }
pub fn op_1_20(x: i64) -> i64 { x * 20 + 1 }
pub fn op_1_21(x: i64) -> i64 { x * 21 + 1 }
pub fn op_1_22(x: i64) -> i64 { x * 22 + 1 }
pub fn op_1_23(x: i64) -> i64 { x * 23 + 1 }
pub fn op_1_24(x: i64) -> i64 { x * 24 + 1 }
pub fn op_1_25(x: i64) -> i64 { x * 25 + 1 }
pub fn op_1_26(x: i64) -> i64 { x * 26 + 1 }
pub fn op_1_27(x: i64) -> i64 { x * 27 + 1 }
pub fn op_1_28(x: i64) -> i64 { x * 28 + 1 }
pub fn op_1_29(x: i64) -> i64 { x * 29 + 1 }
pub fn op_1_30(x: i64) -> i64 { x * 30 + 1 }
pub fn op_1_31(x: i64) -> i64 { x * 31 + 1 }
pub fn op_1_32(x: i64) -> i64 { x * 32 + 1 }
pub fn op_1_33(x: i64) -> i64 { x * 33 + 1 }
pub fn op_1_34(x: i64) -> i64 { x * 34 + 1 }
pub fn op_1_35(x: i64) -> i64 { x * 35 + 1 }
pub fn op_1_36(x: i64) -> i64 { x * 36 + 1 }
pub fn op_1_37(x: i64) -> i64 { x * 37 + 1 }
pub fn op_1_38(x: i64) -> i64 { x * 38 + 1 }
pub fn op_1_39(x: i64) -> i64 { x * 39 + 1 }
pub fn op_1_40(x: i64) -> i64 { x * 40 + 1 }
pub fn op_1_41(x: i64) -> i64 { x * 41 + 1 }
pub fn op_1_42(x: i64) -> i64 { x * 42 + 1 }
pub fn op_1_43(x: i64) -> i64 { x * 43 + 1 }
pub fn op_1_44(x: i64) -> i64 { x * 44 + 1 }
pub fn op_1_45(x: i64) -> i64 { x * 45 + 1 }
pub fn op_1_46(x: i64) -> i64 { x * 46 + 1 }
pub fn op_1_47(x: i64) -> i64 { x * 47 + 1 }
pub fn op_1_48(x: i64) -> i64 { x * 48 + 1 }
pub fn op_1_49(x: i64) -> i64 { x * 49 + 1 }
pub fn op_1_50(x: i64) -> i64 { x * 50 + 1 }
pub fn op_1_51(x: i64) -> i64 { x * 51 + 1 }
pub fn op_1_52(x: i64) -> i64 { x * 52 + 1 }
pub fn op_1_53(x: i64) -> i64 { x * 53 + 1 }
pub fn op_1_54(x: i64) -> i64 { x * 54 + 1 }
pub fn op_1_55(x: i64) -> i64 { x * 55 + 1 }
pub fn op_1_56(x: i64) -> i64 { x * 56 + 1 }
pub fn op_1_57(x: i64) -> i64 { x * 57 + 1 }
pub fn op_1_58(x: i64) -> i64 { x * 58 + 1 }
pub fn op_1_59(x: i64) -> i64 { x * 59 + 1 }
pub fn op_1_60(x: i64) -> i64 { x * 60 + 1 }
pub fn op_1_61(x: i64) -> i64 { x * 61 + 1 }
pub fn op_1_62(x: i64) -> i64 { x * 62 + 1 }
pub fn op_1_63(x: i64) -> i64 { x * 63 + 1 }
pub fn op_1_64(x: i64) -> i64 { x * 64 + 1 }
pub fn op_1_65(x: i64) -> i64 { x * 65 + 1 }
pub fn op_1_66(x: i64) -> i64 { x * 66 + 1 }
pub fn op_1_67(x: i64) -> i64 { x * 67 + 1 }
pub fn op_1_68(x: i64) -> i64 { x * 68 + 1 }
pub fn op_1_69(x: i64) -> i64 { x * 69 + 1 }
pub fn op_1_70(x: i64) -> i64 { x * 70 + 1 }
pub fn op_1_71(x: i64) -> i64 { x * 71 + 1 }
pub fn op_1_72(x: i64) -> i64 { x * 72 + 1 }
pub fn op_1_73(x: i64) -> i64 { x * 73 + 1 }
pub fn op_1_74(x: i64) -> i64 { x * 74 + 1 }
pub fn op_1_75(x: i64) -> i64 { x * 75 + 1 }
pub fn op_1_76(x: i64) -> i64 { x * 76 + 1 }
pub fn op_1_77(x: i64) -> i64 { x * 77 + 1 }
pub fn op_1_78(x: i64) -> i64 { x * 78 + 1 }
pub fn op_1_79(x: i64) -> i64 { x * 79 + 1 }
pub fn op_1_80(x: i64) -> i64 { x * 80 + 1 }
pub fn op_1_81(x: i64) -> i64 { x * 81 + 1 }
pub fn op_1_82(x: i64) -> i64 { x * 82 + 1 }
pub fn op_1_83(x: i64) -> i64 { x * 83 + 1 }
pub fn op_1_84(x: i64) -> i64 { x * 84 + 1 }
pub fn op_1_85(x: i64) -> i64 { x * 85 + 1 }
pub fn op_1_86(x: i64) -> i64 { x * 86 + 1 }
pub fn op_1_87(x: i64) -> i64 { x * 87 + 1 }
pub fn op_1_88(x: i64) -> i64 { x * 88 + 1 }
pub fn op_1_89(x: i64) -> i64 { x * 89 + 1 }
pub fn op_1_90(x: i64) -> i64 { x * 90 + 1 }
pub fn op_1_91(x: i64) -> i64 { x * 91 + 1 }
pub fn op_1_92(x: i64) -> i64 { x * 92 + 1 }
pub fn op_1_93(x: i64) -> i64 { x * 93 + 1 }
pub fn op_1_94(x: i64) -> i64 { x * 94 + 1 }
pub fn op_1_95(x: i64) -> i64 { x * 95 + 1 }
pub fn op_1_96(x: i64) -> i64 { x * 96 + 1 }
pub fn op_1_97(x: i64) -> i64 { x * 97 + 1 }
pub fn op_1_98(x: i64) -> i64 { x * 98 + 1 }
pub fn op_1_99(x: i64) -> i64 { x * 99 + 1 }
pub fn op_1_100(x: i64) -> i64 { x * 100 + 1 }
pub fn op_1_101(x: i64) -> i64 { x * 101 + 1 }
pub fn op_1_102(x: i64) -> i64 { x * 102 + 1 }
pub fn op_1_103(x: i64) -> i64 { x * 103 + 1 }
pub fn op_1_104(x: i64) -> i64 { x * 104 + 1 }
pub fn op_1_105(x: i64) -> i64 { x * 105 + 1 }
pub fn op_1_106(x: i64) -> i64 { x * 106 + 1 }
pub fn op_1_107(x: i64) -> i64 { x * 107 + 1 }
pub fn op_1_108(x: i64) -> i64 { x * 108 + 1 }
pub fn op_1_109(x: i64) -> i64 { x * 109 + 1 }
pub fn op_1_110(x: i64) -> i64 { x * 110 + 1 }
pub fn op_1_111(x: i64) -> i64 { x * 111 + 1 }
pub fn op_1_112(x: i64) -> i64 { x * 112 + 1 }
pub fn op_1_113(x: i64) -> i64 { x * 113 + 1 }
pub fn op_1_114(x: i64) -> i64 { x * 114 + 1 }
pub fn op_1_115(x: i64) -> i64 { x * 115 + 1 }
pub fn op_1_116(x: i64) -> i64 { x * 116 + 1 }
pub fn op_1_117(x: i64) -> i64 { x * 117 + 1 }
pub fn op_1_118(x: i64) -> i64 { x * 118 + 1 }
pub fn op_1_119(x: i64) -> i64 { x * 119 + 1 }
