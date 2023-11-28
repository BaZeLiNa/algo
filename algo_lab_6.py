import random


def rabin_karp_search(pattern, text):
    prime = 10003

    pattern_len = len(pattern)
    text_len = len(text)
    x = 37

    def calculate_hash(string):
        hash_value = 0
        for i in range(len(string)):
            hash_value += ord(string[i]) * x**(len(string) - i - 1)
        return hash_value % prime

    pattern_hash = calculate_hash(pattern)
    text_hash = calculate_hash(text[:pattern_len])
    print(pattern_hash)
    print(pattern_hash % prime)
    print(text_hash)
    print(text_hash % prime)

    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash and text[i:i + pattern_len] == pattern:
            print(f"Find needle in position: {i}")

        if i < text_len - pattern_len:
            text_hash -= ord(text[i]) * x ** (pattern_len - 1)
            text_hash = (text_hash * x + ord(text[i + pattern_len])) % prime


if __name__ == "__main__":
    haystack = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    needle = "ipsum"
    rabin_karp_search(needle, haystack)
