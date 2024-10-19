word_to_number = {
    'one': 1, 
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

digits = []

def convert_w_to_n(letter):
    if letter.isdigit():
        digits.append(letter);

