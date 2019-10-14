// fn fib(term: u32) -> u32 {
//     let mut first = 1;
//     let mut second = 1;
//     let mut current = first + second;
//     for i in 0..term {
//         first = second;
//         second = current;
//         current = first + second;
//     }
//     current
// }

pub fn run() -> u32 {
    let mut first = 1;
    let mut second = 1;
    let mut current = first + second;
    let mut sum = current;
    while current < 4_000_000 {
        first = second;
        second = current;
        current = first + second;
        if current % 2 == 0 && current < 4_000_000 {
            sum += current;
        }
    }
    sum
}
