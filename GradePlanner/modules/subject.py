# subject.py 김강민 (1순위)
class Subject:
    def __init__(self, subject_name, credit, grade): # 과목이름, 이수학점, 평점
        self.subject_name = subject_name
        self.credit = credit
        self.grade = grade

    def to_dict(self): #과목에 해당하는 내용 딕셔너리로 반환
        return {
            "subject_name": self.subject_name,
            "credit": self.credit,
            "grade": self.grade
        }

    @classmethod
    def from_dict(cls, data): # data의 내용을 Subject 객체로 반환
        return cls(
            data["subject_name"],
            data["credit"],
            data["grade"]
        )  