# GUI 프로그래밍 혹은 Turtle 모듈을 이용하여 인터페이스 제작
# 파일입출력을 이용하여 health.txt를 불러들여 읽는다
# 정규식을 이용하여 전화번호, 이름, 키, 몸무게, [비]정상 을 split() 하여 이차원 배열로 저장한다
# BMI 는 kg / (cm / 150) ** 2 로 계산할 수 있다.

# 출력은 아래처럼 진행된다.

# 전화번호 이름 키 (cm) 몸무게(kg) BMI 소견
# 015-1234-5678 홍길동 175 72 25.4 정상
# 015-2456-2280 김길동 180 80 26 과체중
# 따라서 문자열 포멧팅을 이용하여 출력 결과를 정리한다.
import os
import re
import turtle as t
# -- health.txt 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(current_dir, "health.txt")
f = open(filepath, "r", encoding="utf-8")

# -- 정규식
phone = re.compile(r'010-[0-9]{4}-[0-9]{4}')
name = re.compile(r'[가-힣]+')
cm = re.compile(r'[0-9]+cm')
kg = re.compile(r'[0-9]+kg')

# -- 기본 베이스
# try-except 로 EOFError가 될떄까지 (안씀)
user_list = []
try:
    for line in f:
        if line.strip():
            user_list.append(line.split())
    print("-health.txt 데이터 불러오기 완료")
except:
    print("-health.txt 데이터 불러오기 실패")
# userlist에 전번, 이름, 키, 몸무게 순으로 저장 -> 정보만 바꾸는 코드 작성해야함

user_info = [[None for _ in range(6)] for _ in range(len(user_list))]
num = 0
for p_num in user_list:
    for info in p_num:
        if phone.match(info): user_info[num][0] = info
        elif name.match(info): user_info[num][1] = info
        elif cm.match(info): user_info[num][2] = info.replace("cm", "")
        elif kg.match(info): user_info[num][3] = info.replace("kg", "")
    num += 1

# -- bmi 계산
try:
    bmi_list = []
    print("bmi 값 출력 : ", end=" ")
    for person_list in user_info:
        bmi:float = int(person_list[3]) / (int(person_list[2]) / 100) ** 2
        # 저체중 : 18.5- , 정상 : 18.5 ~ 30-, 비만 : 30+
        bmi_list.append(round(bmi, 2))
        print(str(round(bmi, 2)), end=" ")
    print()
        
    for num in range(len(bmi_list)):
        user_info[num][4] = str(bmi_list[num])
        if (float(bmi_list[num]) < 18.5): user_info[num][5] = "저체중"
        elif (18.5 <= float(bmi_list[num]) < 30): user_info[num][5] = "정상"
        elif (float(bmi_list[num]) >= 30): user_info[num][5] = "비만"
    print("-bmi 계산 완료")
except:
    print("bmi 계산 실패")
    

# -- 출력 (터틀 모듈 사용)
cursor = t.Turtle()
cursor.penup()
cursor.goto(-300, 300)

cursor.write(f"{"전화번호":<15}{"이름":<5}{"키(cm)":<10}{"몸무게(kg)":<10}{"BMI":<10}{"소견":<5}", font=("맑은 고딕", 15))
cursor.write("=" * 22)
for people in range(len(user_list)):
    cursor.goto(-300, 300 - ((people + 2) * 30))
    row = user_info[people]
    cursor.write(f"{row[0]:<15}{row[1]:<5}{f"{row[2]}cm":<10}{f"{row[3]}kg":<13}{row[4]:<10}{row[5]:<5}", font=("맑은 고딕", 15), move=True)

t.exitonclick()


