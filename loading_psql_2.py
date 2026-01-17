import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text

# -----------------------------
# CONFIGURATION
# -----------------------------
CSV_FILE_PATH = "./tehsil-level-agcensus-crop.csv"
TABLE_NAME = "tehsil_csv"
SCHEMA_NAME = "public"
CHUNK_SIZE = 5000

DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "loading"

# -----------------------------
# DATABASE CONNECTION
# -----------------------------

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
print("Engine Created Successfully..")

# engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/loading")
try:
    with engine.connect() as conn:
        print("Connection successful")
except:
    print("Something went wrong with connection, Rectify it.")
    break

# -----------------------------
# STEP 1: READ ONLY HEADER
# -----------------------------
try:
    df_header = pd.read_csv(CSV_FILE_PATH, nrows=0)
    columns = df_header.columns.tolist()
    print("Read the table header from csv file.")
except:
    print("There is a problem with reading header.")
    break


# -----------------------------
# STEP 2: CREATE TABLE DYNAMICALLY
# (All columns as TEXT for safety)
# -----------------------------
try:
    create_table_sql = f"""CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.{TABLE_NAME}
                            ({", ".join([f'"{col}" TEXT' for col in columns])});
                            """
    print("Data type of every column is fixed as text as default.")
    print("Table created successfully..")
    
except:
    print("There is a problem in creating table..")
    break

with engine.begin() as conn:
    print("Connected successfully")
    conn.execute(text(create_table_sql))

# -----------------------------
# STEP 3: LOAD DATA IN CHUNKS
# -----------------------------
try:
    c = 0
    for chunk in pd.read_csv(CSV_FILE_PATH, chunksize=CHUNK_SIZE):
        print("Loading.....")
        chunk.to_sql(
                name=TABLE_NAME,
                con=engine,
                schema=SCHEMA_NAME,
                if_exists="append",
                index=False,
                method="multi"
        )
        c+=1

except:
    print("Something went wrong while uploading after ", c*5000, "rows approximately..")
    break

print("CSV data loaded successfully, with total rows ", c * 5000, "Approximately.")
