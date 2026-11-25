from .subject import Subject


# semester.py 김강민 (2순위)
class Semester:
    def __init__(self, semester_name):
        self.semester_name = semester_name
        self.subjects = []

    def add_subject(self, subject): # 성공 여부 반환
        self.subjects.append(subject)
        return True

    def delete_subject(self, subject_name): # 성공 여부 반환
        for index, subject in enumerate(self.subjects):
            if subject.subject_name == subject_name:
                del self.subjects[index]
                return True
        return False

    def to_dict(self): # 학기 정보가 담긴 딕셔너리 반환
        subject_data = []
        for subject in self.subjects:
            subject_data.append(subject.to_dict())

        return {
            "semester_name": self.semester_name,
            "subjects": subject_data
        }

    @classmethod
    def from_dict(cls, data): #Semester 객체 반환
        semester = cls(data["semester_name"])

        for subject_data in data["subjects"]:
            subject = Subject.from_dict(subject_data)
            semester.add_subject(subject)

        return semester