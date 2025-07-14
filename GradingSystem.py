def show_history() -> None:
    print("\n=== Brief History of Python ===")
    print("Created in the year 1991")
    print("Python 3 released in the year 2008")
    print("\n*** Program that Computes the Average Score of Students ***")

    def get_names_score() -> tuple[list[str], list[float]]:
        while True:
            try:
                count = int(input("Number of students: "))
                if count <= 0:
                    print("Please enter a number greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        names_of_students = []
        scores = []
        print("\nEnter student names and their scores:")

        for i in range(count):
            name = input(f'Student {i + 1} name: ').strip()
            if not name:
                name = f'Student_{i+1}'
            names_of_students.append(name)

            while True:
                try:
                    score = float(input(f"Enter the score for {name}: "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        return names_of_students, scores

    names, scores = get_names_score()
    average = sum(scores) / len(scores)
    print(f"\nAverage score: {average:.2f}")

# Call the function to run the program
show_history()
