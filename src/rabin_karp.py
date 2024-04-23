def rabin_karp(haystack, needle):
    if not needle:
        return []

    divisor = 101
    base = 256 #основна система числення яка використовується для хешування
    index = []
    haystack_hash = 0
    needle_hash = 0
    first_letter_power = pow(base, len(needle) - 1) % divisor  #використовується для швидкого оновлення хеш-значення підвідрізків тексту

    for iterator in range(len(needle)):
        needle_hash = (base * needle_hash + ord(needle[iterator])) % divisor  # Виправлення тут: обчислення хеш-значення для патерна
        haystack_hash = (base * haystack_hash + ord(haystack[iterator])) % divisor  # Виправлення тут: обчислення хеш-значення для початкового відрізка тексту

    for iter in range(len(haystack) - len(needle) + 1):
        if needle_hash == haystack_hash and haystack[iter:iter + len(needle)] == needle:
            index.append(iter)

        if iter < len(haystack) - len(needle):
            haystack_hash = (base * (haystack_hash - ord(haystack[iter]) * first_letter_power) + ord(haystack[iter + len(needle)])) % divisor  # Виправлення тут: обчислення хеш-значення для наступного відрізка тексту

    return index


haystack = "ababcababcabc"
needle = "abc"
print("Індекси входжень підстрічки 'needle' у стрічці 'haystack':", rabin_karp(haystack, needle))

