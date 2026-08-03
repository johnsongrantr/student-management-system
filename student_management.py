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
            age=data["age"],
            course=data["course"],
        )


class StudentManagementSystem:
    def __init__(self, data_file: str = "students.json") -> None:
        self.data_file = Path(data_file)
        self.students: list[Student] = []
        self.load()

    def load(self) -> None:
        if self.data_file.exists():
            data = json.loads(self.data_file.read_text(encoding="utf-8"))
            self.students = [Student.from_dict(item) for item in data]
        else:
            self.students = []
            self.save()

    def save(self) -> None:
        self.data_file.write_text(
            json.dumps([student.to_dict() for student in self.students], indent=2),
            encoding="utf-8",
        )

    def add_student(self, student: Student) -> None:
        self.students.append(student)
        self.save()

    def list_students(self) -> list[Student]:
        return self.students

    def get_student(self, student_id: str) -> Optional[Student]:
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def update_student(self, student_id: str, **updates) -> bool:
        for student in self.students:
            if student.student_id == student_id:
                for key, value in updates.items():
                    setattr(student, key, value)
                self.save()
                return True
        return False

    def delete_student(self, student_id: str) -> bool:
        for index, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[index]
                self.save()
                return True
        return False
