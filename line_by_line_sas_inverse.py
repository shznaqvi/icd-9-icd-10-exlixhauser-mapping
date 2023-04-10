import csv

fileType = '9'
# Using readlines()
file1 = open('sas_icd_' + fileType + '.txt', encoding="utf-8")

lines = file1.readlines()

elixhauser = {}
key = ""
values = ()
for line in lines:
    if line.startswith('/*'):
        condition = line.replace('/*', '').replace('*/', '').strip()
        elixhauser[condition] = []
    elif line.startswith('('):
        codes = tuple(line.replace(' ', '').replace('(', '').replace(')', '').replace("'", "").strip().split(','))
        elixhauser[condition.strip()].extend(codes)

print(elixhauser)

# Save the key-value pairs to a CSV file
with open('elixhouser_icd_' + fileType + '.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['code', 'condition'])
    for line in lines:
        if line.startswith('/*'):
            key = line.replace('/*', '').replace('*/', '').strip()
        elif line.startswith('('):
            values = tuple(line.replace('(', '').replace(')', '').replace("'", "").strip().split(','))
            for value in values:
                writer.writerow([value.strip(), key.strip()])

print('CSV file saved successfully!')
