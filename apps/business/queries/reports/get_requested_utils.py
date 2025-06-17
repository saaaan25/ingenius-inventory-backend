from django.db import connection

def get_requested_utils():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                (SELECT SUM(quantity) FROM database_requestdetail) AS total,
                (SELECT SUM(rd.quantity) FROM database_requestdetail rd
                 INNER JOIN database_request r ON rd.request_id = r.id
                 WHERE r.status = 'aceptado') AS aceptados
        """)
        return cursor.fetchone()

def get_plan_requested_utils():
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT 
                (SELECT SUM(quantity) FROM database_requestdetail) AS total,
                (SELECT SUM(rd.quantity) FROM database_requestdetail rd
                 INNER JOIN database_request r ON rd.request_id = r.id
                 WHERE r.status = 'aceptado') AS aceptados
        """)
        plan = cursor.fetchall()
    return [line[0] for line in plan] 