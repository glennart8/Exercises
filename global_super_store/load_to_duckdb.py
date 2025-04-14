import duckdb
import pandas as pd

# Ladda CSV-filen
df = pd.read_csv("global_superstore2.csv", encoding='latin1')

# Koppla till DuckDB (skapar fil om den inte finns)
con = duckdb.connect("superstore.duckdb")

# Spara tabellen
con.execute("DROP TABLE IF EXISTS raw_orders")
con.execute("CREATE TABLE raw_orders AS SELECT * FROM df")


