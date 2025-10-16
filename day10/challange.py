class DigitalSchool:
    def __init__(self, name, city, state, courses):
        self.__name = name
        self.__city = city
        self.__state = state
        self.__courses = courses

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    def show_school_info(self):
        return {
            "Name": self.name,
            "City": self.city,
            "State": self.state,
            "Courses": self.courses
        }

    def organize_hackathon(self):
        raise NotImplementedError("This method is not overridden by subclass")


class DS_Prishtina(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        super().__init__(name, city, state, courses)
        self.__student_number = student_number

    @property
    def student_number(self):
        return self.__student_number

    @student_number.setter
    def student_number(self, number):
        self.__student_number = number

    def SCFC(self):
        print("SCFC(): Spring Code Fest organized in DS_Prishtina!")

    def organize_hackathon(self):
        print("Organizing a Hackathon event for DS_Prishtina students!")



ds = DS_Prishtina("Digital School", "Prishtina", "Kosovo", ["Python", "JavaScript", "React"], 120)

print(ds.show_school_info())
ds.SCFC()
ds.organize_hackathon()
print(f"The number of students in DS_Prishtina is {ds.student_number}.")
