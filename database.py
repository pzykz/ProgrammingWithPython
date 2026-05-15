import os
from sqlalchemy import create_engine, text


def create_db_engine():
    """
    Constructs a SQLAlchemy engine using environment variables.
    This prevents sensitive credentials from being committed to version control.
    """
    # In a real scenario, these variables would be loaded from a .env file
    # that is safely ignored by your .gitignore
    db_user = os.environ.get("DB_USER", "default_user")
    db_pass = os.environ.get("DB_PASS", "default_pass")
    db_host = os.environ.get("DB_HOST", "localhost")
    db_name = os.environ.get("DB_NAME", "analytics_db")

    # Define the connection string (PostgreSQL example)
    connection_uri = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"

    # Initialize the engine
    engine = create_engine(connection_uri)
    return engine


if __name__ == "__main__":
    print("Database engine initialized.")
    # test_engine = create_db_engine()
