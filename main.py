
# 3 ЛР Общая часть
# 1 часть делала с Рощиной

# import os
# from sympy import *
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# SESSION_SECRET = os.environ['SESSION_SECRET']
# print(SESSION_SECRET)

# POLI = os.environ['POLI']
# print(POLI)

# # 2 часть делала с Мамедовой
# # Индивидуальный вариант 2
# k, T, C, L = symbols('k C T L')

# # 1 способ
# C_ost = 90000
# Am_lst = []
# C_ost_lst = []
# for i in range(9):
#     Am = (C - L) / T
#     C_ost -= Am.subs({C: 90000, T: 9, L: 0})
#     Am_lst.append(round(Am.subs({C: 90000, T: 9, L: 0}), 2))
#     C_ost_lst.append(round(C_ost, 2)) # что это? Эта строка добавляет новое значение в конец списка C_ost_lst, предварительно округляя его до 2 знаков после запятой.
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# # 2 способ 
# Aj = 0
# C_ost = 90000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(9):
#     Am = 2 * 1/9 * (90000 - Aj)  # k=2, T=6
#     Am = round(Am, 2)
#     C_ost -= Am
#     C_ost = round(C_ost, 2)
#     Am_lst_2.append(Am)
#     C_ost_lst_2.append(C_ost)
#     Aj += Am
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# # Табличный вывод
# Y = range(1, 10)  
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# # Визуализация
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt.savefig('chart13.png')
# plt.figure()
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')
# plt.savefig('chart14.png')

# # Первая круговая диаграмма
# vals = Am_lst
# labels = [str(x) for x in range(1, 10)]  
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True,
#        explode=explode, wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"},
#        rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart15.png')

# # Вторая круговая диаграмма 
# vals = Am_lst_2
# labels = [str(x) for x in range(1, 10)]  
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True,
#        explode=explode, wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"},
#        rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart16.png')
# plt.figure()

# # Столбчатые диаграммы
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2)) #что это? Эта строка объединяет три списка в один список кортежей 
# tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig('chart17.jpeg')
# plt.figure()
# plt.bar(tfame['Y'], tfame2['Am_lst_2'])
# plt.savefig('chart18.png')
# plt.figure() # что это? это настройки отображения диаграммы, которые включают в себя ширину линии (lw), стиль линии (ls) и цвет линии (edgecolor), а также поворот меток (rotatelabels)
# Выполнено корректно, ставлю 5/5

# Задание 3
# Восстановлен после удаления контейнер визуализации расчетов

# Задание 4
# Выполняла с Мамедовой
# строка 264
import pandas as pd
import matplotlib.pyplot as plt

# Исходные данные: список анализируемых cookies с их атрибутами
cookies = [
    {
        "name": "session_id", "secure": False, "httponly": False,
        "samesite": None, "domain": ".example.com",
        "max_age": None, "host_prefix": False,
    },
    {
        "name": "user_token", "secure": True, "httponly": True,
        "samesite": "Strict", "domain": "app.example.com",
        "max_age": 60 * 60 * 24 * 365, "host_prefix": False,
    },
    {
        "name": "tracking_id", "secure": False, "httponly": False,
        "samesite": "None", "domain": ".example.com",
        "max_age": None, "host_prefix": False,
    },
    {
        "name": "__Host-csrf", "secure": True, "httponly": True,
        "samesite": "Strict", "domain": "app.example.com",
        "max_age": 3600, "host_prefix": True,
    },
]


def add_threat(threats, cookie, category, threat, level, recommendation):
    """Вспомогательная функция: добавляет запись об угрозе в общий список"""
    threats.append({
        "Cookie": cookie["name"],
        "Категория": category,
        "Угроза": threat,
        "Уровень": level,
    })


def analyze_cookie(cookie):
    """Анализирует одну cookie на наличие уязвимостей безопасности"""
    threats = []

    # Проверка 1: отсутствие флага Secure -> риск перехвата при передаче по HTTP
    if not cookie["secure"]:
        add_threat(threats, cookie, "Перехват",
                   "Cookie может быть перехвачена при передаче по HTTP",
                   "Критический", "Добавить флаг Secure")

    # Проверка 2: неправильный SameSite -> риск CSRF-атак
    if cookie["samesite"] is None or cookie["samesite"] == "None":
        add_threat(threats, cookie, "Перехват",
                   "Cookie может передаваться при межсайтовых запросах",
                   "Высокий", "Использовать SameSite=Lax или Strict")

    # Проверка 3: отсутствие HttpOnly -> риск кражи через XSS
    if not cookie["httponly"]:
        add_threat(threats, cookie, "Доступ",
                   "Cookie доступна через JavaScript при XSS-атаке",
                   "Критический", "Добавить флаг HttpOnly")

    # Проверка 4: domain начинается с точки -> доступ для всех поддоменов
    if cookie["domain"].startswith("."):
        add_threat(threats, cookie, "Доступ",
                   "Cookie доступна всем поддоменам",
                   "Средний", "Указать точный домен без точки в начале")

    # Проверка 5: отсутствие префикса __Host- -> недостаточная защита
    if not cookie["host_prefix"]:
        add_threat(threats, cookie, "Изменение",
                   "Cookie не использует защитный префикс __Host-",
                   "Высокий", "Использовать имя cookie с префиксом __Host-")

    # Проверка 6: отсутствие и Secure, и HttpOnly -> риск MitM-атак
    if not cookie["secure"] and not cookie["httponly"]:
        add_threat(threats, cookie, "Изменение",
                   "Cookie можно подменить через Man-in-the-Middle",
                   "Критический", "Добавить Secure и HttpOnly")

    # Проверка 7: срок жизни cookie (бесконечный или слишком долгий)
    month = 60 * 60 * 24 * 30
    if cookie["max_age"] is None:
        add_threat(threats, cookie, "Изменение",
                   "Cookie не имеет заданного срока жизни",
                   "Средний", "Установить max_age или expires")
    elif cookie["max_age"] > month:
        add_threat(threats, cookie, "Изменение",
                   "Cookie хранится слишком долго",
                   "Средний", "Сократить срок хранения cookie")

    return threats

