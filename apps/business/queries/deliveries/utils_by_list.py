from django.db import connection

def get_utils_by_list(utils_list_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT u.description, ld.quantity
            FROM database_listdetail ld
            INNER JOIN database_util u ON ld.util_id = u.id
            WHERE ld.utils_list_id = %s
        """, [utils_list_id])
        return cursor.fetchall()

def get_plan_utils_by_list(utils_list_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT u.description, ld.quantity
            FROM database_listdetail ld
            INNER JOIN database_util u ON ld.util_id = u.id
            WHERE ld.utils_list_id = %s
        """, [utils_list_id])
        plan = cursor.fetchall()
    return [line[0] for line in plan]