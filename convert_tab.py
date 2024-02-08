from fret_mapping import fret_mappings_standard, fret_mapping_open_d_tuning 
from strings_order import standard_tuning, open_d_tuning

def convert_tab_input(tab_input):
    # Split the input into lines
    lines = tab_input.strip().split('\n')

    # Initialize an empty list to store the converted lines
    converted_lines = []
    
    # Iterate through each line and convert fret numbers to note names
    for line_index, line in enumerate(lines):
        converted_line = ''
        string = open_d_tuning[line_index % len(open_d_tuning)]  # Cycle through strings_order based on line_index

        i = 0
        while i < len(line):
            char = line[i]

            if char.isdigit():
                fret = char
                while i + 1 < len(line) and line[i + 1].isdigit():
                    i += 1
                    fret += line[i]
                
                note = fret_mapping_open_d_tuning[string].get(fret, '?')
                converted_line += note
            elif char in '-|':
                converted_line += char
            elif char == 'h':
                converted_line += char
                i += 1  # Skip the next character as it's part of the hammer-on notation
                continue
            else:
                # For other notations or errors, use a placeholder or the character itself
                converted_line += '?'

            i += 1

        converted_lines.append(converted_line)

    # Combine the converted lines into a single string
    result = '\n'.join(converted_lines)
    return result

# Example usage
tab_input_example = """
|-----5-7-5h7-5h7-5h7-:-5h7-5---5-7-5-3b3.5-0----:----------0h3-5-7-5h7-:
|-5h8-----------------:-------8------------------:----------------------:
|-5-------------------:--------------------------:-^2-------------------:
|-0-------------------:--------------------------:-^0-----0-------------:
|---------------------:--------------------------:-^0-------------------:
|---------------------:--------------------------:-^x-------------------:
"""

example_output = convert_tab_input(tab_input_example)
print(example_output)
