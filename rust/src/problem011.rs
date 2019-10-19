use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::io::Error;
use std::io::ErrorKind;
use std::vec::Vec;

pub fn run() -> Result<u64, Error> {
    let f = File::open("resources/problem011.txt")?;
    let f = BufReader::new(f);
    let mut matrix: Vec<Vec<u64>> = Vec::new();
    for line in f.lines() {
        // do some parsing
        let line_split = line?
            .parse::<String>()
            .map_err(|_err| Error::new(ErrorKind::InvalidData, format!("couldn't parse")))
            .unwrap();
        let mut digits: Vec<u64> = Vec::new();
        for character in line_split.split(" ") {
            let number = character
                .parse::<u64>()
                .map_err(|_err| Error::new(ErrorKind::InvalidData, format!("couldn't parse")))?;
            digits.push(number);
        }
        matrix.push(digits);
    }
    // println!("{:?}", matrix);
    // let's brute force search through all the items in the grid
    let mut max_value = 0;

    for (row_index, row) in matrix.iter().enumerate() {
        for (column_index, _column) in row.iter().enumerate() {
            if column_index + 3 < matrix.len() {
                let horizontal_slice = matrix[row_index][column_index..column_index + 4]
                    .iter()
                    .fold(1, |acc, curr| acc * curr);
                if horizontal_slice > max_value {
                    max_value = horizontal_slice;
                    println!(
                        "horizontal {} {:?}",
                        max_value,
                        matrix[row_index][column_index..column_index + 4].to_vec()
                    );
                }
            }
            if row_index + 3 < matrix.len() {
                let vertical_slice = matrix[row_index][column_index]
                    * matrix[row_index + 1][column_index]
                    * matrix[row_index + 2][column_index]
                    * matrix[row_index + 3][column_index];
                if vertical_slice > max_value {
                    max_value = vertical_slice;
                    // println!(
                    //     "vertical {} {:?}",
                    //     max_value,
                    //     vec!(
                    //         matrix[row_index][column_index],
                    //         matrix[row_index + 1][column_index],
                    //         matrix[row_index + 2][column_index],
                    //         matrix[row_index + 3][column_index]
                    //     )
                    // );
                }
            }
            if row_index + 3 < matrix.len() && column_index + 3 < matrix.len() {
                let diagonal_slice = matrix[row_index][column_index]
                    * matrix[row_index + 1][column_index + 1]
                    * matrix[row_index + 2][column_index + 2]
                    * matrix[row_index + 3][column_index + 3];
                if diagonal_slice > max_value {
                    max_value = diagonal_slice;
                    // println!(
                    //     "diagonal left {} {:?}",
                    //     max_value,
                    //     vec!(
                    //         matrix[row_index][column_index],
                    //         matrix[row_index + 1][column_index + 1],
                    //         matrix[row_index + 2][column_index + 1],
                    //         matrix[row_index + 3][column_index + 1]
                    //     )
                    // );
                }
            }
            if row_index > 3 && column_index + 3 < matrix.len() {
                let diagonal_slice = matrix[row_index][column_index]
                    * matrix[row_index - 1][column_index + 1]
                    * matrix[row_index - 2][column_index + 2]
                    * matrix[row_index - 3][column_index + 3];
                if diagonal_slice > max_value {
                    max_value = diagonal_slice;
                    // println!(
                    //     "diagonal right {} {:?}",
                    //     max_value,
                    //     vec!(
                    //         matrix[row_index][column_index],
                    //         matrix[row_index - 1][column_index - 1],
                    //         matrix[row_index - 2][column_index - 2],
                    //         matrix[row_index - 3][column_index - 3]
                    //     )
                    // );
                }
            }
        }
    }
    Ok(max_value)
}
