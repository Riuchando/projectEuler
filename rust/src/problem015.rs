fn choose(n: u64, k: u64) -> u64 {
    if k > n {
        return 0;
    }
    let mut k = k;
    if k * 2 > n {
        k = n - k;
    }

    if k == 0 {
        return 1;
    }

    let mut result = n;
    for i in 2..k + 1 {
        result = result * (n - i + 1) / i;
    }
    result
}

// fn catalan(n :u64) -> u64 {
//     choose(n * 2, n) / (n+1)
// }

pub fn run() -> u64 {
    // println!(
    //     "{:?}",
    //     (1..20)
    //         .map(|n| choose(n * 2, n))
    //         .collect::<Vec<u64>>()
    // );
    choose(20 * 2, 20)
}
