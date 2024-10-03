import os
import json

def txt(file_content):
    # Split content into lines
    Strings = file_content.strip().split(' ')

    # Initialize dictionary to store variables
    variables = {}

    for i, String in enumerate(Strings):
        value = String
        variables['name'] = str(file_num)
        variables[i] = value
        variables['tga'] = str(file_num) + '.tga'
    
    # Output the variables dictionary
    print(variables)
    
    # Save:
    os.chdir(retval)
    path_2 = 'output'
    os.chdir(path_2)
    if not os.path.exists('sprites_json'):
        os.mkdir('sprites_json')
    os.chdir('sprites_json')
    # Save as JSON file.
    with open(variables['name'] + '.json', 'w') as outfile:
        json.dump(variables, outfile)
    
    # Return to the original directory.
    os.chdir(retval_2)

# Initializing Variables.
error = 50
file_num = 50

retval = os.getcwd()
path = 'data/sprites'
os.chdir(path)
retval_2 = os.getcwd()

# Set a threshold to prevent looping all the time.
while error < 70:
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
        error = 50
        with open(file_name, 'r') as file: 
            file_content = file.read()
            # txt()
            txt(file_content)
    # Check the next file.
    file_num = file_num + 1

# Test Txt.
file_content = """
BodyWhite 0 -1 32
"""
