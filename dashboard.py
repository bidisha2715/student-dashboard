import csv
import matplotlib.pyplot as plt
from collections import Counter

students = []

# LOAD DATA WITH ERROR HANDLING
def load_data():
    global students
    students = []

    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    student = {
                        "Name": row["Name"],
                        "Math": int(row["Math"]),
                        "Science": int(row["Science"]),
                        "English": int(row["English"])
                    }

                    # Calculate average
                    avg = (student["Math"] + student["Science"] + student["English"]) / 3
                    student["Average"] = round(avg, 2)

                    students.append(student)

                except:
                    print("⚠️ Skipping invalid row:", row)

    except FileNotFoundError:
        print("❌ students.csv file not found!")

# GRADE FUNCTION
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

# SHOW DATA
def show_data():
    print("\n📊 Student Data:\n")
    for s in students:
        print(f"{s['Name']} → Avg: {s['Average']}")

# BAR GRAPH
def show_bar_graph():
    names = [s["Name"] for s in students]
    averages = [s["Average"] for s in students]

    plt.bar(names, averages)
    plt.title("Student Average Marks")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.show()

# PIE CHART
def show_pie_chart():
    grades = [get_grade(s["Average"]) for s in students]
    grade_count = Counter(grades)

    plt.pie(grade_count.values(), labels=grade_count.keys(), autopct='%1.1f%%')
    plt.title("Grade Distribution")
    plt.show()

# TOPPER
def show_topper():
    topper = max(students, key=lambda x: x["Average"])
    print(f"\n🏆 Topper: {topper['Name']} ({topper['Average']})")

# MENU
def menu():
    while True:
        print("\n==== Student Dashboard ====")
        print("1. Show Data")
        print("2. Show Bar Graph")
        print("3. Show Pie Chart")
        print("4. Show Topper")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_data()
        elif choice == "2":
            show_bar_graph()
        elif choice == "3":
            show_pie_chart()
        elif choice == "4":
            show_topper()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

# RUN PROGRAM
load_data()

if students:
    menu()