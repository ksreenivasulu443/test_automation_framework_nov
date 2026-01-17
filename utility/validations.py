def count_check(source_df, target_df):
    src_cnt = source_df.shape[0]
    tgt_cnt = target_df.shape[0]
    print("=="*100)
    if src_cnt == tgt_cnt:
        print(f"count is matching between source and target..source count is {src_cnt} and target count is {tgt_cnt}")
    else:
        print(f"count is not matching between source and target..source count is {src_cnt} and target count is {tgt_cnt}")
    print("==" * 100)