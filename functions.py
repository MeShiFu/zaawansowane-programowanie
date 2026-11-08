import re


def is_palindrome(text: str) -> bool:
    normalized_text = text.replace(" ", "").lower()
    return normalized_text == normalized_text[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n nie może być ujemne")

    if n == 0:
        return 0

    if n == 1:
        return 1

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current


def count_vowels(text: str) -> int:
    vowels = "aeiouyąęó"
    return sum(1 for char in text.lower() if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("Rabat musi być w przedziale od 0 do 1")

    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


def word_frequencies(text: str) -> dict:
    words = re.findall(r"\b\w+\b", text.lower())
    frequencies = {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
