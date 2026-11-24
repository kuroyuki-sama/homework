from modules.grade_calculator import GradeCalculator
from modules.data_manager import DataManager
from modules.gui import GradePlannerGUI

import tkinter as tk


def main():
    data_manager = DataManager()
    calculator = GradeCalculator()

    semester_list = data_manager.load_data()

    root = tk.Tk()

    app = GradePlannerGUI(
        root,
        semester_list,
        calculator,
        data_manager
    )

    root.mainloop()


if __name__ == "__main__":
    main()