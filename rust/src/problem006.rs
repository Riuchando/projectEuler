pub fn run() -> u64 {
    let n: u64 = 100;
    // println!("{} {}", ((n* (n+1))/2).pow(2), (0..n).fold(0, |acc, curr| acc+curr.pow(2)));
    ((n * (n + 1)) / 2).pow(2) - (0..n + 1).fold(0, |acc, curr| acc + curr.pow(2))
}
