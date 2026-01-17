
from pandasql import sqldf
from utility.reporting import report_output
def count_check(source_df, target_df):
    src_cnt = source_df.shape[0]
    tgt_cnt = target_df.shape[0]
    print("=="*100)
    if src_cnt == tgt_cnt:
        print(f"count is matching between source and target..source count is {src_cnt} and target count is {tgt_cnt}")
        report_output(validation_type='count_check',
                      status='PASS', details=f"count is matching between source and target..source count is {src_cnt} and target count is {tgt_cnt}")
    else:
        print(f"count is not matching between source and target..source count is {src_cnt} and target count is {tgt_cnt}")
        report_output(validation_type='count_check',
                      status='FAIL',
                      details=f"count is matching between source and target..source count is {src_cnt} and target count is {tgt_cnt}")
    print("==" * 100)

def duplicate_check(target_df,pkey_column):
    original_count = target_df.shape[0] # 5
    count_after_drop = target_df[pkey_column].drop_duplicates().shape[0] # 5
    if original_count == count_after_drop:
        print("no duplicates")
    else:
        print("duplicates present")

def duplicate_check_sql(target_df, pkey_column):
    print("==" * 100)
    failed_df = sqldf(f"select {pkey_column}, count(1) from target_df group by {pkey_column} having count(1)>1 ")
    if  failed_df.empty:
        print("no duplicates")
        report_output(validation_type='duplicate_check',
                      status='PASS',
                      details=f"no duplicate")

    else:
        print("duplicates present")
        print(failed_df)
        report_output(validation_type='duplicate_check',
                      status='FAIL',
                      details=failed_df)
    print("==" * 100)

def null_check(target_df,null_column):
    null_column_list = str(null_column).split(',')
    for col in null_column_list:
        null_rows = target_df[target_df[col].isnull()]

        #null_rows = sqldf(f"select * from target_df where {null_column} is null")
        print("==" * 100)
        if null_rows.shape[0]>0:
            print(f" {col} Null rows present")
            print("null rows", null_rows)
        else:
            print(f" {col} No nulls presennt")
        print("==" * 100)

def data_compare(source_df, target_df):
    query = """select * from source_df except select * from target_df
                union all
                select * from target_df except select * from source_df"""
    failed = sqldf(query)
    if failed.shape[0]>0:
        print("data is not matching")
        print(failed)
    else:
        print("data is matching")