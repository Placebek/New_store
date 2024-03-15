import re

def validate_login(login):
    return 3 <= len(login) <= 30

def validate_password(password):
    # Минимальная длина 6 символов, максимальная 30
    # Должен содержать хотя бы одну букву в верхнем и нижнем регистре,
    # хотя бы одну цифру и один специальный символ
    return 6 <= len(password) <= 30 and \
           re.search(r"[a-z]", password) and \
           re.search(r"[A-Z]", password) and \
           re.search(r"\d", password) and \
           re.search(r"[!@#$%^&*()-+=.,]", password)

def validate_name(first_name):
    return 2 <= len(first_name) <= 30 and \
           re.search(r"[a-z]", first_name) and \
           re.search(r"[A-Z]", first_name)