connection_uri = "postgresql://repl:password@localhost:5432/dwh"
db_engine = sqlalchemy.create_engine(connection_uri)

def load_to_dwh(recommendations):
    recommendations.to_sql("recommendations", db_engine, if_exists="replace")


''' 
In [1]: recommendations.to_sql?
Signature: recommendations.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None, method=None)
Docstring:
Write records stored in a DataFrame to a SQL database.

Databases supported by SQLAlchemy [1]_ are supported. Tables can be
newly created, appended to, or overwritten.

Parameters
----------
name : string
    Name of SQL table.
con : sqlalchemy.engine.Engine or sqlite3.Connection
    Using SQLAlchemy makes it possible to use any DB supported by that
    library. Legacy support is provided for sqlite3.Connection objects.
schema : string, optional
    Specify the schema (if database flavor supports this). If None, use
    default schema.
if_exists : {'fail', 'replace', 'append'}, default 'fail'
    How to behave if the table already exists.

    * fail: Raise a ValueError.
    * replace: Drop the table before inserting new values.
    * append: Insert new values to the existing table.
 '''