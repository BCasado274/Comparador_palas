from db import get_connection
from models import Pala

def get_all_palas() -> list[Pala]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM palas")
    rows = cursor.fetchall()
    conn.close()

    return [Pala(**dict(row)) for row in rows]
