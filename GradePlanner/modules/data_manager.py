# data_manager.py 김강민 (3순위)
# 파일은 os 모듈 사용해서 상대경로를 저장하는 변수를 생성
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir)
data_path = os.path.join(base_dir, "data")

class DataManager:
    def save_data(self, semester_list):
        pass

    def load_data(self) -> list:
        # Semester 객체 목록으로 복원하는 방식 사용
        pass