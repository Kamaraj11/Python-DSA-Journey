class Parent:
    def __init__(self):
        self.public_var="Public"
        self._procted_var="Procted"
        self.__private_var="Private"

    def access_from_same_class(self):
        print("Inside Parent Class:")
        print("Public:",self.public_var)
        print("procted:",self._procted_var)
        print("private:",self.__private_var)


class child(Parent):
    def access_from_subclass(self):
        print("public:",self.public_var)
        print("procted:",self._procted_var)
        try:
            print("private:",self.__private_var)
        except AttributeError:
            print("private: cannot access(AttributeError)")





obj1=Parent()
print("Acess from same class")
obj1.access_from_same_class()


obj2=child()

print("This is sub class")
obj2.access_from_subclass()
