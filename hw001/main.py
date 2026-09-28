# GUI 프로그래밍 혹은 Turtle 모듈을 이용하여 인터페이스 제작
# 파일입출력을 이용하여 health.txt를 불러들여 읽는다
# 정규식을 이용하여 전화번호, 이름, 키, 몸무게, [비]정상 을 split() 하여 이차원 배열로 저장한다
# BMI 는 kg / (cm / 100) ** 2 로 계산할 수 있다.

# 출력은 아래처럼 진행된다.

# 전화번호 이름 키 (cm) 몸무게(kg) BMI 소견
# 010-1234-5678 홍길동 175 72 25.4 정상
# 010-2456-2280 김길동 180 80 26 과체중
# 따라서 문자열 포멧팅을 이용하여 출력 결과를 정리한다.

import re
import turtle as t
f = open("health.txt", "r", encoding="utf-8")

phone = re.compile(r'010-[0-9]{4}-[0-9]{4}')
name = re.compile(r'["가"-"힣]*')
cm = re.compile(r'[0-9]*cm')
kg = re.compile(r'[0-9]*kg')
user_list = []

if phone.match(f.readline()):
    user_list.append(f.readline().split().strip())

def get_bmi(cmlst, kglst):
    global bmilst
    idx = 0
    for _ in range(len(cmlst)):
        bmilst.append(f"{kglst[idx] / (cmlst[0] / 100) ** 2:.2f}")
        idx += 1

def test():
    # get_bmi(cm_stu, kg_stu)
    print(bmilst)

if __name__ == "__main__":
    test()
