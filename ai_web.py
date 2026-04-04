import requests


HH_API_URL = "https://api.hh.ru/vacancies"
DEFAULT_PER_PAGE = 7


def format_vacancies(vacancies):
    lines = ["Вот что удалось найти на hh.ru:"]

    for index, vacancy in enumerate(vacancies, start=1):
        employer = vacancy.get("employer", {}).get("name", "Компания не указана")
        title = vacancy.get("name", "Название не указано")
        salary_data = vacancy.get("salary")
        salary_text = ""

        if salary_data:
            salary_from = salary_data.get("from")
            salary_to = salary_data.get("to")
            currency = salary_data.get("currency", "")

            if salary_from and salary_to:
                salary_text = f" Зарплата: {salary_from}-{salary_to} {currency}."
            elif salary_from:
                salary_text = f" Зарплата от {salary_from} {currency}."
            elif salary_to:
                salary_text = f" Зарплата до {salary_to} {currency}."

        lines.append(
            f"{index}. {title}\n"
            f"Компания: {employer}.{salary_text}\n"
            f"Ссылка: {vacancy.get('alternate_url', 'Ссылка недоступна')}"
        )

    return "\n\n".join(lines)


def web_ai(text_ai):
    params = {
        "text": text_ai,
        "per_page": DEFAULT_PER_PAGE,
        "only_with_salary": False,
    }

    headers = {
        "User-Agent": "career-wave-bot/1.0",
        "HH-User-Agent": "career-wave-bot/1.0 (support: local-project)",
    }

    try:
        response = requests.get(HH_API_URL, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return "Не удалось получить вакансии с hh.ru. Попробуй повторить запрос чуть позже."

    vacancies = data.get("items", [])

    if not vacancies:
        return "По этому запросу вакансии не найдены. Попробуй указать профессию, город или уровень опыта, например: Python стажировка Москва."

    return format_vacancies(vacancies)
