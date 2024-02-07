import re
from music21 import stream, meter, key, note

def detect_tuning(tab_input):
    # Define a standard tuning for each string
    standard_tuning = ['E', 'B', 'G', 'D', 'A', 'E']

    return standard_tuning

def parse_guitar_tab(tab_input):
    # Define a regular expression pattern for extracting fret numbers
    pattern = re.compile(r'---(\d+)--', re.IGNORECASE)

    # Tokenize the input
    tokens = pattern.findall(tab_input)

    # Process tokens to extract fret information
    frets = [int(token) for token in tokens]

    # Reverse the list to match the order of strings (E, A, D, G, B, e)
    frets.reverse()

    return frets

def generate_note_names(frets, tunings, keys):
    note_names = []

    for string_index, fret in enumerate(frets):
        # Find the index of the reference note in the keys
        reference_note_index = keys.index(tunings[string_index])

        # Map fret to note name using the standard tuning and keys
        note_name = keys[(fret - reference_note_index) % len(keys)]
        note_names.append(note_name)

    return note_names

# Example usage with dynamically detected standard tuning and keys
standard_tuning_keys = ['E', 'A', 'D', 'G', 'B', 'E']

tab_input_example = """
E|---0--|
B|---0--|
G|---0--|
D|---0--|
A|---1--|
E|---1--|
"""

standard_tuning = detect_tuning(tab_input_example)
frets = parse_guitar_tab(tab_input_example)
note_names = generate_note_names(frets, standard_tuning, standard_tuning_keys)

print("Note Names:", note_names)