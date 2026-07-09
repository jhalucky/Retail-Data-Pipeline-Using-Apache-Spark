def write_parquet(df, output_path):

    (
        df.write
        .mode("overwrite")
        .partitionBy(
            "order_year",
            "order_month"
        )
        .parquet(output_path)
    )

    print("parquet generated.")