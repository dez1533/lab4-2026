import re
from collections import Counter
import os

# --- 1. Базові операції з рядками ---
def find_substring(text, substring):
    """Пошук підрядка в тексті."""
    return text.find(substring)

def replace_substring(text, old, new):
    """Заміна підрядка в тексті."""
    return text.replace(old, new)

def split_text(text, delimiter=' '):
    """Розділення тексту за роздільником."""
    return text.split(delimiter)

def format_string_f(name, age):
    """Форматування рядка з використанням f-string."""
    return f"Мене звати {name} і мені {age} років."

def format_string_method(name, age):
    """Форматування рядка з використанням методу .format()."""
    return "Мене звати {} і мені {} років.".format(name, age)

# --- 2. Регулярні вирази (Загальні) ---
def extract_emails(text):
    """Витяг email адрес з тексту."""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)

def validate_phone_number(number):
    """Валідація телефонного номера."""
    pattern = r'^\+?3?8?(0\d{9})$'
    return bool(re.match(pattern, number))

# --- Варіант 8: Регулярні вирази та аналіз ---
def extract_ai_teachers(text):
    """Вилучення назв ШІ-вчителів (наприклад, EduAI-2000)."""
    pattern = r'\b[A-Za-z]+AI-\d+\b'
    return re.findall(pattern, text)

def analyze_resume(text):
    """Аналіз резюме: витяг контактної інформації, навичок, досвіду роботи."""
    emails = extract_emails(text)
    phones = re.findall(r'\+?3?8?0\d{9}', text)
    
    # Пошук навичок (після слова "Навички:")
    skills_match = re.search(r'Навички:\s*(.*?)(?:\n|$|\.)', text, re.IGNORECASE)
    skills = skills_match.group(1).split(', ') if skills_match else []
    
    # Пошук досвіду роботи (наприклад, "Досвід роботи: 5 років")
    experience_match = re.search(r'Досвід роботи:\s*(\d+\s*років|\d+\s*роки|\d+\s*рік)', text, re.IGNORECASE)
    experience = experience_match.group(1) if experience_match else "Не вказано"
    
    return {
        'emails': emails,
        'phones': phones,
        'skills': skills,
        'experience': experience
    }

# --- 3. Обробка текстових даних ---
def count_words(text):
    """Підрахунок кількості слів у тексті."""
    return len(re.findall(r'\w+', text))

def count_sentences(text):
    """Підрахунок кількості речень у тексті."""
    return len(re.findall(r'[.!?]+', text))

def word_frequency(text):
    """Підрахунок частоти слів у тексті."""
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

def analyze_text_file(filepath):
    """Аналіз текстового файлу з папки data."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            
        word_count = count_words(text)
        sentence_count = count_sentences(text)
        freq = word_frequency(text)
        ai_teachers = extract_ai_teachers(text)
        
        return {
            'word_count': word_count,
            'sentence_count': sentence_count,
            'word_frequency': freq.most_common(5),
            'ai_teachers': ai_teachers
        }
    except FileNotFoundError:
        return None

def format_file_analysis_results(results):
    if not results:
        return "Файл не знайдено! Переконайтеся, що файл neoterra_text.txt лежить у папці data."
        
    output = "Результати аналізу файлу:\n\n"
    output += f"Кількість слів: {results['word_count']}\n"
    output += f"Кількість речень: {results['sentence_count']}\n\n"
    output += "Топ-5 найчастіших слів:\n"
    for word, count in results['word_frequency']:
        output += f"  {word}: {count}\n"
    output += f"\nЗнайдені ШІ-вчителі: {', '.join(results['ai_teachers'])}\n"
    return output

# --- Головна функція ---
def main():
    print("Ласкаво просимо до аналізатора (Варіант 8)!")
    while True:
        try:
            choice = input("\nОберіть опцію:\n1. Аналіз файлу neoterra_text.txt\n2. Аналіз резюме\n3. Вихід\nВаш вибір: ")
            
            if choice == '1':
                base_dir = os.path.dirname(os.path.abspath(__file__))
                filepath = os.path.join(base_dir, 'data', 'neoterra_text.txt')
                
                results = analyze_text_file(filepath)
                print(format_file_analysis_results(results))
                
            elif choice == '2':
                print("Введіть текст резюме (наприклад: 'Email: test@gmail.com. Телефон: 0981112233. Навички: C++, Python, C#. Досвід роботи: 2 роки.'): ")
                text = input()
                res = analyze_resume(text)
                print("\nРезультати аналізу резюме:")
                print(f"Email: {', '.join(res['emails']) if res['emails'] else 'Немає'}")
                print(f"Телефони: {', '.join(res['phones']) if res['phones'] else 'Немає'}")
                print(f"Навички: {', '.join(res['skills']) if res['skills'] else 'Не вказано'}")
                print(f"Досвід роботи: {res['experience']}")
                
            elif choice == '3':
                print("Дякуємо за використання програми!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")
        except Exception as e:
            print(f"Виникла помилка: {e}")

if __name__ == '__main__':
    main()