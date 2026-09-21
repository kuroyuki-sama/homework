# 여러 학생들의 키와 몸무게를 리스트로 입력 받아 BMI 리스트를 출력하는
# 함수와 테스트하는 함수를 작성하시오.
# BMI 함수는 지난 시간에 작성한 get_bmi 함수를 이용하여 작성하시오.

# 입력 조건 예> 몸무게 리스트 : [167, 168, 185]

kg_stu = [int(x) for x in input("몸무게 리스트 : ").strip("[]").split(", ")]
cm_stu = [int(x) for x in input("키 리스트 : ").strip("[]").split(", ")]
bmilst = []

def get_bmi(cmlst, kglst):
    global bmilst
    # idx = 0
    for idx in range(len(cmlst)):
        bmilst.append(f"{kglst[idx] / (cmlst[idx] / 100) ** 2:.2f}")
        # idx += 1

def test():
    get_bmi(cm_stu, kg_stu)
    print(bmilst)

if __name__ == "__main__":
    test()
