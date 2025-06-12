from django.db import connection

def get_purchases_ordered_by_date():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.id, p.purchase_date, u.first_name, u.last_name, p.total_spent
            FROM database_purchase p
            INNER JOIN auth_user u ON p.user_id = u.id
            ORDER BY p.purchase_date DESC
        """)
        return cursor.fetchall()

def get_plan_purchases_ordered_by_date():
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT p.id, p.purchase_date, u.first_name, u.last_name, p.total_spent
            FROM database_purchase p
            INNER JOIN auth_user u ON p.user_id = u.id
            ORDER BY p.purchase_date DESC
        """)
        plan = cursor.fetchall()
    return [line[0] for line in plan] 