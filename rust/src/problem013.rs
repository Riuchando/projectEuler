use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::io::Error;
use std::io::ErrorKind;

use num_bigint::BigInt;

pub fn run() -> Result<String, Error> {
    let f = File::open("resources/problem013.txt")?;
    let f = BufReader::new(f);
    // let mut digits: Vec<u64> = Vec::new();
    let mut sum = BigInt::new(num_bigint::Sign::Plus, vec![0]);
    for line in f.lines() {
        // do some parsing
        let big_int = line?
            .parse::<BigInt>()
            .map_err(|_err| Error::new(ErrorKind::InvalidData, format!("couldn't parse")))
            .unwrap();
        sum = sum + big_int;
    }
    Ok(format!("{}", &sum.to_str_radix(10).to_string()[0..10]))
}
