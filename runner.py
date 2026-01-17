from utility.read_library import read_db, read_files
from utility.validations import count_check
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
testcases = pd.read_excel("/Users/admin/PycharmProjects/test_automation_framework_nov/configs/test_cases.xlsx")

print("test cases:")
print(testcases)
testcases = testcases.query("execution_ind=='Y' ")

print("test cases after selection exe = 'Y' :")
print(testcases)

for ind, row in testcases.iterrows():
    # print("==" * 100)
    # print("ind", ind)
    # print("=="*100)
    # print("row", row)
    # print("==" * 100)
    # print("type(row)", type(row))
    # print("row['source_type']",row['source_type'])
    # print("row['source_path']", row['source_path'])

    if row['source_type'] == 'database':
        source = read_db(query = row['source_query'],
                         creds_file='/Users/admin/PycharmProjects/test_automation_framework_nov/configs/creds_file.xlsx'
                        , env='qa')
    else:
        source = read_files(path=row['source_path'],file_type=row['source_type'], header=0, sep=',')

    if row['target_type'] == 'database':
        target = read_db(query=row['target_query'],
                         creds_file='/Users/admin/PycharmProjects/test_automation_framework_nov/configs/creds_file.xlsx'
                         , env='qa')
    else:
        target = read_files(path=row['target_path'], file_type=row['target_type'], header=0, sep=',')
    print("==" * 100)
    print("source data is", source)
    print("==" * 100)
    print("target data is", target)
    print("==" * 100)
    count_check(source_df=source, target_df=target)