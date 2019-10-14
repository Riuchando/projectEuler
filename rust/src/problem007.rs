fn generate_primes(number_of_primes: u32) -> Vec<u64> {
    let mut prime_list: Vec<u64> = Vec::new();
    let mut count = 2;
    while prime_list.len() < number_of_primes as usize {
        if is_prime(count, &prime_list) {
            prime_list.push(count);
        }
        count += 1
    }
    prime_list
}

fn is_prime(number: u64, prime_list: &Vec<u64>) -> bool {
    for prime in prime_list {
        if number % prime == 0 {
            return false;
        }
    }
    true
}

pub fn run() -> u64 {
    let mut prime_list = generate_primes(10001);
    // print!("{:?}", prime_list);
    match prime_list.pop() {
        Some(x) => x,
        None => 1,
    }
}
