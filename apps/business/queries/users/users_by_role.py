from django.db import connection

def get_users_by_role(role):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, email, name, lastname
            FROM database_user
            WHERE role = %s
        """, [role])
        results = cursor.fetchall()
    return results

def get_plan_users_by_role(role):
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT id, email, name, lastname
            FROM database_user
            WHERE role = %s
        """, [role])
        plan = cursor.fetchall()

    return [line[0] for line in plan] 