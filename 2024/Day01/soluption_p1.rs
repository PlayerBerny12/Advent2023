use std::io;

fn main() {
    let mut vec_l = vec![];
    let mut vec_r = vec![];
    let lines = io::stdin().lines();

    for line in lines {
        let line = line.unwrap();
        let (l, r) = line.split_once("   ").unwrap();

        let l_num: i32 = l.parse().unwrap();
        let r_num: i32 = r.parse().unwrap();

        vec_l.push(l_num);
        vec_r.push(r_num);
    }

    vec_l.sort_unstable();
    vec_r.sort_unstable();

    let acc: u32 = vec_l
        .into_iter()
        .zip(vec_r.into_iter())
        .map(|(l, r)| l.abs_diff(r))
        .sum();

    println!("{}", acc);
}
