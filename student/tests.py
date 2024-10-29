from django.test import TestCase

from student.models import Student


class StudentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.student = Student.objects.create(
            student_id="1231231",
            first_name="Kofi",
            last_name="Ntiamoah",
        )

    def test_student_attributes(self):
        self.assertEqual(self.student.student_id, "1231231")
        self.assertEqual(self.student.first_name, "Kofi")
        self.assertEqual(self.student.last_name, "Ntiamoah")
