from django.db import connection

def get_utils_by_purchase(purchase_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT u.description, pd.unit_price, pd.quantity
            FROM database_purchasedetail pd
            INNER JOIN database_util u ON pd.util_id = u.id
            WHERE pd.purchase_id = %s
        """, [purchase_id])
        return cursor.fetchall()

def get_plan_utils_by_purchase(purchase_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT u.description, pd.unit_price, pd.quantity
            FROM database_purchasedetail pd
            INNER JOIN database_util u ON pd.util_id = u.id
            WHERE pd.purchase_id = %s
        """, [purchase_id])
        plan = cursor.fetchall()
    return [line[0] for line in plan]