def calculate_success_probability(deal_history, current_result):
    # Рассчитываем количество успешных сделок
    successful_deals = sum(1 for deal in deal_history if deal > 0)

    # Рассчитываем общее количество сделок
    total_deals = len(deal_history)

    # Рассчитываем вероятность успешной сделки на основе истории
    if total_deals > 0:
        success_rate = successful_deals / total_deals
    else:
        success_rate = 0

    # Рассчитываем вероятность текущей успешной сделки
    current_success_rate = 0
    if current_result > 0:
        current_success_rate = success_rate
    else:
        current_success_rate = 1 - success_rate

    # Вычисляем чистый доход (убыток) инвестора
    net_income = sum(deal_history) + current_result

    # Вычисляем ROI (возврат на инвестиции) в процентах
    capital = 1000
    roi = (net_income / capital) * 100

    # Возвращаем вероятность текущей успешной сделки и другие результаты
    return {
        "current_success": current_success_rate,
        "net_income": net_income,
        "ROI_percentage": roi
    }


# Пример использования функции с данными из задачи
deal_success = [-107, -521, -107, -126, 352, -58, 221, 193, -38, 454, -12, -211, 129, 85, 342]
last_deal_result = -250  # Замени на желаемый результат последней сделки

results = calculate_success_probability(deal_success, last_deal_result)
print("Вероятность текущей успешной сделки:", results["current_success"])
print("Чистый доход (убыток) инвестора:", results["net_income"])
print("ROI (возврат на инвестиции), %:", results["ROI_percentage"])