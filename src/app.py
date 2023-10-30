import os
import pandas as pd
from dotenv import load_dotenv
import psycopg2 as ps


# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
con = ps.connect(connection_string)

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
con = ps.connect(connection_string)
cursor = con.cursor()
con.commit()
con.close()

# 4) Use pandas to print one of the tables as dataframes using read_sql function
result_dataFrame = pd.read_sql("""Select * from BOOKS B
JOIN BOOK_AUTHORS BA ON B.BOOK_ID = BA.BOOK_ID
;""", con)
print(result_dataFrame)