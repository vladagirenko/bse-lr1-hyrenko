import random

# Константи для стилів тексту (щоб уникнути дублювання літералів)
STYLE_INTRIGUING = "Інтригуючий"
STYLE_HUMOROUS = "Гумористичний"

# Шаблони для імітації генерації ШІ за специфікацією HookCraft [cite: 1, 22]
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
    # FR-02: Генерація варіантів текстових «гачків» [cite: 31]
    templates = HOOK_TEMPLATES.get(style, HOOK_TEMPLATES[STYLE_INTRIGUING])
    selected = random.sample(templates, min(count, len(templates)))
    return [hook.format(topic=topic) for hook in selected]

def main():
    print("=== HookCraft: AI Content Hook Generator ===") 
    
    # FR-01: Введення теми або опису контенту [cite: 30]
    topic = input("Введіть тему контенту (наприклад, 'ідеальна паста'): ").strip() 
    if not topic:
        print("Помилка: тема не може бути порожньою!")
        return

    # FR-03: Вибір стилю тексту [cite: 32]
    print("\nОберіть тональність (стиль) тексту:")
    print(f"1. {STYLE_INTRIGUING}")
    print(f"2. {STYLE_HUMOROUS}")
    style_choice = input("Ваш вибір (1 або 2): ")
    
    style = STYLE_HUMOROUS if style_choice == "2" else STYLE_INTRIGUING
    
    print(f"\nГенерація варіантів для теми '{topic}' у стилі '{style}'... [NFR-P-02]") 
    
    # FR-04: Відображення списку варіантів [cite: 33]
    generated_hooks = generate_hooks(topic, style, count=3)
    
    print("\n=== Згенеровані «гачки» ===") 
    for index, hook in enumerate(generated_hooks, 1):
        print(f"{index}. {hook}")

if __name__ == "__main__":
    main()