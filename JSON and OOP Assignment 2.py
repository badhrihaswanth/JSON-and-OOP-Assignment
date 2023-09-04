indian_states_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Kerala": "Thiruvananthapuram",
    "Uttar Pradesh": "Lucknow",
    "Bihar": "Patna"
}

with open('indian_states.json', 'w') as json_file:
    json.dump(indian_states_capitals, json_file)

employee_list = []
with open('employee.json', 'r') as json_file:
    employee_data = json.load(json_file)
    for employee_info in employee_data:
        employee = Employee(
            employee_info['Name'],
            employee_info['DOB'],
            employee_info['Height'],
            employee_info['City'],
            employee_info['State']
        )
        employee_list.append(employee)
        
for employee in employee_list:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")
