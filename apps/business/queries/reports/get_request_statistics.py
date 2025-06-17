from django.db import connection

def get_request_statistics():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                COUNT(*) AS total,
                COUNT(*) FILTER (WHERE status = 'aceptado') AS aceptadas,
                COUNT(*) FILTER (WHERE status = 'rechazado') AS rechazadas,
                COUNT(*) FILTER (WHERE status IN ('aceptado', 'rechazado')) AS terminado,
                ROUND(
                    100.0 * COUNT(*) FILTER (WHERE status = 'aceptado') /
                    NULLIF(COUNT(*) FILTER (WHERE status IN ('aceptado', 'rechazado')), 0), 2
                ) AS porcentaje_aceptadas
            FROM database_request
        """)
        return cursor.fetchone()

def get_plan_request_statistics():
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT 
                COUNT(*) AS total,
                COUNT(*) FILTER (WHERE status = 'aceptado') AS aceptadas,
                COUNT(*) FILTER (WHERE status = 'rechazado') AS rechazadas,
                COUNT(*) FILTER (WHERE status IN ('aceptado', 'rechazado', 'terminado')) AS respondidas,
                ROUND(
                    100.0 * COUNT(*) FILTER (WHERE status = 'aceptado') /
                    NULLIF(COUNT(*) FILTER (WHERE status IN ('aceptado', 'rechazado', 'terminado')), 0), 2
                ) AS porcentaje_aceptadas
            FROM database_request
        """)
        plan = cursor.fetchall()
    return [line[0] for line in plan] 