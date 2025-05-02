a = input("Enter text: ").lower()
split_nsp = [i for i in a if i.isalpha()]
if not split_nsp:
    print("No valid characters to process.")
    exit()

from collections import Counter
char_count = Counter(split_nsp)
most_com, c = char_count.most_common(1)[0]

shift = ord(most_com) - ord('e')

decode_n = [chr((ord(i) - shift - ord('a')) % 26 + ord('a')) if i.isalpha() else i for i in a]
decode_char = ''.join(decode_n)

print("Decoded text:", decode_char)
print("Shift value:", shift)