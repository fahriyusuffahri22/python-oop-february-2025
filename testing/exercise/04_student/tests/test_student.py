from project.student import Student
from unittest import TestCase, main


class StudentTests(TestCase):
    def setUp(self):
        self.student_without_courses = Student("name1")
        self.student_with_courses = Student(
            "name2",
            {
                "course_name1": ["note1"],
                "course_name2": ["note1", "note2"]
            }
        )

    def test_init_(self):
        self.assertEqual(self.student_without_courses.name, "name1")
        self.assertEqual(self.student_without_courses.courses, {})

        self.assertEqual(
            self.student_with_courses.courses,
            {
                "course_name1": ["note1"],
                "course_name2": ["note1", "note2"]
            })

    def test_enroll_updates_existing_course(self):
        self.assertEqual(
            self.student_with_courses.enroll("course_name1", ["note2", "note3"]),
            "Course already added. Notes have been updated."
        )

        self.assertEqual(
            self.student_with_courses.courses,
            {
                "course_name1": ["note1", "note2", "note3"],
                "course_name2": ["note1", "note2"]
            })

    def test_enroll_adds_course_with_notes(self):
        self.assertEqual(
            self.student_without_courses.enroll("course_name1", ["note1"]),
            "Course and course notes have been added."
        )

        self.assertEqual(
            self.student_without_courses.courses,
            {
                "course_name1": ["note1"]
            })

        self.assertEqual(
            self.student_without_courses.enroll("course_name2", ["note1", "note2"], "Y"),
            "Course and course notes have been added."
        )

        self.assertEqual(
            self.student_without_courses.courses,
            {
                "course_name1": ["note1"],
                "course_name2": ["note1", "note2"]
            })

    def test_enroll_adds_course_without_notes(self):
        self.assertEqual(
            self.student_without_courses.enroll("course_name1", ["note1"], "N"),
            "Course has been added."
        )

        self.assertEqual(
            self.student_without_courses.courses,
            {
                "course_name1": []
            })


    def test_add_notes_updates_existing_course(self):
        self.assertEqual(
            self.student_with_courses.add_notes("course_name1", "note2"),
            "Notes have been updated"
        )

        self.assertEqual(
            self.student_with_courses.courses,
            {
                "course_name1": ["note1", "note2"],
                "course_name2": ["note1", "note2"]
            }
        )

    def test_add_notes_raises_course_not_found_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_without_courses.add_notes("course_name1", "note1")

        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")
        self.assertEqual(self.student_without_courses.courses, {})

    def test_leave_course_removes_existing_course(self):
        self.assertEqual(
            self.student_with_courses.leave_course("course_name2"),
            "Course has been removed"
        )

        self.assertEqual(
            self.student_with_courses.courses,
            {
                "course_name1": ["note1"]
            })

    def test_leave_course_raises_course_not_found_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.leave_course("course_name3")

        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")

        self.assertEqual(
            self.student_with_courses.courses,
            {
                "course_name1": ["note1"],
                "course_name2": ["note1", "note2"]
            })


if __name__ == "__main__":
    main()
