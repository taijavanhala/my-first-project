import string

ALPHABET = string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def load_config(filename: str) -> tuple[list[str], str]:
    """
    Load rotor and reflector configuration from a file.

    Expected format:
    Rotor1:<26 letters>
    Rotor2:<26 letters>
    Rotor3:<26 letters>
    Reflector:<26 letters>
    """
    rotors: list[str] = ["", "", ""]
    reflector: str = ""

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if key == "Rotor1":
                rotors[0] = value
            elif key == "Rotor2":
                rotors[1] = value
            elif key == "Rotor3":
                rotors[2] = value
            elif key == "Reflector":
                reflector = value

    return rotors, reflector


def step_rotors(positions: list[int]) -> None:
    """
    Step rotors like a simple odometer.

    Rotor1 always steps.
    When Rotor1 wraps around from 25 -> 0, Rotor2 steps, etc.
    """
    positions[0] = (positions[0] + 1) % 26

    if positions[0] == 0:
        positions[1] = (positions[1] + 1) % 26

        if positions[1] == 0:
            positions[2] = (positions[2] + 1) % 26


def forward_pass(letter: str, rotors: list[str], positions: list[int]) -> str:
    """
    Forward pass through rotors 1 -> 3.
    """
    idx = ALPHABET.index(letter)

    for rotor_index in range(3):
        pos = positions[rotor_index]
        offset_index = (idx + pos) % 26
        mapped_letter = rotors[rotor_index][offset_index]
        idx = ALPHABET.index(mapped_letter)

    return ALPHABET[idx]


def reflect(letter: str, reflector: str) -> str:
    """
    Reflect letter using reflector mapping.
    """
    idx = ALPHABET.index(letter)
    return reflector[idx]


def reverse_pass(letter: str, rotors: list[str], positions: list[int]) -> str:
    """
    Reverse pass through rotors 3 -> 1.
    """
    idx = ALPHABET.index(letter)

    for rotor_index in range(2, -1, -1):
        pos = positions[rotor_index]
        # We know rotors[rotor_index][j] was used in forward pass.
        # Now we find j such that rotors[rotor_index][j] is our current letter.
        rotor = rotors[rotor_index]
        j = rotor.index(ALPHABET[idx])
        original_index = (j - pos) % 26
        idx = original_index

    return ALPHABET[idx]


def encrypt_character(
    ch: str, rotors: list[str], reflector: str, positions: list[int]
) -> str:
    """
    Encrypt a single character with Enigma:
    - step rotors
    - forward pass through rotors
    - reflector
    - reverse pass through rotors
    """
    # Step rotors before processing this character
    step_rotors(positions)

    letter = ch.upper()
    if letter not in ALPHABET:
        return ch

    # Forward through rotors
    letter = forward_pass(letter, rotors, positions)

    # Reflect
    letter = reflect(letter, reflector)

    # Reverse through rotors
    letter = reverse_pass(letter, rotors, positions)

    return letter


def main() -> None:
    print("Insert config(filename): ", end="")
    config_filename = input().strip()

    rotors, reflector = load_config(config_filename)

    print("Insert plugs (y/n)?: ", end="")
    plugs_answer = input().strip().lower()

    # Plugboard not implemented; just print info
    print("No extra plugs inserted.")
    print("Enigma initialized.\n")

    while True:
        print("Insert row (empty stops): ", end="")
        row = input()

        if row == "":
            print("\nEnigma closing.")
            break

        # Reset rotor positions to [0, 0, 0] for each row
        positions: list[int] = [0, 0, 0]

        result_chars: list[str] = []

        for ch in row:
            if ch.upper() in ALPHABET:
                illuminated = encrypt_character(ch, rotors, reflector, positions)
                print(f'Character "{ch.upper()}" illuminated as "{illuminated}"')
                result_chars.append(illuminated)
            else:
                # If non-letter characters appear, we could pass them through unchanged.
                # But the examples use only A-Z.
                result_chars.append(ch)

        converted = "".join(result_chars)
        print(f'Converted row - "{converted}".\n')


if __name__ == "__main__":
    main()
