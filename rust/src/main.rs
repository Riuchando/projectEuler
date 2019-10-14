use std::env;
use std::io::Error;

mod problem001;
mod problem002;
mod problem003;
mod problem004;
mod problem005;

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
        _ => println!("{}", "invalid argument"),
    }
    Ok(())
}
