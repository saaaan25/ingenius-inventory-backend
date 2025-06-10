from django.db import connection

def get_users_by_role(role):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT auth_user.id, auth_user.email, auth_user.first_name, auth_user.last_name
            FROM auth_user
            INNER JOIN database_collaborator ON auth_user.id = database_collaborator.user_id
            INNER JOIN auth_group ON database_collaborator.role_id = auth_group.id
            WHERE auth_group.name = %s
        """, [role])
        results = cursor.fetchall()
    return results

def get_plan_users_by_role(role):
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT auth_user.id, auth_user.email, auth_user.first_name, auth_user.last_name
            FROM auth_user
            INNER JOIN database_collaborator ON auth_user.id = database_collaborator.user_id
            INNER JOIN auth_group ON database_collaborator.role_id = auth_group.id
            WHERE auth_group.name = %s
        """, [role])
        plan = cursor.fetchall()

    return [line[0] for line in plan] 