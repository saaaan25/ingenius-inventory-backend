from django.db import connection

def get_requests_by_status(status):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                DATE(request_date) AS day,
                id, user_id, classroom_id, justification, status, request_date
            FROM database_request
            WHERE status = %s
            ORDER BY request_date DESC
        """, [status])
        return cursor.fetchall()
    
def get_plan_requests_by_status(status):
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT 
                DATE(request_date) AS day,
                id, user_id, classroom_id, justification, status, request_date
            FROM database_request
            WHERE status = %s
            ORDER BY request_date DESC
        """, [status])
        plan = cursor.fetchall()
    return [line[0] for line in plan] 