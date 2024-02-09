from fret_mapping import fret_mappings_standard, fret_mapping_open_d_tuning ,fret_mapping_dad_tuning
from strings_order import standard_tuning, open_d_tuning, dad_tuning

def convert_tab_input(tab_input):
    # Split the input into lines
    lines = tab_input.strip().split('\n')

    # Initialize an empty list to store the converted lines
    converted_lines = []
    
    # Iterate through each line and convert fret numbers to note names
    for line_index, line in enumerate(lines):
        converted_line = ''
        string = dad_tuning[line_index % len(dad_tuning)]  # Cycle through strings_order based on line_index

        i = 0
        while i < len(line):
            char = line[i]

            if char.isdigit():
                fret = char
                while i + 1 < len(line) and line[i + 1].isdigit():
                    i += 1
                    fret += line[i]
                
                note = fret_mapping_dad_tuning[string].get(fret, '?')
                converted_line += note
            elif char in '-|':
                converted_line += char
            elif char in 'x': # For muteted notes
                converted_line += char    # For strum pattern
            elif char in '^':
                converted_line += char  
            elif char in ':':
                converted_line += char  # For bend notes
            elif char in 'b':
                converted_line += char  # For pause notes
            elif char in '.':
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

# Example usage D A D G A D
tab_input_example = """
d|-----5-7-5h7-5h7-5h7-:-5h7-5---5-7-5-3b3.5-0----:----------0h3-5-7-5h7-:
A|-5h8-----------------:-------8------------------:----------------------:
G|-5-------------------:--------------------------:-^2-------------------:
D|-0-------------------:--------------------------:-^0-----0-------------:
A|---------------------:--------------------------:-^0-------------------:
D|---------------------:--------------------------:-^x-------------------:
 
 

"""

example_output = convert_tab_input(tab_input_example)
print(tab_input_example, example_output)
