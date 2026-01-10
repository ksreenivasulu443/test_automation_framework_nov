#Two function
# 1. read files data
# 2. read db data


import pandas as pd
import snowflake.connector as snow
from pandasql import sqldf


def read_files(path, file_type, header=0, sep='|'):
    file_type = file_type.lower()
    if file_type == 'csv':
        df = pd.read_csv(path, header=header, sep=sep)
    elif file_type == 'excel':
        df = pd.read_excel(path)
    elif file_type == 'parquet':
        df = pd.read_parquet(path)
    elif file_type == 'txt':
        df = pd.read_csv(path)
    elif file_type == 'json':
        df = pd.read_json(path)
    else:
        print("Entered file format is not covered as part of current implementation. Please try with csv, excel and parquet")
        df = pd.DataFrame()

    return df

def read_db(database_type,query, creds_file, env='qa'):
    creds = pd.read_excel(creds_file)
    print("creds", creds)
    print("creds", creds.query(f"database_type == '{env}' "))
    creds = creds.query(f"database_type == '{env}' ")

    conn = snow.connect(
        user=creds.loc[0, 'username'],
        password=creds.loc[0, 'password'],
        account=creds.loc[0, 'account'],
        warehouse=creds.loc[0, 'warehouse']
    )

    print("conn", conn)
    df = pd.read_sql(sql=query, con=conn)
    return df