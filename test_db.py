from sqlalchemy import create_engine
from app.core.config import DATABASE_URL

print("Database URL:", DATABASE_URL)

try:
    engine = create_engine(DATABASE_URL)

    with engine.connect() as conn:
        print("DB Connected Successfully")

except Exception as e:
    print("Connection Failed")
    print(e)