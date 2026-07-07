from src.config.spark_session import get_spark_session
from pyspark.sql.functions import col, when, count

def validate_emails(df, email_column):

    spark = get_spark_session()

    invalid_rows = []

    for index, email in enumerate(df[email_column]):

        if df.select([
        count(
            when(col(email_column).isNull(), email_column)
        ).alias(email_column)]):
            
            invalid_rows.append(index)

            continue

        if "@" not in email:
            invalid_rows.append(index)
            continue

        username, domain = email.split("@", 1)

        if username == "" or email == "":
            invalid_rows.append(index)
            continue

        if "." not in domain:
            invalid_rows.append(index)
            continue

    print("\nInvalid Rows:")
    print(invalid_rows)


    return invalid_rows

