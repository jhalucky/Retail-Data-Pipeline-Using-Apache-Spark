from pyspark.sql.functions import sum, desc


def top_selling_products(df, limit=10):

    product_df = (
        df.groupBy("product_name")
        .agg(sum("sales_amount").alias("total_revenue"))
        .orderBy("total_revenue")
        .limit(limit)
    )


    return product_df


def top_categories(df):

    category_df = (
        df.groupBy("category")
        .agg(
            sum("sales_amount").alias("total_revenue")
        )
        .orderBy(desc("total_revenue"))
    ) 

    return category_df