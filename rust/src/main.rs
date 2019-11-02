extern crate num_bigint;

use std::env;
use std::io::Error;

mod problem001;
mod problem002;
mod problem003;
mod problem004;
mod problem005;
mod problem006;
mod problem007;
mod problem008;
mod problem009;
mod problem010;
mod problem011;
mod problem012;
mod problem013;
mod problem015;
mod problem026;
mod problem069;

fn main() -> Result<(), Error> {
    let args: Vec<String> = env::args().collect();
    match args[1].as_ref() {
        "problem1" => {
            println!("{}", problem001::run());
        }
        "problem2" => {
            println!("{}", problem002::run());
        }
        "problem3" => {
            println!("{}", problem003::run());
        }
        "problem4" => {
            println!("{}", problem004::run());
        }
        "problem5" => {
            println!("{}", problem005::run());
        }
        "problem6" => {
            println!("{}", problem006::run());
        }
        "problem7" => {
            println!("{}", problem007::run());
        }
        "problem8" => {
            println!("{}", problem008::run()?);
        }
        "problem9" => {
            println!("{}", problem009::run());
        }
        "problem10" => {
            println!("{}", problem010::run());
        }
        "problem11" => {
            println!("{}", problem011::run()?);
        }
        "problem12" => {
            println!("{}", problem012::run());
        }
        "problem13" => {
            println!("{}", problem013::run()?);
        }
        "problem15" => {
            println!("{}", problem015::run());
        }
        // "problem26" => {
        //     println!("{}", problem026::run());
        // }
        "problem69" => {
            println!("{}", problem069::run());
        }
        _ => println!("{}", "invalid argument"),
    }
    Ok(())
}
