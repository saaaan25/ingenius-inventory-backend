from django.db import connection

def get_utils_by_request(request_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT u.description, rd.quantity
            FROM database_requestdetail rd
            INNER JOIN database_util u ON rd.util_id = u.id
            WHERE rd.request_id = %s
        """, [request_id])
        return cursor.fetchall()

def get_plan_utils_by_request(request_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT u.description, rd.quantity
            FROM database_requestdetail rd
            INNER JOIN database_util u ON rd.util_id = u.id
            WHERE rd.request_id = %s
        """, [request_id])
        plan = cursor.fetchall()
    return [line[0] for line in plan] 