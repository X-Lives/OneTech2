import json 
import os

# This function creates a new HTML file for each object in the objects_json folder.
def create_object(num_id):
    num_id = str(num_id)
    os.chdir(retval)
    os.chdir('web')
    file_html = num_id + '.html'
    with open('Obj.html', "rb") as src, open(file_html, "wb") as dst:
        data = src.read()
        dst.write(data)
    for key in variables.keys():
        old = key
        new = variables[key]
        f = open(file_html, "r", encoding='UTF-8')
        lines = f.readlines()
        f.close()
        f = open(file_html, "w+", encoding='UTF-8')
        for line in lines:
            line = line.replace(old, new)
            f.write(line)
        f.close()
        #with open(file_html, 'r+', encoding='UTF-8') as filetxt:
        #    lines = filetxt.read()
        #    filetxt.seek(0)
        #    lines = lines.replace(old,new)
        #    filetxt.write(lines)
    for key in variables_null.keys():
        old = key
        new = variables_null[key]
        f = open(file_html, "r", encoding='UTF-8')
        lines = f.readlines()
        f.close()
        f = open(file_html, "w+", encoding='UTF-8')
        for line in lines:
            line = line.replace(old, new)
            f.write(line)
        f.close()
    os.chdir('..')
    os.chdir('output')
    os.chdir('objects_json')

retval = os.getcwd()
os.chdir('output')
# Reading the file count from file_count.json
with open('file_count.json', 'r', encoding='UTF-8') as f:
    file_count_dict = json.load(f)
    file_count = file_count_dict['file_count']
with open('object-null.json', 'r', encoding='UTF-8') as f:
    variables_null = json.load(f)

os.chdir('objects_json')

# Initializing Variables.
error = 0
file_num = 1

while error < 20:
    file_name = str(file_num) + '.json'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='UTF-8') as f:
            variables = json.load(f)
        create_object(file_num)
        error = 0
    else:
        error += 1
    file_num += 1
    #print('file_num:', file_num)
    #print('error:', error)
    #print(os.getcwd())

