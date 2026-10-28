# 미니 프로젝트 2: 단위 변환기(cm → 인치)
CM_PER_INCH = 2.54

cm = float(input("길이(cm): "))
inch = cm / CM_PER_INCH
print(f"{cm}cm는 {inch:.2f}인치입니다.")
