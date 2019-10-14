fn reverse_number(number: u32) -> u32 {
    let mut reverse = 0;
    let mut number = number;
    while number != 0 {
        let pop = number % 10;
        number = number / 10;
        if reverse > std::u32::MAX / 10 || (reverse == std::u32::MAX / 10 && pop > 7) {
            return 0;
        }
        // if reverse < std::u32::MAX/10 || (reverse == std::u32::MAX / 10 && pop < -8) {
        //     return 0;
        // }
        reverse = reverse * 10 + pop;
    }
    reverse
}

pub fn run() -> u32 {
    let n: u32 = 3;
    let mut biggest = 0;
    for _z in 2..std::u32::MAX {
        if _z > (10 as u32).pow(n) {
            break;
        }

        let left: u32 = (10 as u32).pow(n) - _z;
        let right: u32 = reverse_number(left);
        if _z.pow(2) <= 4 * right || right == 0 {
            continue;
        }
        let root_1 = 0.5 * ((_z as f64) + ((_z.pow(2) - 4 * right) as f64).sqrt());
        let root_2 = 0.5 * ((_z as f64) - ((_z.pow(2) - 4 * right) as f64).sqrt());
        if root_1.floor() == root_1 || root_2.floor() == root_2 {
            biggest = (10 as u32).pow(n) * left + right;
        }
    }
    biggest
}
