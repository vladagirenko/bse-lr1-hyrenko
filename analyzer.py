# Функція, яка приймає текст програми, рахує кількість символів і слів у ньому, та виводить аналіз у консоль
def analyze_text(text):
    char_count = len(text)
    word_count = len(text.split())
    print(f"Кількість символів: {char_count}")
    print(f"Кількість слів: {word_count}")

analyze_text("Більшість людей ніколи не дізнаються правду про HookCraft...")