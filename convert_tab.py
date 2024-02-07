def convert_tab_input(tab_input):
    # Split the input into lines
    lines = tab_input.strip().split('\n')

    # Initialize an empty list to store the converted lines
    converted_lines = []

    # Mapping of fret numbers and symbols to note names
    fret_mapping = {
        '0': 'E', '1': 'F', '2': 'F#', '3': 'G', '4': 'G#',
        '5': 'A', '6': 'A#', '7': 'B', '8': 'C', '9': 'C#',
        'h': 'h', ':': ':', '^': '^', '.': '.', 'x': 'x'
    }

    # Iterate through each line and convert symbols to note names
    for line in lines:
        converted_line = '|--'
        for segment in line.split('--')[1:-1]:
            for char in segment:
                converted_line += fret_mapping[char] if char in fret_mapping else char
            converted_line += '--'
        converted_lines.append(converted_line + '|')

    # Combine the converted lines into a single string
    result = '\n'.join(converted_lines)
    return result

# Example usage
tab_input_example = """
e|-------------------3-3----------------3-3---------|
B|-------------------3-3----------------3-3---------|
G|-------------------0-0------0---------0-0---------|
D|----------0--2-----2-2---2-----2--0---0-0---------| 
A|-----0h2-----------2-2----------------2-2---------|
E|--3----------------0-0----------------3-3---------|
"""

example_output = convert_tab_input(tab_input_example)
print(example_output)