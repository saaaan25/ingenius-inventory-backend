from django.db import connection

def get_deliveries_by_student(student_id):
    deliveries = []

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT d.id, ud.delivery_date, u.description, udd.quantity, udd.status
            FROM database_delivery d
            INNER JOIN database_utilsdelivery ud ON ud.delivery_id = d.id
            INNER JOIN database_utilsdeliverydetail udd ON ud.id = udd.utils_delivery_id
            INNER JOIN database_util u ON udd.util_id = u.id
            WHERE d.student_id = %s
            ORDER BY ud.delivery_date
        """, [student_id])
        rows = cursor.fetchall()

    utils_by_delivery = {}
    for delivery_id, delivery_date, description, quantity, status in rows:
        if delivery_id not in utils_by_delivery:
            utils_by_delivery[delivery_id] = {
                "type": "materials",
                "delivery_id": delivery_id,
                "date": delivery_date,
                "items": []
            }
        utils_by_delivery[delivery_id]["items"].append({
            "util": description,
            "quantity": quantity,
            "status": status
        })
    deliveries.extend(utils_by_delivery.values())

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT d.id, md.amount, md.delivery_date
            FROM database_delivery d
            INNER JOIN database_moneydelivery md ON md.delivery_id = d.id
            WHERE d.student_id = %s
            ORDER BY md.delivery_date
        """, [student_id])
        rows = cursor.fetchall()

    for delivery_id, amount, delivery_date in rows:
        deliveries.append({
            "type": "money",
            "delivery_id": delivery_id,
            "date": delivery_date,
            "amount": amount
        })

    return deliveries

def get_plan_deliveries_by_student(student_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT ud.id, ud.delivery_date, u.description, udd.quantity, udd.status
            FROM database_utilsdelivery ud
            INNER JOIN database_utilsdeliverydetail udd ON ud.id = udd.utils_delivery_id
            INNER JOIN database_util u ON udd.util_id = u.id
            INNER JOIN database_delivery d ON ud.delivery_id = d.id
            WHERE d.student_id = %s
        """, [student_id])
        plan_materials = cursor.fetchall()

    with connection.cursor() as cursor:
        cursor.execute("""
            EXPLAIN ANALYZE
            SELECT SUM(md.amount)
            FROM database_moneydelivery md
            INNER JOIN database_delivery d ON md.delivery_id = d.id
            WHERE d.student_id = %s
        """, [student_id])
        plan_money = cursor.fetchall()

    return {
        "materials_plan": [line[0] for line in plan_materials],
        "money_plan": [line[0] for line in plan_money]
    }
