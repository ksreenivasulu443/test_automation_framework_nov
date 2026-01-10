from utility.read_library import read_db, read_files
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
    print("==" * 100)
    print("ind", ind)
    print("=="*100)
    print("row", row)
    print("==" * 100)
    print("type(row)", type(row))
    print("row['source_type']",row['source_type'])
    print("row['source_path']", row['source_path'])

    source = read_files(path=row['source_path'],file_type=row['source_type'], header=0, sep=',')
    print(source)

d = {1:'sreenii', 2:'rahul'}

for key, value in d.items():
    print(key)
    print(value)