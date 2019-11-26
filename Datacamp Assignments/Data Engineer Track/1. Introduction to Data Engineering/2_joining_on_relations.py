# Complete the SELECT statement
data = pd.read_sql("""
SELECT * FROM "Customer"
INNER JOIN "Order"
ON "Order"."customer_id"="Customer"."id"
""", db_engine)

# Show the id column of data
print(data.id)

# <script.py> output:
#        id  id
#     0   1   1
#     1   2   2
#     2   1   3
#     3   5   4
#     4   3   5

# data.id outputs 2 columns. This is often a source of error, so a better strategy here would be to select specific columns or use the AS keyword in SQL to rename columns.

