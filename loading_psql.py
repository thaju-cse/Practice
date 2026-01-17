import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text

# -----------------------------
# CONFIGURATION
# -----------------------------
CSV_FILE_PATH = "./input-survey-non-crop.csv"
TABLE_NAME = "dynamic_csv_table"
SCHEMA_NAME = "public"
CHUNK_SIZE = 5000

DB_USER = "postgres"
DB_PASSWORD = "Thaju4@Postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "loading"

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
# engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/loading")
with engine.connect() as conn:
    print("Connection successful")

# -----------------------------
# STEP 1: READ ONLY HEADER
# -----------------------------
df_header = pd.read_csv(CSV_FILE_PATH, nrows=0)
columns = df_header.columns.tolist()

# -----------------------------
# STEP 2: CREATE TABLE DYNAMICALLY
# (All columns as TEXT for safety)
# -----------------------------
create_table_sql = f"""
CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.{TABLE_NAME} (
    {", ".join([f'"{col}" TEXT' for col in columns])}
);
"""
print("Table created successfully..")

with engine.begin() as conn:
    print("Connected successfully")
    conn.execute(text(create_table_sql))

# -----------------------------
# STEP 3: LOAD DATA IN CHUNKS
# -----------------------------
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

print("CSV data loaded successfully.")
