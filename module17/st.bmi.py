import streamlit as st

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

    def run(self):
        st.title("BMI Calculator")
        st.write("Calculate your Body Mass Index (BMI)")

        with st.form("bmi_form", clear_on_submit=True):
            st.header("Enter your personal information")
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=1, step=1)
            gender = st.selectbox("Gender", ["Male", "Female"])
            weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
            height = st.number_input("Height (cm)", min_value=0.5, step=0.01)
            submitted = st.form_submit_button("Calculate BMI")

            if submitted:
                person = Person(name, age, gender, weight, height)
                self.add_person(person)
                bmi = person.calculate_bmi()
                category = person.get_category()

                st.success(f"{name}'s Results")
                st.write(f"Age: {age} years")
                st.write(f"Gender: {gender}")
                st.write(f"BMI: {bmi:.2f}")
                st.write(f"Category: {category}")

        if len(self.people) > 0:
            st.divider()
            st.subheader("BMI History")
            for p in self.people:
                st.write(f"{p.name} ({p.age} yrs): {p.calculate_bmi():.2f} - {p.get_category()}")


if __name__ == "__main__":
    app = BMICalculator()
    app.run()
