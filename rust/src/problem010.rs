fn generate_primes(prime_max: u64) -> Vec<u64> {
    let mut prime_list: Vec<u64> = Vec::new();
    let mut count: u64 = 2;
    while prime_max > count {
        if is_prime(count, &prime_list) {
            prime_list.push(count);
        }
        if count != 2 {
            count += 2
        } else {
            count += 1
        }
    }
    prime_list
}

fn is_prime(number: u64, prime_list: &Vec<u64>) -> bool {
    let sqrt = (number as f64).sqrt().ceil() as u64;
    for prime in prime_list {
        if number % prime == 0 {
            return false;
        }
        if sqrt < *prime {
            break;
        }
    }
    true
}

pub fn run() -> u64 {
    // println!("{:?}", generate_primes(100));

    generate_primes(2_000_000)
        .iter()
        .fold(0, |acc, curr| acc + curr)
}