def analyze_all_cookies(cookies_list):
    """Анализирует все cookies и формирует итоговую таблицу в формате pandas DataFrame"""
    all_threats = []
    # Последовательно анализируем каждую cookie
    for cookie in cookies_list:
        all_threats.extend(analyze_cookie(cookie))
    # Создаем DataFrame из собранных угроз
    df = pd.DataFrame(all_threats)
    # Настраиваем сортировку по уровню опасности (от критических к низким)
    levels = ["Критический", "Высокий", "Средний", "Низкий"]
    df["Уровень"] = pd.Categorical(df["Уровень"], categories=levels, ordered=True)
    df = df.sort_values(["Уровень", "Категория"]).reset_index(drop=True)
    # Добавляем нумерацию строк (начиная с 1)
    df.index += 1
    df.index.name = "№"
    return df
def show_summary(df):
    """Подсчитывает количество угроз по категориям и выводит статистику в консоль"""
    counts = df["Категория"].value_counts()
    print("\nКоличество угроз по категориям:")
    print(f"Перехват:  {counts.get('Перехват', 0)}")
    print(f"Доступ:    {counts.get('Доступ', 0)}")
    print(f"Изменение: {counts.get('Изменение', 0)}")
    return counts
def build_charts(counts):
    """Строит и сохраняет две визуализации: круговую диаграмму и гистограмму"""
    colors = ["#ff6b6b", "#ffd166", "#4dabf7"]
    # 1. Круговая диаграмма (показывает процентное соотношение угроз)
    plt.figure(figsize=(7, 6))
    plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%", colors=colors)
    plt.title("Круговая диаграмма угроз")
    plt.tight_layout()
    plt.savefig("cookie_threats_pie.png", dpi=150)
    plt.close()  # Закрываем фигуру, чтобы не накладывать графики
    # 2. Гистограмма (показывает абсолютное количество угроз каждого типа)
    plt.figure(figsize=(7, 6))
    plt.bar(counts.index, counts.values, color=colors)
    plt.title("Гистограмма угроз")
    plt.xlabel("Категория угрозы")
    plt.ylabel("Количество")
    plt.tight_layout()
    plt.savefig("cookie_threats_histogram.png", dpi=150)
    plt.close()
def main():
    """Главная функция: запускает анализ, выводит результаты и сохраняет файлы"""
    # Шаг 1: Анализ всех cookies и создание таблицы угроз
    df = analyze_all_cookies(cookies)
    # Шаг 2: Вывод таблицы в консоль
    print("\nТаблица найденных угроз:")
    print(df.to_string())
    # Шаг 3: Сохранение таблицы в CSV-файл (с поддержкой русских символов)
    df.to_csv("cookie_threats_report.csv", encoding="utf-8-sig")
    # Шаг 4: Подсчет статистики и вывод в консоль
    counts = show_summary(df)
    # Шаг 5: Построение и сохранение графиков
    build_charts(counts)
    # Шаг 6: Информирование пользователя о сохраненных файлах
    print("\nФайлы сохранены:")
    print("cookie_threats_report.csv — таблица угроз")
    print("cookie_threats_pie.png — круговая диаграмма")
    print("cookie_threats_histogram.png — гистограмма")
# Точка входа в программу
if __name__ == "__main__":
    main()


# Описание функций:

# 1. add_threat() — добавляет найденную угрозу в список угроз.
# 2. analyze_cookie() — проверяет одну cookie на перехват, доступ и изменение.
# 3. analyze_all_cookies() — проверяет все cookies и создаёт pandas DataFrame.
# 4. show_summary() — выводит количество угроз по категориям.
# 5. build_charts() — строит круговую диаграмму и гистограмму в отдельных PNG-файлах.
# 6. main() — запускает программу, сохраняет CSV-отчёт и PNG-графики.
# '''

