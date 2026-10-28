total = int(input("초: "))
hours = total // 3600
minutes = total % 3600 // 60
seconds = total % 60
print(f"{hours}시간 {minutes}분 {seconds}초")
