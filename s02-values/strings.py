word = "python"
print(word[0], word[-1])
print(word[1:4], word[:2], word[3:])
print(len(word))

raw = "  hello, python world  "
clean = raw.strip()
print(clean)
print(clean.upper())
print(clean.replace("python", "파이썬"))
print(clean.split(", "))

price = 12500
rate = 0.4567
print(f"가격 {price:,}원, 비율 {rate:.1%}")
print("줄을\n바꿔요")
email = "dante@example.com"
print("@" in email, email.endswith(".com"))
