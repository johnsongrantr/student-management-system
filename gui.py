import tkinter as tk
from tkinter import messagebox, ttk

from student_management import Student, StudentManager


class StudentGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("700x450")
        self.manager = StudentManager("students.json")
        self.editing_id: str | None = None

        self.build_ui()
        self.refresh_list()

    def build_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding=12)
        main_frame.pack(fill="both", expand=True)

        form_frame = ttk.LabelFrame(main_frame, text="Student Details", padding=10)
        form_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=(0, 10))

        ttk.Label(form_frame, text="Student ID:").grid(row=0, column=0, sticky="w", pady=2)
        self.student_id_entry = ttk.Entry(form_frame, width=30)
        self.student_id_entry.grid(row=0, column=1, sticky="ew", pady=2)

        ttk.Label(form_frame, text="Name:").grid(row=1, column=0, sticky="w", pady=2)
        self.name_entry = ttk.Entry(form_frame, width=30)
        self.name_entry.grid(row=1, column=1, sticky="ew", pady=2)

        ttk.Label(form_frame, text="Age:").grid(row=2, column=0, sticky="w", pady=2)
        self.age_entry = ttk.Entry(form_frame, width=30)
        self.age_entry.grid(row=2, column=1, sticky="ew", pady=2)

        ttk.Label(form_frame, text="Course:").grid(row=3, column=0, sticky="w", pady=2)
        self.course_entry = ttk.Entry(form_frame, width=30)
        self.course_entry.grid(row=3, column=1, sticky="ew", pady=2)

        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        ttk.Button(button_frame, text="Save", command=self.save_student).pack(side="left", padx=(0, 5))
        ttk.Button(button_frame, text="Clear", command=self.clear_form).pack(side="left", padx=(0, 5))
        ttk.Button(button_frame, text="Delete", command=self.delete_student).pack(side="left")

        list_frame = ttk.LabelFrame(main_frame, text="Students", padding=10)
        list_frame.grid(row=0, column=1, sticky="nsew")

        self.student_list = tk.Listbox(list_frame, height=15, width=45)
        self.student_list.pack(fill="both", expand=True)
        self.student_list.bind("<<ListboxSelect>>", self.on_select)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

    def refresh_list(self) -> None:
        self.student_list.delete(0, tk.END)
        for student in self.manager.get_students():
            self.student_list.insert(
                tk.END,
                f"{student.student_id} | {student.name} | {student.age} | {student.course}",
            )

    def clear_form(self) -> None:
        self.editing_id = None
        self.student_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)
        self.student_list.selection_clear(0, tk.END)

    def on_select(self, event) -> None:
        selection = self.student_list.curselection()
        if not selection:
            return
        item = self.student_list.get(selection[0])
        student_id = item.split(" | ")[0]
        student = self.manager.get_student(student_id)
        if student:
            self.editing_id = student.student_id
            self.student_id_entry.delete(0, tk.END)
            self.student_id_entry.insert(0, student.student_id)
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, student.name)
            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(0, str(student.age))
            self.course_entry.delete(0, tk.END)
            self.course_entry.insert(0, student.course)

    def save_student(self) -> None:
        student_id = self.student_id_entry.get().strip()
        name = self.name_entry.get().strip()
        age_text = self.age_entry.get().strip()
        course = self.course_entry.get().strip()

        if not student_id or not name or not age_text or not course:
            messagebox.showwarning("Missing data", "Please fill in all fields.")
            return

        try:
            age = int(age_text)
        except ValueError:
            messagebox.showerror("Invalid age", "Age must be a number.")
            return

        if self.editing_id:
            updated = self.manager.update_student(self.editing_id, name=name, age=age, course=course)
            if updated:
                messagebox.showinfo("Updated", "Student updated successfully.")
            else:
                messagebox.showerror("Error", "Could not update student.")
        else:
            student = Student(student_id=student_id, name=name, age=age, course=course)
            added = self.manager.add_student(student)
            if added:
                messagebox.showinfo("Added", "Student added successfully.")
            else:
                messagebox.showerror("Duplicate ID", "A student with that ID already exists.")
                return

        self.refresh_list()
        self.clear_form()

    def delete_student(self) -> None:
        student_id = self.student_id_entry.get().strip()
        if not student_id:
            messagebox.showwarning("No selection", "Select a student first.")
            return

        confirm = messagebox.askyesno("Delete student", f"Delete student {student_id}?")
        if not confirm:
            return

        deleted = self.manager.delete_student(student_id)
        if deleted:
            messagebox.showinfo("Deleted", "Student deleted successfully.")
        else:
            messagebox.showerror("Not found", "Student not found.")
            return

        self.refresh_list()
        self.clear_form()


def main() -> None:
    root = tk.Tk()
    StudentGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
