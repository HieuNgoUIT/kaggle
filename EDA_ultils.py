import pandas as pd
def check_basic_df(df):
    print(df.head())
    print(df.info())
    print(df.isnull().sum())
    print(df.shape)

    ##check duplicated
    print(len(df[df.duplicated()]))
