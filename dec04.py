import re

def read_input():
    lines = []
    with open("dec04_input.txt", "r") as infile:
        for line in infile:
            lines.append(line)
    return lines

def is_valid(line) -> bool:
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all(field+":" in line for field in fields)

def is_valid2(passport) -> bool:
    passport = passport.replace("\n", " ").replace("  ", " ")
    fields = passport.split(" ")
    dct = {}
    for field in fields:
        if len(field) > 0:
            key, value = field.split(":")
            dct[key] = value

    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if not all(key in dct for key in keys):
        return False

    if not (1920 <= int(dct["byr"]) <= 2002):
        return False
    if not (2010 <= int(dct["iyr"]) <= 2020):
        return False
    if not (2020 <= int(dct["eyr"]) <= 2030):
        return False

    if dct["hgt"].endswith("cm"):
        if not (150 <= int(dct["hgt"][:-2]) <= 193):
            return False
    elif dct["hgt"].endswith("in"):
        if not (59 <= int(dct["hgt"][:-2]) <= 76):
            return False
    else:
        return False
        assert False, f"Height ends with neither cm nor in, it is {dct['hgt']}"

    if re.compile("^#[0-9a-f]{6}$").match(dct["hcl"]) is None:
        return False

    if not (dct["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return False

    if re.compile("^[0-9]{9}$").match(dct["pid"]) is None:
        return False

    return True

def main(lines):
    count = 0
    passports = "".join(lines).split("\n\n")
    print(f"Total Passports: {len(passports)}")
    return sum([is_valid2(passport) for passport in passports])

if __name__ == "__main__":
    lines = read_input()
    print(f"Valid Passports: {main(lines)}")

