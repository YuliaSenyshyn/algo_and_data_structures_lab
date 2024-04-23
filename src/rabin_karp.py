def rabin_karp(haystack, needle, divisor: int = 101, base: int = 256):
    if not needle:
        return []
    index = []
    haystack_hash = 0
    needle_hash = 0
    first_letter_power = pow(base, len(needle) - 1) % divisor

    for iterator in range(len(needle)):
        needle_hash = (base * needle_hash + ord(needle[iterator])) % divisor
        haystack_hash = (base * haystack_hash + ord(haystack[iterator])) % divisor

    for iter in range(len(haystack) - len(needle) + 1):
        if needle_hash == haystack_hash and haystack[iter:iter + len(needle)] == needle:
            index.append(iter)

        if iter < len(haystack) - len(needle):
            haystack_hash = (base * (haystack_hash - ord(haystack[iter]) * first_letter_power) + ord(haystack[iter + len(needle)])) % divisor  

    return index


haystack = "ababcababcabc"
needle = "abc"
print("Індекси входжень підстрічки 'needle' у стрічці 'haystack':", rabin_karp(haystack, needle))

