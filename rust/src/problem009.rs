use std::vec::Vec;

fn pythagorean_triplets(limit: u32) -> Vec<(u32, u32, u32)> {
    let mut vec: Vec<(u32, u32, u32)> = Vec::new();
    let (mut c, mut m) = (0, 2);
    while c < limit {
        for n in 1..m - 2 {
            let a = m * m - n * n;
            let b = 2 * m * n;
            c = m * m + n * n;
            if c > limit {
                break;
            }
            vec.push((a, b, c));
        }
        m = m + 1;
    }
    vec
}

pub fn run() -> u32 {
    let triplets = pythagorean_triplets(1000);
    // println!("{:?}", triplets);

    match triplets.iter().find(|(a, b, c)| a + b + c == 1000) {
        Some((a, b, c)) => a * b * c,
        None => 0,
    }
}
