class Student:
    def __init__(self, student_id, grade_list) -> None:
        self.student_id = student_id
        self.grade_list = grade_list

    def __str__(self) -> str:
        return f"Student ID: {self.student_id}\nGrades: {self.grade_list}"

    def __lt__(self, other) -> bool:
        if sum(self.grade_list) < sum(other.grade_list):
            return True
        else:
            return False

    def get_max_grade(self):
        return max(self.grade_list)



