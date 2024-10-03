from typing import List, Tuple

# Функція для валідації даних
def validate_data(lawyers: List[List[float]], weights: List[float]) -> None:
    assert all(len(lawyer) == len(weights) for lawyer in lawyers), "Кількість критеріїв у адвокатів повинна збігатися з кількістю вагових коефіцієнтів"
    assert len(lawyers) > 0, "Список адвокатів не може бути порожнім"
    assert len(weights) > 0, "Список вагових коефіцієнтів не може бути порожнім"
    assert all(max(col) != min(col) for col in zip(*lawyers)), "Не можна нормалізувати критерії з однаковими мінімальними та максимальними значеннями"

# Функція для знаходження мінімальних і максимальних значень по критеріях
def find_min_max(lawyers: List[List[float]]) -> Tuple[List[float], List[float]]:
    mins = [min(col) for col in zip(*lawyers)]
    maxs = [max(col) for col in zip(*lawyers)]
    return mins, maxs

# Функція для нормалізації оцінок
def normalize_lawyers(lawyers: List[List[float]], mins: List[float], maxs: List[float]) -> List[List[float]]:
    normalized_lawyers = []
    for lawyer in lawyers:
        normalized_lawyer = [(x - min_val) / (max_val - min_val) if max_val != min_val else 0 for x, min_val, max_val in zip(lawyer, mins, maxs)]
        normalized_lawyers.append(normalized_lawyer)
    return normalized_lawyers

# Спеціальна нормалізація для другого критерію (стовпець 1)
def special_normalization(normalized_lawyers: List[List[float]], lawyers: List[List[float]], maxs: List[float], mins: List[float]) -> None:
    for i in range(len(lawyers)):
        normalized_lawyers[i][1] = (maxs[1] - lawyers[i][1]) / (maxs[1] - mins[1])

# Функція для обчислення загальної оцінки для кожного адвоката
def calculate_total_scores(normalized_lawyers: List[List[float]], weights: List[float]) -> List[float]:
    return [sum(value * weight for value, weight in zip(lawyer, weights)) for lawyer in normalized_lawyers]

# Функція для вибору найкращого адвоката
def select_best_lawyer(total_scores: List[float], candidates_names: List[str]) -> Tuple[str, float]:
    best_index = total_scores.index(max(total_scores))
    return candidates_names[best_index], total_scores[best_index]

# Основна функція
def main() -> None:
    # Дані адвокатів і ваги критеріїв
    lawyers = [
        [85, 30, 22, 0.65, 6],
        [60, 20, 10, 0.6, 7],
        [30, 12, 5, 0.45, 5],
        [75, 24, 13, 0.7, 8],
        [40, 15, 7, 0.55, 7]
    ]
    weights = [7, 5, 6, 8, 6]
    candidates_names = ['A1', 'A2', 'A3', 'A4', 'A5']

    # Валідація даних
    validate_data(lawyers, weights)

    # Знаходження мінімальних і максимальних значень
    mins, maxs = find_min_max(lawyers)

    # Нормалізація оцінок
    normalized_lawyers = normalize_lawyers(lawyers, mins, maxs)

    # Спеціальна нормалізація для другого критерію
    special_normalization(normalized_lawyers, lawyers, maxs, mins)

    # Обчислення загальної оцінки
    total_scores = calculate_total_scores(normalized_lawyers, weights)

    # Визначення найкращого адвоката
    best_lawyer, best_score = select_best_lawyer(total_scores, candidates_names)

    # Виведення результату
    print(f"Найкращий адвокат: {best_lawyer}")
    print(f"Загальна оцінка: {best_score}")

if __name__ == "__main__":
    main()
