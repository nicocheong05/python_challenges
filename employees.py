class Employee:
    def __init__(self, firstName, lastName, empID):
        self.__FirstName = firstName                      # string
        self.__LastName = lastName                        # string
        self.__FullName = firstName + " " + lastName      # string
        self.__Email = firstName.lower() + "." + lastName.lower() + "@company.com"
        self.__EmployeeID = empID

    def GetEmployeeEmail(self):
        return self.__Email

    def PrintDetails(self):
        return self.__FullName, self.__Email


Employees = []

try:
    f = open("emailList.txt", "r")
    while True:
        fname = f.readline().strip()
        if fname == "":
            break
        lname = f.readline().strip()
        id = f.readline().strip()
        Employees.append(Employee(fname, lname, id))
    f.close()
except FileNotFoundError:
    print("Sorry file not found.")


for i in range(len(Employees)):
    print(Employee.PrintDetails(Employees[i]))