class Myclass:

    def instance_metthod(self):
        print("Called instance method")

    @classmethod
    def class_method(cls):
        print("Called class method")

    @staticmethod
    def static_method():
        print("Called static method")


obj1 = Myclass()

obj1.instance_metthod()
Myclass.class_method()
Myclass.static_method()