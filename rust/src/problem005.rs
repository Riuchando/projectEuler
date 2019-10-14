use std::collections::HashMap;

fn prime_factor_counts(value: u64) -> HashMap<u64, u32> {
    let mut factors: HashMap<u64, u32> = HashMap::new();
    let mut value = value;
    let mut calc = 2;
    while value > 1 {
        while value % calc == 0 {
            factors.insert(calc, match factors.get(&calc) {Some(count) => count+ 1, None => 1} );
            value = value / calc;
        }
        calc = calc + 1;
    }
    if factors.len() == 0 {
        factors.insert(value, 1);
    } 
    factors
}

pub fn run() -> u64 {
    // for this we try to determine this by prime factors
    // for 1 to 10, we need at most 3 2s (8)
    // 2 3s (9)
    // then one of each other prime factor


    // for 1 to 20
    // 20: 2 2 5
    // 19: 
    // 18: 2 2 3 3
    // ... 
    let mut global_counts: HashMap<u64, u32> = HashMap::new();
    for value in 1..20 {
        let counts = prime_factor_counts(value);
        for (key,value) in &counts {
            match global_counts.get(key) {
                Some(global_value) => if global_value < value {
                    global_counts.insert(*key, *value);
                }
                None => {
                    global_counts.insert(*key, *value);
                }
            }
        }
    }
    // println!("{:?}", global_counts);

    global_counts.iter().fold(1 , |acc, (key, value)| acc * (*key as u64).pow(*value))
    
}