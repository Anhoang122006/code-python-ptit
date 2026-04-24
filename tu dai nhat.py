s = input().split()

max_word = ""
max_len = 0

for word in s:
    if len(word) > max_len:
        max_len = len(word)
        max_word = word

print(max_word, max_len)
