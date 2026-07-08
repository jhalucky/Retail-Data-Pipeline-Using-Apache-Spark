from pyspark.sql.functions import sum, desc


def top_customers(df, limit=10):

    customer_df = (
        df.groupBy("customer_id","first_name", "last_name")
        .agg(
            sum("sales_amount").alias("total_orders")
        )
        .orderBy(desc("total_orders"))
        .limit(limit)
    )

    return customer_df