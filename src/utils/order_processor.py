from .calculations import get_discount_by_total, calculate_order_total


def load_orders_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f]
        
    except FileNotFoundError as er:
        print("Файл с таким именем не был найден:", er) 


def processed_orders(orders_data):
    result_lst = []
    
    for order in orders_data:
        try:
            num, total_sum, stats, user = order.split(":") 
            total_sum = int(total_sum)
        except ValueError as er:
            print("ошибка обработки заказа:", order, "ошибка:", er)
            continue
        
        discount = get_discount_by_total(total_sum)
        total = calculate_order_total(discount, total_sum)
    
        result_lst.append({
                "order_id": num,
                "total": total, 
                "status": stats, 
                "user": user
        })
    
    return result_lst


def analyze_orders(processed_orders: list[dict]):
    stats = {
        "total_orders": 0,
        "total_sum": 0,
        "by_status": {},
        "unique_users": set()
    }
    for orders in processed_orders:
        stats["total_orders"] += 1
        stats["total_sum"] += orders["total"]
        
        status = orders['status']

        if status not in stats['by_status']:
            stats['by_status'][status] = 0
        stats["by_status"][status] += 1
        
        stats["unique_users"].add(orders["user"])
    return stats


def process_order_file(input_file, output_file):
    res_1 = load_orders_from_file(input_file)
    res_2 = processed_orders(res_1)
    res_3 = analyze_orders(res_2)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Обработано заказов: {res_3['total_orders']}\n")
        f.write(f"Общая сумма: {res_3['total_sum']}\n")
        f.write(f"По статусам: {", ".join(res_3["by_status"])}\n")
        f.write(f"Уникальных пользователей: {len(res_3["unique_users"])}\n")