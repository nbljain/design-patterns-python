import unittest
from enum import Enum
from builder_pattern.builder import BinaryResponse, Person, StudentProfile, ProfessionalProfile



class TestPersonBuilder(unittest.TestCase):

    def test_student_profile_creation(self):
        """Test creating a StudentProfile using the builder."""
        student = (StudentProfile()
                   .set_name("Alice")
                   .set_age(22)
                   .lives_in("London")
                   .studies_at("Oxford")
                   .build())

        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.age, 22)
        self.assertEqual(student.city, "London")
        self.assertEqual(student.school, "Oxford")
        self.assertIsNone(student.works_at)  # A student shouldn't have a workplace set
        self.assertIsNone(student.is_married)  # A student shouldn't have marital status set
        self.assertIsNone(student.has_children)  # A student shouldn't have children status set

    def test_professional_profile_creation(self):
        """Test creating a ProfessionalProfile using the builder."""
        professional = (ProfessionalProfile()
                        .set_name("Bob")
                        .set_age(35)
                        .lives_in("New York")
                        .works_at("Google")
                        .is_married(BinaryResponse.YES)
                        .has_children(BinaryResponse.NO)
                        .build())

        self.assertEqual(professional.name, "Bob")
        self.assertEqual(professional.age, 35)
        self.assertEqual(professional.city, "New York")
        self.assertEqual(professional.works_at, "Google")
        self.assertEqual(professional.is_married, BinaryResponse.YES)
        self.assertEqual(professional.has_children, BinaryResponse.NO)
        self.assertIsNone(professional.school)  # A professional shouldn't have a school set

    def test_student_profile_does_not_have_professional_methods(self):
        """Test that StudentProfile does not allow setting workplace, marital status, or children status."""
        student = StudentProfile().set_name("Charlie").set_age(21).lives_in("Paris").studies_at("Sorbonne").build()

        # Ensure that work, marriage, and children attributes remain None
        self.assertIsNone(student.works_at)
        self.assertIsNone(student.is_married)
        self.assertIsNone(student.has_children)

    def test_professional_profile_can_set_all_attributes(self):
        """Test that ProfessionalProfile can set all expected attributes."""
        professional = (ProfessionalProfile()
                        .set_name("David")
                        .set_age(40)
                        .lives_in("Berlin")
                        .works_at("Amazon")
                        .is_married(BinaryResponse.NO)
                        .has_children(BinaryResponse.YES)
                        .build())

        self.assertEqual(professional.name, "David")
        self.assertEqual(professional.age, 40)
        self.assertEqual(professional.city, "Berlin")
        self.assertEqual(professional.works_at, "Amazon")
        self.assertEqual(professional.is_married, BinaryResponse.NO)
        self.assertEqual(professional.has_children, BinaryResponse.YES)

    def test_student_profile_reset_after_build(self):
        """Test that building a student profile resets the builder."""
        builder = StudentProfile()
        student1 = builder.set_name("Emma").set_age(19).lives_in("Madrid").studies_at("UCM").build()
        student2 = builder.set_name("Liam").set_age(20).lives_in("Rome").studies_at("Sapienza").build()

        self.assertEqual(student1.name, "Emma")
        self.assertEqual(student2.name, "Liam")
        self.assertNotEqual(student1, student2)  # Ensure new objects are created

    def test_professional_profile_reset_after_build(self):
        """Test that building a professional profile resets the builder."""
        builder = ProfessionalProfile()
        professional1 = builder.set_name("Sophia").set_age(30).lives_in("Tokyo").works_at("Sony").build()
        professional2 = builder.set_name("James").set_age(45).lives_in("Seoul").works_at("Samsung").build()

        self.assertEqual(professional1.name, "Sophia")
        self.assertEqual(professional2.name, "James")
        self.assertNotEqual(professional1, professional2)  # Ensure new objects are created


if __name__ == '__main__':
    unittest.main()
