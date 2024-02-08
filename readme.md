Code to translate standard guitar tuned tabs to notes

To select tuning change line 14
string = open_d_tuning[line_index % len(open_d_tuning)]  # Cycle through strings_order based on line_index
string = tandard_tuning[line_index % len(tandard_tuning)]  # Cycle through strings_order based on line_index

and line 26
note = fret_mapping_open_d_tuning[string].get(fret, '?')

note = fret_mappings_standard[string].get(fret, '?')

To Use. Get your guitar tab from  https://tabs.ultimate-guitar.com
This is the example here
https://tabs.ultimate-guitar.com/tab/pink-floyd/wish-you-were-here-chords-44555
e|-------------------3-3----------------3-3---------|
B|-------------------3-3----------------3-3---------|
G|-------------------0-0------0---------0-0---------|
D|----------0--2-----2-2---2-----2--0---0-0---------| 
A|-----0h2-----------2-2----------------2-2---------|
E|--3----------------0-0----------------3-3---------|

Paste tab into the string 
tab_input_example = """
e|-------------------3-3----------------3-3---------|
B|-------------------3-3----------------3-3---------|
G|-------------------0-0------0---------0-0---------|
D|----------0--2-----2-2---2-----2--0---0-0---------| 
A|-----0h2-----------2-2----------------2-2---------|
E|--3----------------0-0----------------3-3---------|
"""
run 'python convert_tab.py'

Output equals
|-------------------G-G----------------G-G--------|
|-------------------G-G----------------G-G--------|
|-------------------E-E------E---------E-E--------|
|----------E--F#-----F#-F#---F#-----F#--E---E-E--------|
|-----EhF#-----------F#-F#----------------F#-F#--------|
|--G----------------E-E----------------G-G--------|