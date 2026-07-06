def print_schema(df):

    df.printSchema()

def show_columns(df):

    return df.columns

def count_rows(df):

    return df.count()

def show_rows(df, rows=10):
    
    df.show(rows, truncate=False)


def describe_data(df):
    
    return df.describe().show()



