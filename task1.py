import re

def total_salary(path: str) -> tuple[int, float] | None:

    employees_and_salaries = dict[str, int]()
    salary_entries = list[str]()
    regex_pattern = r".+,\d+"  # Entry pattern

    try:
        with open(path) as file:
            file_content = file.read()
            salary_entries = re.findall(regex_pattern, file_content)
    except FileNotFoundError:
        print("File not found!")
        return None

    if len(salary_entries) == 0:
        print("No salary entries found in file! Check file format and try again.")
        return None

    for salary_entry in salary_entries:
        name_and_salary = salary_entry.split(",")
        employee_name = name_and_salary[0]
        employee_salary = int(name_and_salary[1])
        employees_and_salaries.update({employee_name: employee_salary})

    salaries_sum = 0

    for employee_name, salary in employees_and_salaries.items():
        salaries_sum += salary

    average_salary = salaries_sum / len(employees_and_salaries)
    return salaries_sum, average_salary

