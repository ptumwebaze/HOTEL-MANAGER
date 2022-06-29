import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("C:\\Users\\OSBERT\\Desktop\\kkkkkkkk.sqlite")
df = pd.read_mql_query("SELECT * from surveys", con)

# Verify that result of SQL query is stored in the dataframe
print(df.head())

con.close()
