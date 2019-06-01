def normalize_employees(employees):
    normalized_employees = []
    for employee in employees:
        data = {}
        for field in employee:
            data[field] = employee[field]
        normalized_employees.append(data)
    return normalized_employees