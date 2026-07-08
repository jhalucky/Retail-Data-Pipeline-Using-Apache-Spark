from pyspark.sql.functions import col 
from schemas import FACT_SALES_COLUMNS


def create_fact_sales(df):

    df = df.withColumn(
        "sales_amount",
        col("quantity") * col("unit_price")
    )

    df = df.select(*FACT_SALES_COLUMNS)
    


    return df


