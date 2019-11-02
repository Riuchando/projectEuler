fn A051626(n: u64) -> u32 {
    let mut lpow = 1;
    loop {
        for mpow in (0..lpow - 1).rev() {
            // println!("{} {} {}",lpow, mpow,n );
            let pow_diff = 10_f64.powi(lpow) - 10_f64.powi(mpow);
            if pow_diff - (pow_diff / n as f64).trunc() * (n as f64)   == 0_f64 {
                return (lpow - mpow) as u32;
            }
        }
        lpow += 1
    }
}

pub fn run() -> u32 {
    let y : Vec<(u32, u32)> = (2..100).map(|x| (x, A051626(x as u64))).collect();
    println!("{:?}", y);
    match (2..100).max_by_key(|x| A051626(*x as u64)) {
        Some(x) => x,
        None => 0,
    }
}
