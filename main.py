#== Алгоритм Кнута-Морріса-Пратта (KMP) для пошуку підрядка в рядку ===#
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

#== Алгоритм Боєра-Мура для пошуку підрядка в рядку ===#
def build_shift_table(pattern):
  """Створити таблицю зсувів для алгоритму Боєра-Мура."""
  table = {}
  length = len(pattern)
  # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
  for index, char in enumerate(pattern[:-1]):
    table[char] = length - index - 1
  # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
  table.setdefault(pattern[-1], length)
  return table

def boyer_moore_search(text, pattern):
  # Створюємо таблицю зсувів для патерну (підрядка)
  shift_table = build_shift_table(pattern)
  i = 0 # Ініціалізуємо початковий індекс для основного тексту

  # Проходимо по основному тексту, порівнюючи з підрядком
  while i <= len(text) - len(pattern):
    j = len(pattern) - 1 # Починаємо з кінця підрядка

    # Порівнюємо символи від кінця підрядка до його початку
    while j >= 0 and text[i + j] == pattern[j]:
      j -= 1 # Зсуваємось до початку підрядка

    # Якщо весь підрядок збігається, повертаємо його позицію в тексті
    if j < 0:
      return i # Підрядок знайдено

# Зсуваємо індекс i на основі таблиці зсувів
    # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
    i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

  # Якщо підрядок не знайдено, повертаємо -1
  return -1

text = "Being a developer is not easy"
pattern = "developer"

position = boyer_moore_search(text, pattern)
if position != -1:
  print(f"Substring found at index {position}")
else:
  print("Substring not found")


# raw = "Цей алгоритм часто використовується в текстових редакторах та системах пошуку для ефективного знаходження підрядка в тексті."

# pattern = "алг"

# print(kmp_search(raw, pattern))

def __main__():
    with open('стаття 2.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    pattern = input("Введіть підрядок для пошуку: ")
    index = kmp_search(text, pattern)
    if index != -1:
        print(f"Підрядок знайдено на позиції: {index}")
    else:
        print("Підрядок не знайдено.")

if __name__ == "__main__":
    __main__()
