def details():
        try:
            name=input("Enter the Name: \n" )
            age=int(input("Enter the age: \n"))
            if age == 0:
                raise Exception
            gender=input("enter the gender: \n")
            if gender != "male" or gender != "female":
                raise Exception
            salary=input("enter the salary: \n")
            state=input("enter the state: \n")
            city=input("enter the city: \n")
            print("Name: {}\nAge: {}\n Gender: {}\n Salary: {}\n State: {}\n City: {}\n" .format(name, age, gender,salary,state,city))

        except:
            print("Age cannot be zero")
            print("Specify the gender correctly")
details()
