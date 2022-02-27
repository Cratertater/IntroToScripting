# Jake Million
# 2/22/22
# Employee Dictionary
emp = {'47899': {'name': 'Susan Meyers', 'department': 'Accounting', 'title': 'Vice President'},
       '39119': {'name': 'Mark Jones', 'department': 'IT', 'title': 'Programmer'},
       '81774': {'name':  'Joy Rogers', 'department': 'Manufacturing', 'title': 'Engineer'}}

# Print Menu and get input
ui = input(print("[1] Look up Employee   [2] Add new Employee\n[3] Change Employee information   [4] Delete Employee\n"
                 "[5] Quit"))
while ui != "5":
    # Looking employee up
    if ui == "1":
        ui2 = input(print("Enter an employee ID: "))
        if ui2 in emp:
            print(emp[ui2])
            # printing menu again
            print("\n\n[1] Look up Employee   [2]Add new Employee\n[3] Change Employee info  [4] Delete Employee")
            print("[5] Quit")
            ui = input()
    # Adding a new employee
    elif ui == "2":
        nEmp = input(print("enter new employee id: "))
        nEmpInfo = input(print("Enter new employee information: "))
        emp[nEmp] = nEmpInfo
        print("\n\n[1] Look up Employee   [2]Add new Employee\n[3] Change Employee info  [4] Delete Employee")
        print("[5] Quit")
        ui = input()
    # Changing employee info
    elif ui == "3":
        up = input(print("Enter employee id to update: "))
        upInfo = input(print("Enter the updated info: "))
        emp.update(upInfo)
        print("\n\n[1] Look up Employee   [2]Add new Employee\n[3] Change Employee info  [4] Delete Employee")
        print("[5] Quit")
        ui = input()
    # Delete Employee
    elif ui == "4":
        delete = input(print("Enter the employee you wish to delete: "))
        del emp[delete]
        print("\n\n[1] Look up Employee   [2]Add new Employee\n[3] Change Employee info  [4] Delete Employee")
        print("[5] Quit")
        ui = input()
    # if user enters 5
    else:
        print("End of program.")
        break
