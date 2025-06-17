from django.db import connection

def get_general_statistics():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                (SELECT COALESCE(SUM(quantity), 0) FROM database_util) AS total_utiles_disponibles,
                (SELECT COALESCE(SUM(amount), 0) FROM database_moneydelivery) 
                - 
                (SELECT COALESCE(SUM(total_spent), 0) FROM database_purchase) AS dinero_disponible;
        """)
        return cursor.fetchone()

def get_plan_general_statistics():
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT 
                (SELECT COALESCE(SUM(quantity), 0) FROM database_util) AS total_utiles_disponibles,
                (SELECT COALESCE(SUM(amount), 0) FROM database_moneydelivery) 
                - 
                (SELECT COALESCE(SUM(total_spent), 0) FROM database_purchase) AS dinero_disponible;
        """)
        plan = cursor.fetchall()
    return [line[0] for line in plan]
