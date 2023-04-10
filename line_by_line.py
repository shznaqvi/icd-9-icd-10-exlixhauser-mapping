L = ["Geeks\n", "for\n", "Geeks\n"]

fileCcs = open('elixhouser_icd_9_10.csv', 'w')
wLine = 'Comorbidities, Elixhauser’s original ICD-9-CM, Elixhauser AHRQWeb ICD-9-CM, ICD-10, Enhanced ICD-9-CM '
fileCcs.writelines(wLine + '\n')

# Using readlines()
file1 = open('elixhouser_icd_9_10.txt', encoding="utf-8")

Lines = file1.readlines()

count = 0
sameField = True
textField = True
numField = False
fieldText = ''
lineText = ''
# Strips the newline character
for line in Lines:
    if len(line.strip()) == 0:
        print(f'length: {len(line)}')
    if not sameField:
        lineText += ", '" + fieldText + "'"
        fieldText = ''
        sameField = True
        print(f"LINE {len(line)}: " + lineText)
    count += 1
    # print(f"Line{count}: {line.strip()}")
    if line[1].isnumeric():
        numField = True
        if textField:
            lineText += "'" + fieldText + "'"
            fieldText = ''
            textField = False
            print(f"LINE {len(line)}: " + lineText)
        numIndex = line.find(' ')
        if ',' in line:
            fieldText += line.strip() + " "
        else:
            fieldText += line.strip()
            sameField = False

    #  ccsCode = line[0:numIndex]
    #  ccsDesc = line[numIndex:].strip()
    # # print("* CCS Code: " + ccsCode)
    #  # print("* CCS Label: " + ccsDesc)
    if not line[1].isnumeric():
        fileCcs.writelines(lineText + "\n")
        textField = True
        if numField:
            lineText = ""
            fieldText = ''
            numField = False
            # print(f"3LINE {len(line)}: " + lineText)

        fieldText += line.strip()

#         icdCodes = line.strip().split()
#         for c in icdCodes:
#             wLine = str(c) + ', ' + str(ccsCode) + ', ' + str(ccsDesc)+'\n'
#             print(wLine)
#             fileCcs.writelines(wLine)
# fileCcs.close()
