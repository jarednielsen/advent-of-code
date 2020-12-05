use std::io::Read;

fn is_valid(line: String) {
    println!("is_valid({})", line);
}

fn main() {
    let mut file = std::fs::File::open("dec04_input.txt").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    print!("{}", contents);

    let passports = contents.split("\n\n");
    let mut passports = passports.map(|x| x.replace("\n", " "));

    for p in &passports {
        println!("{}\n", p);
    }

    println!("{}", "hello there\nsecond line\n".replace("\n", " "));
    is_valid(passports.next().unwrap());
}