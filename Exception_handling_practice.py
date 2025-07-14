class UserDefined(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

class Exceptions:
    def userdefined_exception(self):
        print("Entered into function")
        try :
            print("In the try block, catchin user defined exception now.")
            raise UserDefined("This is user defined exception")
        
        except UserDefined as e:
            print("User defined exception is caught")
        
        finally:
            print("Finally block is executed")

exp = Exceptions()
exp.userdefined_exception()

