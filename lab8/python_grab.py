import json

# load json file
with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

# define extracting 
fields = ['name', 'html_url', 'updated_at', 'visibility']

with open('chacon.csv', 'a') as outfile: 
    for r in data[:5]:
        extracted_fields = [r[a] for a in fields]
        line = ','.join(extracted_fields) + '\n'
        outfile.write(line)