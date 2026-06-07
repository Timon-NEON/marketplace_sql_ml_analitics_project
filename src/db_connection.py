from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        if result.scalar() == 1:
            print("Connected to the database")
        else:
            print("Connection to the database is not successful:", result.scalar())
except:
    print("Connection to the database is not successful")