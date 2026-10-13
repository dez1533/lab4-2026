import unittest
import sys
import os

# Додаємо шлях до папки src, щоб можна було імпортувати lab4
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lab4 import (
    find_substring, replace_substring, split_text, 
    format_string_f, format_string_method, 
    extract_emails, validate_phone_number, 
    extract_ai_teachers, count_words, count_sentences,
    analyze_resume
)

class TestLab4(unittest.TestCase):
    def test_find_substring(self):
        self.assertEqual(find_substring("Hello, world!", "world"), 7)

    def test_replace_substring(self):
        self.assertEqual(replace_substring("Hello, world!", "world", "Python"), "Hello, Python!")

    def test_split_text(self):
        self.assertEqual(split_text("Hello, world!", ", "), ["Hello", "world!"])

    def test_format_string_f(self):
        self.assertEqual(format_string_f("Максим", 19), "Мене звати Максим і мені 19 років.")

    def test_format_string_method(self):
        self.assertEqual(format_string_method("Максим", 19), "Мене звати Максим і мені 19 років.")

    def test_extract_emails(self):
        self.assertEqual(
            extract_emails("Contact us at info@example.com or support@test.com"),
            ["info@example.com", "support@test.com"]
        )

    def test_validate_phone_number(self):
        self.assertTrue(validate_phone_number("+380981234567"))
        self.assertTrue(validate_phone_number("0981234567"))
        self.assertFalse(validate_phone_number("12345"))

    def test_extract_ai_teachers(self):
        self.assertEqual(
            extract_ai_teachers("Уроки проводять ШІ, такі як EduAI-2000 та MathAI-500."),
            ["EduAI-2000", "MathAI-500"]
        )
        
    def test_analyze_resume(self):
        text = "Мій email test@gmail.com, тел 0981112233. Навички: C++, Python. Досвід роботи: 2 роки."
        result = analyze_resume(text)
        self.assertEqual(result['emails'], ["test@gmail.com"])
        self.assertEqual(result['skills'], ["C++", "Python"])
        self.assertEqual(result['experience'], "2 роки")

    def test_count_words(self):
        self.assertEqual(count_words("This is a test sentence."), 5)

    def test_count_sentences(self):
        self.assertEqual(count_sentences("This is one. This is two! Is this three?"), 3)

if __name__ == '__main__':
    import io
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLab4)
    output = io.StringIO()
    runner = unittest.TextTestRunner(stream=output, verbosity=2)
    result = runner.run(suite)
    
    print(output.getvalue())
    print(f"\nУспішних тестів: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Невдалих тестів: {len(result.failures)}")
    print(f"Помилок: {len(result.errors)}")
    
if result.failures or result.errors:
        print("\nДетальна інформація про невдалі тести та помилки:")
        for test, error in result.failures + result.errors:
            print(f"\n{test}")
            print(error)
            
