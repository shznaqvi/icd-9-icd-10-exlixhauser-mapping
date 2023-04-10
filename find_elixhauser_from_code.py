# Define a dictionary for ICD-9 codes and their corresponding conditions
icd_9 = {'Congestive Heart Failure': ['39891', '40201', '40211', '40291', '40401', '40403', '40411', '40413', '40491',
                                      '40493', '4254', '4255', '4257', '4258', '4259', '428'],
         'Cardiac Arrhythmia': ['4260', '42613', '4267', '4269', '42610', '42612', '4270', '4271', '4272', '4273',
                                '4274', '4276', '4278', '4279', '7850', '99601', '99604', 'V450', 'V533'],
         'Valvular Disease': ['0932', '394', '395', '396', '397', '424', '7463', '7464', '7465', '7466', 'V422',
                              'V433'],
         'Pulmonary Circulation Disorders': ['4150', '4151', '416', '4170', '4178', '4179'],
         'Peripheral Vascular Disorders': ['0930', '4373', '440', '441', '4431', '4432', '4438', '4439', '4471', '5571',
                                           '5579', 'V434'], 'Hypertension Uncomplicated': ['401'],
         'Hypertension Complicated': ['402', '403', '404', '405'],
         'Paralysis': ['3341', '342', '343', '3440', '3441', '3442', '3443', '3444', '3445', '3446', '3449'],
         'Other Neurological Disorders': ['3319', '3320', '3321', '3334', '3335', '33392', '334', '335', '3362', '340',
                                          '341', '345', '3481', '3483', '7803', '7843'],
         'Chronic Pulmonary Disease': ['4168', '4169', '490', '491', '492', '493', '494', '495', '496', '500', '501',
                                       '502', '503', '504', '505', '5064', '5081', '5088'],
         'Diabetes Uncomplicated': ['2500', '2501', '2502', '2503'],
         'Diabetes Complicated': ['2504', '2505', '2506', '2507', '2508', '2509'],
         'Hypothyroidism': ['2409', '243', '244', '2461', '2468'],
         'Renal Failure': ['40301', '40311', '40391', '40402', '40403', '40412', '40413', '40492', '40493', '585',
                           '586', '5880', 'V420', 'V451', 'V56'],
         'Liver Disease': ['07022', '07023', '07032', '07033', '07044', '07054', '0706', '0709', '4560', '4561', '4562',
                           '570', '571', '5722', '5723', '5724', '5728', '5733', '5734', '5738', '5739', 'V427'],
         'Peptic Ulcer Disease excluding bleeding': ['5317', '5319', '5327', '5329', '5337', '5339', '5347', '5349'],
         'AIDS/HIV': ['042', '043', '044'], 'Lymphoma': ['200', '201', '202', '2030', '2386'],
         'Metastatic Cancer': ['196', '197', '198', '199'],
         'Solid Tumor without Metastasis': ['140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150',
                                            '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161',
                                            '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172',
                                            '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184',
                                            '185', '186', '187', '188', '189', '190', '191', '192', '193', '194',
                                            '195'],
         'Rheumatoid Arthritis/collagen': ['446', '7010', '7100', '7101', '7102', '7103', '7104', '7108', '7109',
                                           '7112', '714', '7193', '720', '725', '7285', '72889', '72930'],
         'Coagulopathy': ['286', '2871', '2873', '2874', '2875'], 'Obesity': ['2780'],
         'Weight Loss': ['260', '261', '262', '263', '7832', '7994'],
         'Fluid and Electrolyte Disorders': ['2536', '276'], 'Blood Loss Anemia': ['2800'],
         'Deficiency Anemia': ['2801', '2808', '2809', '281'],
         'Alcohol Abuse': ['2652', '2911', '2912', '2913', '2915', '2918', '2919', '3030', '3039', '3050', '3575',
                           '4255', '5353', '5710', '5711', '5712', '5713', '980', 'V113'],
         'Drug Abuse': ['292', '304', '3052', '3053', '3054', '3055', '3056', '3057', '3058', '3059', 'V6542'],
         'Psychoses': ['2938', '295', '29604', '29614', '29644', '29654', '297', '298'],
         'Depression': ['2962', '2963', '2965', '3004', '309', '311']}

