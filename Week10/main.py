import sqlite3
from contextlib import closing

db_path="sqlite3.db"

try:
    with closing(sqlite3.connect(db_path)) as db_con:
        db_con.row_factory = sqlite3.Row #Enable dictionary-like row access
        with closing(db_con.cursor()) as cursor:
        try:
            query_1 = "SELECT * FROM demo WHERE id > 14"
            cursor.execute(query_1)
            rows = cursor.fetchall()
            print("Name of rows with id > 14:")
            for row in rows:
                print(row['name'])
            except Exception as e:
                print(f"Error exculting query 1: {e}")    
            # Delete Row based on User input
            try:
                del_row = int (input("Enter the row ID threshold for delete: "))
                query_2 = "DELETE FROM demo WHERE id < 3"
                cursor.execute(query_2)
                num_rows = cursor.rowcount
                print(f"{num_rows} rows affected. Are you sure you want to countinue?")
                db_con.commit()
            except Exception as e:
                print(f"Error exculting query 2: {e}")

except sqlite3.Error as e:
    print()
    print("--")        