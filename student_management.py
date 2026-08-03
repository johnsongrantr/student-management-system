from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Student:
    student_id: str
    name: str
    age: int
    course: str

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(
            student_id=data["student_id"],
            name=data["name"],
<<<<<<< HEAD
            age=int(data["age"]),
=======
            age=data["age"],
>>>>>>> 7da123323f54031d676e54fbf8bca919fbcf2a01
            course=data["course"],
        )


<<<<<<< HEAD
class StudentManager:
=======
class StudentManagementSystem:
>>>>>>> 7da123323f54031d676e54fbf8bca919fbcf2a01
    def __init__(self, data_file: str = "students.json") -> None:
        self.data_file = Path(data_file)
        self.students: list[Student] = []
        self.load()

    def load(self) -> None:
        if self.data_file.exists():
<<<<<<< HEAD
            try:
                data = json.loads(self.data_file.read_text(encoding="utf-8"))
                self.students = [Student.from_dict(item) for item in data]
            except json.JSONDecodeError:
                self.students = []
                self.save()
=======
            data = json.loads(self.data_file.read_text(encoding="utf-8"))
            self.students = [Student.from_dict(item) for item in data]
>>>>>>> 7da123323f54031d676e54fbf8bca919fbcf2a01
        else:
            self.students = []
            self.save()

    def save(self) -> None:
        self.data_file.write_text(
            json.dumps([student.to_dict() for student in self.students], indent=2),
            encoding="utf-8",
        )

<<<<<<< HEAD
    def add_student(self, student: Student) -> bool:
        if self.get_student(student.student_id):
            return False
        self.students.append(student)
        self.save()
        return True

    def get_students(self) -> list[Student]:
=======
    def add_student(self, student: Student) -> None:
        self.students.append(student)
        self.save()

    def list_students(self) -> list[Student]:
>>>>>>> 7da123323f54031d676e54fbf8bca919fbcf2a01
        return self.students

    def get_student(self, student_id: str) -> Optional[Student]:
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

<<<<<<< HEAD
    def update_student(self, student_id: str, *, name: str, age: int, course: str) -> bool:
        student = self.get_student(student_id)
        if not student:
            return False
        student.name = name
        student.age = age
        student.course = course
        self.save()
        return True
=======
    def update_student(self, student_id: str, **updates) -> bool:
        for student in self.students:
            if student.student_id == student_id:
                for key, value in updates.items():
                    setattr(student, key, value)
                self.save()
                return True
        return False
>>>>>>> 7da123323f54031d676e54fbf8bca919fbcf2a01

    def delete_student(self, student_id: str) -> bool:
        for index, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[index]
                self.save()
                return True
        return False
