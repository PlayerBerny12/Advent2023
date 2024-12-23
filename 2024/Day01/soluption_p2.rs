use std::collections::HashMap;
use std::io;

fn main() {
    let mut vec_l = vec![];
    let mut hash_r = HashMap::new();
    let lines = io::stdin().lines();

    for line in lines {
        let line = line.unwrap();
        let (l, r) = line.split_once("   ").unwrap();

        let l_num: i32 = l.parse().unwrap();
        let r_num: i32 = r.parse().unwrap();

        vec_l.push(l_num);
        hash_r.entry(r_num).and_modify(|val| *val += 1).or_insert(1);
    }

    let acc: i32 = vec_l
        .into_iter()
        .map(|l| l * hash_r.get(&l).unwrap_or(&0))
        .sum();

    println!("{}", acc);
}
