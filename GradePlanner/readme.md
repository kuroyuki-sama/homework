# 공동개발규칙 및 프로그램 구조

1. **명세서에 없는 클래스명이나 함수명을 임의로 변경하지 않는다.**
2. **다른 팀원의 파일을 사용하기 전에 함수의 매개변수와 반환값을 확인한다.**
3. **AI를 활용해 코드를 작성하더라도 코드의 작동 원리를 이해하고 직접 테스트한다.**


* 파일 구조
main.py	프로그램 실행 및 전체 모듈 연결
subject.py	과목 정보를 관리하는 클래스
semester.py	학기 및 학기별 과목 관리 클래스
grade_calculator.py	학기 평점, 누적 평점, 목표 평점 계산
data_manager.py	JSON 저장 및 불러오기
gui.py	tkinter GUI 구현


클래스명	역할

Subject	하나의 과목 정보
Semester	하나의 학기 정보
GradeCalculator	평점 계산
DataManager	데이터 저장 및 불러오기
GradePlannerGUI	GUI 화면 및 이벤트 관리


변수명	의미

subject_name	과목명
credit	과목 학점
grade	과목 성적
semester_name	학기 이름
subjects	학기에 포함된 과목 목록
semester_list	전체 학기 목록
current_gpa	현재 누적 평점
target_gpa	목표 누적 평점
total_credits	현재까지 이수한 총학점

클래스 규칙
- Semester는 여러 Subject 객체를 보유한다.

- GradeCalculator는 Semester 객체 또는 학기 목록을 받아 계산한다

- DataManager는 학기 목록을 JSON으로 저장하고, JSON을 객체 목록으로 복원한다.

- GradePlannerGUI는 다른 클래스의 기능을 호출해 화면에 결과를 표시한다.

- main.py는 객체를 생성하고 각 모듈을 연결한다.