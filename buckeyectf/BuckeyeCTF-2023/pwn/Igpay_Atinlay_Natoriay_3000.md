# Igpay Atinlay Natoriay 3000 (beginner)
ustray isyay ayay afesay, efficientyay, emssystay ogramingpray anguagelay.

`nc chall.pwnoh.io 13370`

## Files
* Cargo.toml
* Cargo.lock
* src/main.rs
* run

## Solution
We have to crash the program to get the flag:
```
$ cat run
#!/bin/sh

./igpay-atinlay-natoriay-3000 \
    || printf "You crashed my program :(\n$FLAG"
$
```

The program itself is written in Rust and take a user input string to manipulate this:
```rust
use std::io::{self, Read, BufRead};

fn main() {
    let input = loop {
        match get_line() {
            Ok(my_str) => break my_str,
            Err(_) => {
                print!("Try again.");
                continue;
            }
        }
    };


    let mut output = String::new();

    for word in input.split_whitespace() {
        let first = &word[0..1];
        let rest = &word[1..];

        output += rest;
        output += first;
        output += "ay";
        output += " ";
    }

    print!("{output}");
}

fn get_line() -> Result<String, io::Error> {
    let mut input = String::new();

    io::BufReader::new(io::stdin().take(1862)).read_line(&mut input)?;

    Ok(input)
}
```

So the goal is to input an invalid string value, that causes a crash of the program. I just generated some random data with invalid ASCII literals and input this to the application:
```
$ cat out
ÐBA4 µ@0ÅáãÒ¢rÑaÐã CÁ±±°±@
$ cat out | nc chall.pwnoh.io 13370
thread 'main' panicked at 'byte index 1 is not a char boundary; it is inside 'µ' (bytes 0..2) of `µ@0ÅáãÒ¢rÑaÐã`', src/main.rs:18:22
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
You crashed my program :(
bctf{u$trAy_1SyAy_Af3$ay_aNDy@Y_3cUR3s@y}
$
```