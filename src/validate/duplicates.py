def validate_duplicate_rows(df):

    total_rows = df.count()

    unique_rows = df.dropDuplicates().count()

    duplicate_rows = total_rows - unique_rows

    print(f"Duplicate rows: {duplicate_rows}")

    return df


def validate_duplicate_primary_keys(df, column_name):

    total_rows = df.count()

    unique_rows = df.dropDuplicates([column_name]).count()

    duplicate_rows = total_rows - unique_rows

    print(f"Duplicate primary keys rows: {duplicate_rows}")

    return df