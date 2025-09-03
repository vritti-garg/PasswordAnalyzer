import os

# Function to create leetspeak variations
def leetspeak(word):
    mapping = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5", "t": "7"}
    variations = {word}
    for char, sub in mapping.items():
        new_variations = set()
        for w in variations:
            if char in w:
                new_variations.add(w.replace(char, sub))
        variations.update(new_variations)
    return variations

# Function to generate wordlist
def generate_wordlist(inputs, birth_year=None):
    wordlist = set()

    for word in inputs:
        word = word.strip()
        if not word:
            continue

        # Basic variations
        wordlist.add(word.lower())
        wordlist.add(word.capitalize())
        wordlist.update(leetspeak(word.lower()))

        # Add only the given year (and nearby)
        if birth_year:
            wordlist.add(f"{word}{birth_year}")
            wordlist.add(f"{birth_year}{word}")
            # Add nearby years (+/- 1 for realism)
            try:
                y = int(birth_year)
                for delta in [-1, 1]:
                    wordlist.add(f"{word}{y+delta}")
                    wordlist.add(f"{y+delta}{word}")
            except ValueError:
                pass

        # Add common suffixes
        for suffix in ["123", "!", "@", "#", "$"]:
            wordlist.add(word + suffix)

    return wordlist

if __name__ == "__main__":
    # Take inputs
    name = input("Enter your name: ")
    nickname = input("Enter nickname: ")
    parent = input("Enter parent name: ")
    dob = input("Enter birth year: ")

    # Generate wordlist
    inputs = [name, nickname, parent]
    wordlist = generate_wordlist(inputs, dob)

    # Save to file
    os.makedirs("wordlist", exist_ok=True)
    filepath = "wordlist/custom_wordlist.txt"
    with open(filepath, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    print(f"[+] Wordlist generated with {len(wordlist)} entries")
    print(f"[+] Saved at {filepath}")