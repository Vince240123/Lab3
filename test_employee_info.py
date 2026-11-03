import employee_info

def test_get_employees_by_age_range():
    expected = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]

    result = employee_info.get_employees_by_age_range(24, 33)

    assert (result == expected)


def test_get_employees_by_age_range_none():
    expected = []

    result = employee_info.get_employees_by_age_range(50, 60)

    assert (result == expected)


def test_calculate_average_salary():
    expected = 361000 / 6   # 60166.67

    result = employee_info.calculate_average_salary()

    assert result == expected


def test_get_employees_by_dept():
    expected = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]

    result = employee_info.get_employees_by_dept("Marketing")

    assert (result == expected)


def test_get_employees_by_dept_not_found():
    expected = []

    result = employee_info.get_employees_by_dept("HR")

    assert (result == expected)