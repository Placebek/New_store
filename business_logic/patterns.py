import re

def validate_login(email):
    return 3 <= len(email) <= 100

def validate_password(password):
    # Минимальная длина 6 символов, максимальная 30
    # Должен содержать хотя бы одну букву в верхнем и нижнем регистре,
    # хотя бы одну цифру и один специальный символ
    return 6 <= len(password) <= 30 and \
           re.search(r"[a-z]", password) and \
           re.search(r"[A-Z]", password) and \
           re.search(r"\d", password) and \
           re.search(r"[!@#$%^&*()-+=.,]", password)

def validate_phone_number(number):
    # Паттерн для проверки казахстанских номеров телефона
    pattern = re.compile(r"^\+7\d{10}$")
    return pattern.match(number) is not None