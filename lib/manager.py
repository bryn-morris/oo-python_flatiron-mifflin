from lib.employee import Employee

class Manager:

    all = []
    all_departments = []
    new_employee_counter = 5
    age_list = []

    #need to be able to call this AFTER classes are instantiated so can't be
    # class attribute or it needs to update when we call it such as 
    # with a getter
    # average_age = (0 if age_list == [] else sum(age_list)/len(age_list))
    
    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
        self.employee_list = []
        Manager.all.append(self)
        Manager.age_list.append(age)

        if self.department not in Manager.all_departments:
            Manager.all_departments.append(self.department)

    def get_employees(self):

        # test list comprehension once employees are built out
        # return [em for em in Employee if em.manager_name == self]

        for employee in Employee.all:
            if employee.manager_name == self.name and employee not in self.employee_list:
                self.employee_list.append(employee)

        return self.employee_list
    
    def hire_employee(self, employee_name, employee_salary):
        
        #Still need to concatenate number with new_em variable

        for new_em in range(Manager.new_employee_counter, Manager.new_employee_counter + 1):    
            new_em = Employee(employee_name, employee_salary, self)
            self.employee_list.append(new_em)

        Manager.new_employee_counter += 1
    
    @classmethod
    def get_average_age(cls):
        return sum(cls.age_list)/len(cls.age_list)


    # Only returning Property Object instead of Expected value,
    # having some issue with using property on class method
    # average_age = property(get_average_age)
    employees = property(get_employees)
