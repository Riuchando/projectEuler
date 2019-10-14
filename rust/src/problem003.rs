use std::vec::Vec;

fn prime_factors(value: u64) -> Vec<u64> {
    let mut factors = Vec::new();
    let mut value = value;
    let mut calc = 2;
    while value > 1 {
        while value % calc == 0 {
            factors.push(calc);
            value = value / calc;
        }
        calc = calc + 1;
    }
    factors
}

pub fn run() -> u64 {
    // println!("{:?}",prime_factors(600851475143));
    prime_factors(600851475143)
        .iter()
        .cloned()
        .fold(0, u64::max)
}
