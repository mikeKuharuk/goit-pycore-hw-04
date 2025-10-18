import Task1
import Task2

while True:
    print("\nWhat would you like to do?"
          "\n0. Exit"
          "\n1. Calculate salaries"
          "\n2. Get Cat data"
          "\n4. Open Bot assistant\n")
    choice = input("Enter your choice: ")

    if choice == "0":
        break

    elif choice == "1":
        print("Please provide Salaries files destination, or type 'default' to use the default salaries")
        path = input("Enter path: ")

        if path == "default":
            path = "Files/Salaries.txt"

        total_and_average_salary = Task1.total_salary(path)

        if total_and_average_salary is None:
            print("Function did not return any data")
        else:
            print(f"Total Salaries: {total_and_average_salary[0]},\nAverage Salaries: {total_and_average_salary[1]}")

    elif choice == "2":
        print("Input path to cats data file or type 'default' to use the default cats data")
        path = input("Enter path: ")
        if path == "default":
            path = "Files/CatsInfo.txt"

        cats_info = Task2.get_cats_info(path)
        if cats_info is None:
            print("Function did not return any data")
        else:
            print(f"Cat info:\n {cats_info}")

    elif choice == "4":
        continue

    else:
        print("Invalid choice, please try again!")

