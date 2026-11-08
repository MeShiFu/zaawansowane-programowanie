from functions import (
    is_palindrome,
    fibonacci,
    count_vowels,
    calculate_discount,
    flatten_list,
    word_frequencies,
    is_prime,
)


# is_palindrome
def test_palindrome_true():
    assert is_palindrome("kajak") is True


def test_palindrome_ignores_case():
    assert is_palindrome("Kobyła ma mały bok") is True


def test_palindrome_false():
    assert is_palindrome("python") is False


def test_palindrome_empty_string():
    assert is_palindrome("") is True


def test_palindrome_single_character():
    assert is_palindrome("A") is True


# fibonacci
def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 1


def test_fibonacci_five():
    assert fibonacci(5) == 5


def test_fibonacci_ten():
    assert fibonacci(10) == 55


def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 1


def test_fibonacci_five():
    assert fibonacci(5) == 5


def test_fibonacci_ten():
    assert fibonacci(10) == 55


def test_fibonacci_negative():
    import pytest

    with pytest.raises(ValueError):
        fibonacci(-1)


# count_vowels
def test_count_vowels_python():
    assert count_vowels("Python") == 2


def test_count_vowels_all():
    assert count_vowels("AEIOUY") == 6


def test_count_vowels_none():
    assert count_vowels("bcd") == 0


def test_count_vowels_empty():
    assert count_vowels("") == 0


def test_count_vowels_polish():
    assert count_vowels("Próba żółwia") == 5


# calculate_discount
def test_discount_twenty_percent():
    assert calculate_discount(100, 0.2) == 80.0


def test_discount_zero():
    assert calculate_discount(50, 0) == 50.0


def test_discount_one_hundred_percent():
    assert calculate_discount(200, 1) == 0.0


def test_discount_negative():
    import pytest

    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)


def test_discount_above_one():
    import pytest

    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)


# flatten_list
def test_flatten_simple_list():
    assert flatten_list([1, 2, 3]) == [1, 2, 3]


def test_flatten_nested_list():
    assert flatten_list([1, [2, 3], 4]) == [1, 2, 3, 4]


def test_flatten_empty_list():
    assert flatten_list([]) == []


def test_flatten_deeply_nested_list():
    assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]


def test_flatten_mixed_list():
    assert flatten_list([[1, 2], [3, 4], 5]) == [1, 2, 3, 4, 5]


# word_frequencies
def test_word_frequencies_basic():
    assert word_frequencies("To be or not to be") == {
        "to": 2,
        "be": 2,
        "or": 1,
        "not": 1,
    }


def test_word_frequencies_punctuation():
    assert word_frequencies("Hello, hello!") == {"hello": 2}


def test_word_frequencies_empty():
    assert word_frequencies("") == {}


def test_word_frequencies_case_insensitive():
    assert word_frequencies("Python Python python") == {"python": 3}


def test_word_frequencies_polish():
    assert word_frequencies("Ala ma kota, a kot ma Ale.") == {
        "ala": 1,
        "ma": 2,
        "kota": 1,
        "a": 1,
        "kot": 1,
        "ale": 1,
    }


# is_prime
def test_is_prime_two():
    assert is_prime(2) is True


def test_is_prime_three():
    assert is_prime(3) is True


def test_is_prime_five():
    assert is_prime(5) is True


def test_is_prime_ninety_seven():
    assert is_prime(97) is True


def test_is_prime_four():
    assert is_prime(4) is False


def test_is_prime_zero():
    assert is_prime(0) is False


def test_is_prime_one():
    assert is_prime(1) is False
