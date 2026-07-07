def validate_schema(df, expected_columns):

    actual_columns = list(df.columns)

    if actual_columns == expected_columns:
        print("\nSchema Validation passed.")
        return True
    
    print("\nSchema Validation failed")

    print("\nExpected Columns:")
    print(expected_columns)

    print("\nActual Columns")
    print(actual_columns)

    return False