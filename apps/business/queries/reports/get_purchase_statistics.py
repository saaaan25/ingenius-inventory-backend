from django.db import connection

def get_purchase_statistics():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                COUNT(*) AS total_compras,
                SUM(pd.quantity) AS utiles_comprados,
                SUM(p.total_spent) AS total_gastado
            FROM database_purchase p
            INNER JOIN database_purchasedetail pd ON p.id = pd.purchase_id
        """)
        return cursor.fetchone()

def get_plan_purchase_statistics():
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT 
                COUNT(*) AS total_compras,
                SUM(pd.quantity) AS utiles_comprados,
                SUM(p.total_spent) AS total_gastado
            FROM database_purchase p
            INNER JOIN database_purchasedetail pd ON p.id = pd.purchase_id
        """)
        plan = cursor.fetchall()
    return [line[0] for line in plan] 