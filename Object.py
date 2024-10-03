import os
import json

def count_files(directory):
    count = 0
    for _, _, files in os.walk(directory):
        count += len(files)
    return count

def file_writer(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)

def txt(file_content):
    # Split content into lines
    lines = file_content.strip().split('\n')

    # Initialize dictionary to store variables
    variables = {}

    # Loop through lines and assign values
    for i, line in enumerate(lines):
        if i == 1:
            # The second line is the Name
            variables['Obj-Name'] = line
        else:
            # Handle lines with key=value pairs
            if '=' in line:
                if 'biomes' in line:
                    # A lousy way to avoid the conflicts that '#' brings.
                    key, value = line.split('=')
                    variables['Obj-' + key] = value
                else:

                    sub = '='
                    count = line.count(sub)
                    sub_2 = ','
                    count_2 = line.count(sub_2)
                    if count == 1 and count_2 >= 1:
                        key, value = line.split('=')
                        variables['Obj-' + key] = value
                    else:
                        # Split by '#' first, as these separate multiple key=value pairs
                        parts = line.split('#')
                        for part in parts:
                            # Split by commas to separate key=value pairs
                            pairs = part.split(',')
                            for pair in pairs:
                                key, value = pair.split('=')
                                variables['Obj-' + key] = value

    # Output the variables dictionary
    print(variables)

    # Save:
    os.chdir(retval)
    path_2 = 'output'
    os.chdir(path_2)
    if not os.path.exists('objects_json'):
        os.mkdir('objects_json')
    os.chdir('objects_json')
    # Save as JSON file.
    with open(variables['Obj-id'] + '.json', 'w') as outfile:
        json.dump(variables, outfile)
    
    # Return to the original directory.
    os.chdir(retval_2)


# Initializing Variables.
error = 0
file_num = 0

retval = os.getcwd()
path = 'data/objects'
os.chdir(path)
retval_2 = os.getcwd()

# Set a threshold to prevent looping all the time.
while error < 20:
    file_name = str(file_num) + '.txt'
    # Checks if the file exists and returns bool.
    isfile=os.path.isfile(str(file_name))
    if isfile == False:
        # file does not exist, then skip.
        error = error + 1
        print(file_name)
    else:
        # file exists, read.
        print('ithas')
        error = 0
        # Open & Read File.
        with open(file_name, 'r') as file: 
            file_content = file.read()
            # txt()
            txt(file_content)
    # Check the next file.
    file_num = file_num + 1

# Go back to the original directory.
os.chdir(retval)
# => retvals/output/
os.chdir('output')
retval_3 = os.getcwd()
# => retvals/output/objects_json/
if not os.path.exists('objects_json'):
    os.mkdir('objects_json')
os.chdir('objects_json')
retval_4 = os.getcwd()
file_count = count_files(retval_4)
# => retvals/output/
os.chdir(retval_3)
file_writer('file_count.json', {'file_count': file_count})

# Test Txt.
file_content = """
id=11
Skin Tone A,B,C,D,E,F
mapChance=0.000000#biomes_0
"""
