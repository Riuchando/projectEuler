use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::io::Error;
use std::io::ErrorKind;
use std::vec::Vec;
use std::collections::VecDeque;

pub fn run() -> Result<u64, Error> {
    // let data = fs::read_to_string("resources/problem008.txt").expect("Unable to read file");
    // println!("{}", data);

    let f = File::open("resources/problem008.txt")?;
    let f = BufReader::new(f);
    let mut digits: Vec<u64> = Vec::new();
    for line in f.lines() {
        // do some parsing
        let line_split = line?
            .parse::<String>()
            .map_err(|_err| Error::new(ErrorKind::InvalidData, format!("couldn't parse")))
            .unwrap();
        for character in line_split.chars() {
            match character.to_digit(10) {
                Some(digit) => digits.push(digit as u64),
                None => {
                    return Err(Error::new(
                        ErrorKind::InvalidData,
                        format!("couldn't parse {}", character),
                    ))
                }
            }
        }
    }
    println!("{:?}", digits);
    let max_buf_size  = 13;
    let mut buf = VecDeque::new();
    let mut max_running_multiplier = 0;
    for digit in digits {
        if buf.len() >=  max_buf_size {
            buf.pop_front();
        }
        buf.push_back(digit);
        // println!("{:?}",buf);
        let running_multiplier = buf.iter().fold(1, |acc, curr| acc*curr);
        if running_multiplier > max_running_multiplier {
            max_running_multiplier = running_multiplier;
        }
    }
    Ok(max_running_multiplier)
}
