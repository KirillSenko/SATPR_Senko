from typing import List, Tuple

# Функція для перевірки валідності даних
def validate_data(candidates: List[List[int]], weights: List[int]) -> None:
    assert all(len(candidate) == len(weights) for candidate in candidates), "Кількість критеріїв у кандидатів повинна збігатися з кількістю вагових коефіцієнтів"
    assert len(candidates) > 0, "Список кандидатів не може бути порожнім"
    assert len(weights) > 0, "Список вагових коефіцієнтів не може бути порожнім"

# Функція для обчислення загальної оцінки для кожного кандидата
def calculate_total_scores(candidates: List[List[int]], weights: List[int]) -> List[float]:
    return [sum(score * weight for score, weight in zip(candidate, weights)) for candidate in candidates]

# Функція для вибору найкращого кандидата
def select_best_candidate(candidates_scores: List[float], candidates_names: List[str]) -> Tuple[str, float]:
    best_index = candidates_scores.index(max(candidates_scores))
    return candidates_names[best_index], candidates_scores[best_index]

# Основна функція
def main() -> None:
    # Дані кандидатів і ваги критеріїв
    candidates = [
        [3, 7, 2, 9],
        [8, 3, 6, 7],
        [4, 8, 3, 5],
        [9, 6, 5, 4]
    ]
    weights = [8, 9, 6, 7]
    candidates_names = ['A1', 'A2', 'A3', 'A4']

    # Валідація даних
    validate_data(candidates, weights)

    # Обчислення загальних оцінок
    total_scores = calculate_total_scores(candidates, weights)

    # Вибір найкращого кандидата
    best_candidate, best_score = select_best_candidate(total_scores, candidates_names)

    # Виведення результату
    print(f"Найкращий кандидат: {best_candidate}")
    print(f"Загальна оцінка: {best_score}")

if __name__ == "__main__":
    main()
