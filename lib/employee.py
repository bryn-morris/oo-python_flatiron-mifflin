
class Employee:

    all = []
    
    def __init__(self, name, salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager
        self.manager_name = manager.name

        Employee.all.append(self)

    @classmethod    
    def paid_over(cls, salary_number):

        # test this refactor

        return [em for em in cls.all if em.salary > salary_number]

        # salary_list = []

        # for employee in cls.all:
        #     if employee.salary > salary_number:
        #         salary_list.append(employee)

        # return salary_list
    
    @classmethod
    def find_by_department(cls, dept_string):

        employee_by_dept_list = []

        for employee in cls.all:
            if employee.manager.department == dept_string:
                employee_by_dept_list.append(employee)
        
        return employee_by_dept_list[0]
    
    def get_tax_bracket(self):

        tax_bracket_list = []
        
        for em in Employee.all:
             if em.salary-1000 <= self.salary <= em.salary+1000:
                 tax_bracket_list.append(em)

        return tax_bracket_list
    
    tax_bracket = property(get_tax_bracket)

                    