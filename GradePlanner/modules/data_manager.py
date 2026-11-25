# data_manager.py 김강민 (3순위)
# 파일은 os 모듈 사용해서 상대경로를 저장하는 변수를 생성
import json
import os

from .semester import Semester


current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir)
data_path = os.path.join(base_dir, "data")

class DataManager:
    def save_data(self, semester_list):
        os.makedirs(data_path, exist_ok=True)
        file_path = os.path.join(data_path, "grade_data.json")

        data = []
        for semester in semester_list:
            data.append(semester.to_dict())

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_data(self) -> list:
        # Semester 객체 목록으로 복원하는 방식 사용
        file_path = os.path.join(data_path, "grade_data.json")
        if not os.path.exists(file_path):
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        semester_list = []
        for semester_data in data:
            semester_list.append(Semester.from_dict(semester_data))

        return semester_list