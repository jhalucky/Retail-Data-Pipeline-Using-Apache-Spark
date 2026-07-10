from src.config.spark_session import get_spark_session
from src.extract.read_csv import read_csv
from src.extract.explore_df import print_schema, show_columns, describe_data, count_rows, show_rows
from src.experiments.lazy_evaluation import lazy_evaluation_demo
from src.validate.missing import validate_missing_values
from src.validate.duplicates import validate_duplicate_rows
from src.validate.primary_key import validate_duplicate_primary_keys
from src.validate.email import validate_emails
from src.validate.schema import validate_schema
from src.transform.trim_whitespace import trim_whitespace
from src.transform.standardize_case import standardize_case
from src.transform.clean_email import clean_email
from src.transform.convert_dtypes import convert_dtypes
from src.transform.joins import create_sales_dataframe
from src.transform.create_fact_sales import create_fact_sales
from src.analytics.revenue import revenue_by_category, revenue_by_state, revenue_by_month
from src.load.write_parquet import write_parquet
from src.extract.read_parquet import read_parquet
from src.transform.add_partition_columns import add_partition_columns
from schemas import CUSTOMER_SCHEMA, ORDER_ITEM_SCHEMA, ORDER_SCHEMA, PAYMENT_SCHEMA, PRODUCT_SCHEMA


spark = get_spark_session()
customer_df = read_csv(spark, "data/raw/customers.csv")
product_df = read_csv(spark, "data/raw/products.csv")
order_df = read_csv(spark, "data/raw/orders.csv")
order_item_df = read_csv(spark, "data/raw/order_items.csv")
payment_df = read_csv(spark, "data/raw/payments.csv")


# customer_df run
# print_schema(customer_df)
# print(f"spark version : {spark.version}")
# print(show_columns(customer_df))
# print(describe_data(customer_df))
# print(count_rows(customer_df))
# print(show_rows(customer_df, 10))
# print(validate_missing_values(customer_df))

# print(validate_duplicate_rows(customer_df))
# print(validate_duplicate_primary_keys(customer_df, "customer_id"))
# print(count_rows(customer_df))
# validate_emails(customer_df, "email")
# lazy_evaluation_demo(customer_df)
# validate_schema(customer_df, CUSTOMER_SCHEMA)
# trim_whitespace(customer_df)
# standardize_case(customer_df)
# customer_df=clean_email(customer_df)
# customer_df = convert_dtypes(customer_df, CUSTOMER_SCHEMA)
# print(describe_data(customer_df))
# print(show_rows(customer_df, 10))




# order_df run

# print_schema(order_df)
# print(show_columns(order_df))
# print(describe_data(order_df))
# print(count_rows(order_df))
# print(show_rows(order_df, 20))
# print(validate_missing_values(order_df))
# print(validate_duplicate_rows(order_df))
# print(validate_duplicate_primary_keys(order_df, "order_id"))

sales_df = create_sales_dataframe(
    customer_df, order_df, order_item_df, product_df, payment_df
)
# show_rows(sales_df, 10)
# print_schema(sales_df)

# category_revenue_df = revenue_by_category(sales_df)
# category_revenue_df = revenue_by_state(sales_df)
# category_revenue_df = revenue_by_month(sales_df)
fact_sales_df = create_fact_sales(sales_df)
# show_rows(fact_sales_df)

# write_parquet(customer_df, "data/processed/customers")
# write_parquet(product_df, "data/processed/products")
# fact_sales_df = read_parquet(spark, "data/processed/fact_sales")
# fact_sales_df = add_partition_columns(fact_sales_df)

# write_parquet(fact_sales_df, "data/processed/fact_sales")
print(f"Before: {fact_sales_df.rdd.getNumPartitions()}")
fact_sales_df = fact_sales_df.repartition(8)
print(f"After: {fact_sales_df.rdd.getNumPartitions()}")
# show_rows(fact_sales_df)
spark.stop()