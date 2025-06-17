from django.db import connection

def get_utils_by_teacher(user_id=None):
    with connection.cursor() as cursor:
        base_query = """
            SELECT u.description, SUM(rd.quantity) AS total
            FROM database_request r
            INNER JOIN database_requestdetail rd ON r.id = rd.request_id
            INNER JOIN database_util u ON rd.util_id = u.id
            WHERE r.status = 'aceptado' AND r.request_date < CURRENT_DATE
        """
        params = []
        if user_id:
            base_query += " AND r.user_id = %s"
            params.append(user_id)

        base_query += " GROUP BY u.description"

        cursor.execute(base_query, params)
        return cursor.fetchall()

def get_plan_utils_by_teacher(user_id=None):
    with connection.cursor() as cursor:
        base_query = """
            EXPLAIN ANALYZE
            SELECT u.description, SUM(rd.quantity) AS total
            FROM database_request r
            INNER JOIN database_requestdetail rd ON r.id = rd.request_id
            INNER JOIN database_util u ON rd.util_id = u.id
            WHERE r.status = 'aceptado' AND r.request_date < CURRENT_DATE
        """
        params = []
        if user_id:
            base_query += " AND r.user_id = %s"
            params.append(user_id)

        base_query += " GROUP BY u.description"

        cursor.execute(base_query, params)
        plan = cursor.fetchall()
    return [line[0] for line in plan] 