def register_sales_table(df):

    df.createOrReplaceTempView("fact_sales")



def revenue_by_category_sql(spark):

        return spark.sql("""
             
           SELECT
                category,
                         SUM(sales_amount) AS total_revenue


           FROM fact_sales
           
           GROUP BY category
                         
           ORDER BY total_revenue DESC

""")