text = input("문장: ").strip()
words = text.split()
print(f"단어 {len(words)}개, 처음 {words[0]}, 마지막 {words[-1]}")
