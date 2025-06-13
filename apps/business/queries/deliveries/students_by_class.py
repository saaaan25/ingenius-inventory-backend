from django.db import connection

def get_students_by_class(classroom_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT s.id, s.name, s.lastname
            FROM database_student s
            WHERE s.classroom_id = %s
        """, [classroom_id])
        return cursor.fetchall()

def get_plan_students_by_class(classroom_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT s.id, s.name, s.lastname
            FROM database_student s
            WHERE s.classroom_id = %s
        """, [classroom_id])
        plan = cursor.fetchall()
    return [line[0] for line in plan]