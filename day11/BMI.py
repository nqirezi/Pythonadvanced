class Person:
    def __init__(self, name, age, gender, weight, height):
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.weight = float(weight)
        self.height = float(height)

    def calculate_bmi(self):

        return self.weight / (self.height ** 2)

    def get_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"


class BMICalculator:
    def __init__(self):
        self.people = []  

    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):
        while True:
            print("\n--- Enter Personal Info ---")
            name = input("Name: ")
            age = input("Age: ")
            gender = input("Gender: ")
            weight = input("Weight (kg): ")
            height = input("Height (m): ")

            person = Person(name, age, gender, weight, height)
            self.add_person(person)

            more = input("Add another person? (y/n): ").lower()
            if more != "y":
                break

    def print_results(self):
        print("\n--- BMI Results ---")
        for person in self.people:
            bmi = person.calculate_bmi()
            category = person.get_category()
            print(f"{person.name} ({person.age} yrs): BMI = {bmi:.2f}, Category = {category}")

    def run(self):
        print("Welcome to the BMI Calculator!")
        self.collect_user_data()
        self.print_results()
        print("\nThank you for using the BMI Calculator!")


if __name__ == "__main__":
    app = BMICalculator()
    app.run()
