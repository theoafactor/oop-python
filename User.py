class User():

    def __init__(self):
        print("works")

    def register(self):
        errors = []
        firstname = input("Enter firstname: ")
        lastname = input("Enter lastname: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
            
        if len(firstname.strip()) == 0:
            #print("Firstname not entered")
            errors.append("Firstname not entered")

        if len(lastname.strip()) == 0:
            #print("Lastname not entered")
            errors.append("Lastname not entered")
        if len(email.strip()) == 0:
            #print("Email not entered")
            errors.append("Email not entered")
        if len(password.strip()) == 0:
            #print("Password not entered")
            errors.append("Password not entered")

        if len(errors) > 0:
            ## there is/are error(s)
            print(errors)
            return False
        else:
            self.firstname = firstname
            self.lastname = lastname
            self.email = email
            self.password = password
            print("User registered successfully")
            return True
    

    def login(self, email, password):
        pass

    def getUsername(self, email):
        pass

person = User()

person2 = User()

#person.register()

print(type(person))



