L = ["Geeks\n", "for\n", "Geeks\n"]

fileCcs = open('elixhouser_icd_9_10.csv', 'w')
wLine = 'Comorbidities, Elixhauser’s original ICD-9-CM, Elixhauser AHRQWeb ICD-9-CM, ICD-10, Enhanced ICD-9-CM '
fileCcs.writelines(wLine + '\n')

# Using readlines()
file1 = open('sas_icd_10.txt.txt', encoding="utf-8")

lines = file1.readlines()

elixhauser = {}
key = ""
values = ()

# Loop through the lines and extract the variable name and values
for i in range(len(lines)):
    # Check if the line starts with a /*, indicating the variable name
    if lines[i].startswith('/*'):
        var_name = lines[i].replace('/*', '').replace('*/', '').strip()
        values = []
        # Loop through the lines after the variable name until the next variable name is found
        for j in range(i + 1, len(lines)):
            if lines[j].startswith('/*'):
                break
            # Check if the line is not empty
            elif lines[j].strip():
                # Extract the values from the parentheses and split them by comma
                values += lines[j].replace('(', '').replace(')', '').replace("'", '').strip().split(',')
        # Add the variable name and values as a key-value pair in the dictionary
        elixhauser[var_name] = values

# Print the resulting dictionary
print(elixhauser)
