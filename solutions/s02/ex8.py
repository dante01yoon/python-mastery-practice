age = int(input("나이: "))
member = input("회원(y/n): ") == "y"
print("입장" if age >= 19 and member else "불가")
