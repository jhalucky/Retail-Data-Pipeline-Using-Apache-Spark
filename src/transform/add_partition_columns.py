from pyspark.sql.functions import year, month


def add_partition_columns(df):

    df = (
        df.withColumn(
            "order_year",
            year("order_date")
        )
        .withColumn(
            "order_month",
            month("order_date")
        )
    )

    return df