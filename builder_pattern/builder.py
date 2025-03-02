from abc import ABC, abstractmethod
from enum import Enum

class BinaryResponse(Enum):
    """
    Enum to represent binary responses: YES or NO.
    """
    YES = "Yes"
    NO = "No"

class Person:
    """
    A class representing a person with attributes such as name, age, 
    city of residence, workplace, school, marital status, and children status.
    """
    def __init__(self, name=None, age=None):
        """
        Initializes a Person object.

        Args:
            name (str, optional): The name of the person. Defaults to None.
            age (int, optional): The age of the person. Defaults to None.
        """
        self.name = name
        self.age = age
        self.city = None
        self.works_at = None 
        self.school = None
        self.is_married = None
        self.has_children = None

    def __str__(self):
        """
        Returns a string representation of the Person object.

        Returns:
            str: A formatted string describing the person's details.
        """
        return (f"Person: {self.name}, Age: {self.age}, Lives in {self.city}, "
                f"Studied at {self.school if self.school else 'N/A'}, "
                f"Works at {self.works_at if self.works_at else 'N/A'}, "
                f"Married: {self.is_married}, Has children: {self.has_children}")


class PersonBuilder(ABC):
    """
    Abstract builder class for constructing Person objects.
    """
    def __init__(self):
        """
        Initializes the PersonBuilder with a new Person instance.
        """
        self.person = Person()

    def set_name(self, name):
        """
        Sets the name of the person.

        Args:
            name (str): The name of the person.

        Returns:
            PersonBuilder: The builder instance for method chaining.
        """
        self.person.name = name
        return self

    def set_age(self, age):
        """
        Sets the age of the person.

        Args:
            age (int): The age of the person.

        Returns:
            PersonBuilder: The builder instance for method chaining.
        """
        self.person.age = age
        return self

    @abstractmethod
    def lives_in(self, city):
        """
        Abstract method to set the city where the person lives.

        Args:
            city (str): The city of residence.
        """
        pass

    @abstractmethod
    def build(self):
        """
        Abstract method to build and return the Person instance.

        Returns:
            Person: The constructed Person object.
        """
        pass


class StudentProfile(PersonBuilder):
    """
    Builder class for creating a Student profile, which extends PersonBuilder.
    """
    def lives_in(self, city):
        """
        Sets the city where the student lives.

        Args:
            city (str): The city of residence.

        Returns:
            StudentProfile: The builder instance for method chaining.
        """
        self.person.city = city
        return self

    def studies_at(self, school):
        """
        Sets the school where the student is studying.

        Args:
            school (str): The name of the school.

        Returns:
            StudentProfile: The builder instance for method chaining.
        """
        self.person.school = school
        return self

    def build(self):
        """
        Builds and returns a Student profile as a Person object.

        Returns:
            Person: The constructed Person object.
        """
        built_person = self.person
        self.person = Person()  # Reset for new builds
        return built_person


class ProfessionalProfile(PersonBuilder):
    """
    Builder class for creating a Professional profile, which extends PersonBuilder.
    """
    def lives_in(self, city):
        """
        Sets the city where the professional lives.

        Args:
            city (str): The city of residence.

        Returns:
            ProfessionalProfile: The builder instance for method chaining.
        """
        self.person.city = city
        return self

    def works_at(self, company): 
        """
        Sets the company where the professional works.

        Args:
            company (str): The name of the company.

        Returns:
            ProfessionalProfile: The builder instance for method chaining.
        """
        self.person.works_at = company
        return self

    def is_married(self, is_married: BinaryResponse):
        """
        Sets the marital status of the professional.

        Args:
            is_married (BinaryResponse): Enum value (YES/NO) representing marital status.

        Returns:
            ProfessionalProfile: The builder instance for method chaining.
        """
        self.person.is_married = is_married
        return self

    def has_children(self, has_children: BinaryResponse):
        """
        Sets whether the professional has children.

        Args:
            has_children (BinaryResponse): Enum value (YES/NO) representing whether they have children.

        Returns:
            ProfessionalProfile: The builder instance for method chaining.
        """
        self.person.has_children = has_children
        return self

    def build(self):
        """
        Builds and returns a Professional profile as a Person object.

        Returns:
            Person: The constructed Person object.
        """
        built_person = self.person
        self.person = Person()  # Reset for new builds
        return built_person


if __name__ == "__main__":
    # Create a Student Profile
    student = (StudentProfile()
               .set_name("Alice")
               .set_age(22)
               .lives_in("London")
               .studies_at("Oxford")
               .build())
    print(student)  

    # Create a Professional Profile
    professional = (ProfessionalProfile()
                    .set_name("Bob")
                    .set_age(35)
                    .lives_in("New York")
                    .works_at("Google")
                    .is_married(BinaryResponse.YES)
                    .has_children(BinaryResponse.NO))
    print(professional.build())