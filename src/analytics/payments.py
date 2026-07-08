from pyspark.sql.functions import count, desc

def payment_distribution(df):

    payment_df = (
        df.groupBy("payment_method")
        .agg(
            count("*").alias("total_orders")
        )
        .orderBy(desc("total_orders"))
    )

    return payment_df