# Define a dictionary for ICD-10 codes and their corresponding conditions
icd_10 = {
    'Congestive Heart Failure': ['I099', 'I110', 'I130', 'I132', 'I255', 'I420', 'I425', 'I426', 'I427', 'I428', 'I429',
                                 'I43', 'I50', 'P290'],
    'Cardiac Arrhythmia': ['I441', 'I442', 'I443', 'I456', 'I459', 'I47', 'I48', 'I49', 'R000', 'R001', 'R008', 'T821',
                           'Z450', 'Z950'],
    'Valvular Disease': ['A520', 'I05', 'I06', 'I07', 'I08', 'I091', 'I098', 'I34', 'I35', 'I36', 'I37', 'I38', 'I39',
                         'Q230', 'Q231', 'Q232', 'Q233', 'Z952', 'Z953', 'Z954'],
    'Pulmonary Circulation Disorders': ['I26', 'I27', 'I280', 'I288', 'I289'],
    'Peripheral Vascular Disorders': ['I70', 'I71', 'I731', 'I738', 'I739', 'I771', 'I790', 'I792', 'K551', 'K558',
                                      'K559', 'Z958', 'Z959'], 'Hypertension Uncomlicated': ['I10'],
    'Hypertension comlicated': ['I11', 'I12', 'I13', 'I15'],
    'Paralysis': ['G041', 'G114', 'G801', 'G802', 'G81', 'G82', 'G830', 'G831', 'G832', 'G833', 'G834', 'G839'],
    'Other Neurological Disorders': ['G10', 'G11', 'G12', 'G13', 'G20', 'G21', 'G22', 'G254', 'G255', 'G312', 'G318',
                                     'G319', 'G32', 'G35', 'G36', 'G37', 'G40', 'G41', 'G931', 'G934', 'R470', 'R56'],
    'Chronic Pulmonary Disease': ['I278', 'I279', 'J40', 'J41', 'J42', 'J43', 'J44', 'J45', 'J46', 'J47', 'J60', 'J61',
                                  'J62', 'J63', 'J64', 'J65', 'J66', 'J67', 'J684', 'J701', 'J703'],
    'Diabetes Uncomplicated': ['E100', 'E101', 'E109', 'E110', 'E111', 'E119', 'E120', 'E121', 'E129', 'E130', 'E131',
                               'E139', 'E140', 'E141', 'E149'],
    'Diabetes Complicated': ['E102', 'E103', 'E104', 'E105', 'E106', 'E107', 'E108', 'E112', 'E113', 'E114', 'E115',
                             'E116', 'E117', 'E118', 'E122', 'E123', 'E124', 'E125', 'E126', 'E127', 'E128', 'E132',
                             'E133', 'E134', 'E135', 'E136', 'E137', 'E138', 'E142', 'E143', 'E144', 'E145', 'E146',
                             'E147', 'E148'], 'Hypothyroidism': ['E00', 'E01', 'E02', 'E03', 'E890'],
    'Renal Failure': ['I120', 'I131', 'N18', 'N19', 'N250', 'Z490', 'Z491', 'Z492', 'Z940', 'Z992'],
    'Liver Disease': ['B18', 'I85', 'I864', 'I982', 'K70', 'K711', 'K713', 'K714', 'K715', 'K717', 'K72', 'K73', 'K74',
                      'K760', 'K762', 'K763', 'K764', 'K765', 'K766', 'K767', 'K768', 'K769', 'Z944'],
    'Peptic Ulcer Disease excluding bleeding': ['K257', 'K259', 'K267', 'K269', 'K277', 'K279', 'K287', 'K289'],
    'AIDS/HIV': ['B20', 'B21', 'B22', 'B24'],
    'Lymphoma': ['C81', 'C82', 'C83', 'C84', 'C85', 'C88', 'C96', 'C900', 'C902'],
    'Metastatic Cancer': ['C77', 'C78', 'C79', 'C80'],
    'Solid Tumor without Metastasis': ['C00', 'C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C10',
                                       'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21',
                                       'C22', 'C23', 'C24', 'C25', 'C26', 'C30', 'C31', 'C32', 'C33', 'C34', 'C37',
                                       'C38', 'C39', 'C40', 'C41', 'C43', 'C45', 'C46', 'C47', 'C48', 'C49', 'C50',
                                       'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 'C58', 'C60', 'C61', 'C62',
                                       'C63', 'C64', 'C65', 'C66', 'C67', 'C68', 'C69', 'C70', 'C71', 'C72', 'C73',
                                       'C74', 'C75', 'C76', 'C97'],
    'Rheumatoid Arthritis/collagen': ['L940', 'L941', 'L943', 'M05', 'M06', 'M08', 'M120', 'M123', 'M30', 'M310',
                                      'M311', 'M312', 'M313', 'M32', 'M33', 'M34', 'M35', 'M45', 'M461', 'M468',
                                      'M469'],
    'Coagulopathy': ['D65', 'D66', 'D67', 'D68', 'D691', 'D693', 'D694', 'D695', 'D696'], 'Obesity': ['E66'],
    'Weight Loss': ['E40', 'E41', 'E42', 'E43', 'E44', 'E45', 'E46', 'R634', 'R64'],
    'Fluid and Electrolyte Disorders': ['E222', 'E86', 'E87'], 'Blood Loss Anemia': ['D500'],
    'Deficiency Anemia': ['D508', 'D509', 'D51', 'D52', 'D53'],
    'Alcohol Abuse': ['F10', 'E52', 'G621', 'I426', 'K292', 'K700', 'K703', 'K709', 'T51', 'Z502', 'Z714', 'Z721'],
    'Drug Abuse': ['F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F18', 'F19', 'Z715', 'Z722'],
    'Psychoses': ['F20', 'F22', 'F23', 'F24', 'F25', 'F28', 'F29', 'F302', 'F312', 'F315'],
    'Depression': ['F204', 'F313', 'F314', 'F315', 'F32', 'F33', 'F341', 'F412', 'F432']}


# Define a function to get the condition associated with a code in a given ICD dictionary
def get_conditions(code, icd_dict):
    matches = []
    for condition, codes in icd_dict.items():
        if code in codes:
            matches.append(condition)
    return matches if matches else None


test_code = '40403'
# Test the function for ICD-9 and ICD-10 dictionaries with a sample code
print(f'ICD-9: {get_conditions(test_code, icd_9)}')
print(f'ICD-10: {get_conditions(test_code, icd_10)}')
matched_codes = []

print("ICD-9 codes that match multiple conditions:")
for codes in icd_9.values():
    for code in codes:
        icd_9_matches = get_conditions(code, icd_9)
        if icd_9_matches and len(icd_9_matches) > 1 and code not in matched_codes:
            matched_codes.append(code)
            print(f'ICD-9 code {code} | conditions: {icd_9_matches}')

print("\nICD-10 codes that match multiple conditions:")
for codes in icd_10.values():
    for code in set(codes):
        icd_10_matches = get_conditions(code, icd_10)
        if icd_10_matches and len(icd_10_matches) > 1 and code not in matched_codes:
            matched_codes.append(code)
            print(f'ICD-10 code {code} | conditions: {icd_10_matches}')
