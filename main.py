def main():
    person1 = input("Input name of Person 1: ")
    
    person2 = input("Input name of Person 2: ")

    compatibility = calculate(person1, person2)
    print(f"{person1} and {person2} are {compatibility} % compatible")

def calculate(person1, person2):
    combined_names = (person1 + person2).upper()
    
    letter_counts = []
    for letter in "TRUELOVE":
        letter_count = combined_names.count(letter)
        letter_counts.append(letter_count)
        print(f"Count of '{letter}' in combined names: {letter_count}")

    print(f"Initial letter counts: {letter_counts}")

    while len(letter_counts) > 2:
        new_counts = []
        for i in range(len(letter_counts) - 1):
            new_counts.append((letter_counts[i] + letter_counts[i + 1]) % 10)
        letter_counts = new_counts
        print(f"New letter counts: {letter_counts}")

    compatibility = int("".join(map(str, letter_counts)))
    print(f"Final compatibility: {compatibility}")
    
    return compatibility

main()
