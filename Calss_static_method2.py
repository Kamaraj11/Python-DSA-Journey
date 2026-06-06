class Employee:
    company_name="OpenAI"

    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name

Employee.change_company("Microsoft")
print(Employee.company_name)