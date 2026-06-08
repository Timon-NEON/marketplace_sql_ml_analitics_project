from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

df = pd.read_csv('../data/processed/retail_clean.csv')

df['invoicedate'] = pd.to_datetime(df['invoicedate'])

df.to_sql(
    'sales',
    engine,
    if_exists='replace',
    index=False
)
