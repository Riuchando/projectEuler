use itertools::Itertools;
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
    for i in 1..100000 {
        let triangle_number = i * (i + 1) / 2;
        let divisor_count = prime_factors(triangle_number)  // get the prime factors
            .iter()
            .group_by(|a| &**a)
            .into_iter()
            .fold(1, |acc, (_k, v)| acc * (v.count() + 1)); // the number of divisors are the number of prime factors' exponent 
        // println!("{} {}", triangle_number, divisor_count);
        if divisor_count > 500 {
            return triangle_number;
        }
    }
    0
}
