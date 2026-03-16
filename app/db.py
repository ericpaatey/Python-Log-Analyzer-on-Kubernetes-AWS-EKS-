import psycopg2
import os

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS")
)

def insert_result(result):

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO log_results(total_logs, errors, warnings) VALUES(%s,%s,%s)",
        (
            result["total_logs"],
            result["errors"],
            result["warnings"]
        )
    )

    conn.commit()