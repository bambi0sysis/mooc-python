from string import ascii_letters, digits


def change_case(orig_string: str):
    result = ""
    for letter in orig_string:
        result += letter.lower() if letter.isupper() else letter.upper()
    return result


def split_in_half(orig_string: str):
    return orig_string[: len(orig_string) // 2], orig_string[len(orig_string) // 2 :]


def remove_special_characters(orig_string: str):
    result = ""
    for letter in orig_string:
        if letter in ascii_letters or letter in digits or letter == " ":
            result += letter
    return result
