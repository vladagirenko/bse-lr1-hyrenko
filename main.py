import random

# Константи для стилів тексту (щоб уникнути дублювання літералів)
STYLE_INTRIGUING = "Інтригуючий"
STYLE_HUMOROUS = "Гумористичний"

# Шаблони для імітації генерації ШІ за специфікацією HookCraft
HOOK_TEMPLATES = {
    STYLE_INTRIGUING: [
        "Більшість людей ніколи не дізнаються правду про {topic}...",
        "Ось чому те, що ви знаєте про {topic} — це велика помилка.",
        "Це один секрет про {topic}, який повністю змінить усе."
    ],
    STYLE_HUMOROUS: [
        "Мій кіт розуміє {topic} краще, ніж 90% експертів. Ось чому...",
        "{topic} — це як спроба приготувати пасту за 5 хвилин: хаос, але весело."
    ]
}

def generate_hooks(topic, style, count=3):
    # Якщо стиль не знайдено, за замовчуванням беремо інтригуючий константний стиль
    templates = HOOK_TEMPLATES.get(style, HOOK_TEMPLATES[STYLE_INTRIGUING])
    selected = random.sample(templates, min(count, len(templates)))
    return [hook.format(topic=topic) for hook in selected]

def main():
    print("=== HookCraft: AI Content Hook Generator ===")
    
    # Введення теми (Вимога FR-01 з SRS)
    topic = input("Введіть тему контенту (наприклад, 'ідеальна паста'): ").strip()
    if not topic:
        print("Помилка: тема не може бути порожньою!")
        return

    # Вибір стилю (Вимога FR-03 з SRS)
    print("\nОберіть тональність (стиль) тексту:")
    print(f"1. {STYLE_INTRIGUING}")
    print(f"2. {STYLE_HUMOROUS}")
    style_choice = input("Ваш вибір (1 або 2): ")
    
    style = STYLE_HUMOROUS if style_choice == "2" else STYLE_INTRIGUING
    
    print(f"\nГенерація варіантів для теми '{topic}' у стилі '{style}'...")
    
    # Виведення результату (Вимога FR-04 з SRS)
    generated_hooks = generate_hooks(topic, style, count=3)
    
    print("\n=== Згенеровані «гачки» ===")
    for index, hook in enumerate(generated_hooks, 1):
        print(f"{index}. {hook}")

if __name__ == "__main__":
    main()