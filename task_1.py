class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        print("Setting value...")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)

class Descriptor:
    def __get__(self, instance, owner):
        print(f"Getting value of {self} in {instance} of {owner}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"Setting value of {self} in {instance} to {value}")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    attr1 = Descriptor()
    attr2 = Descriptor()

'''
    В этом примере мы создаем класс Celsius, который имеет свойство temperature для получения и установки температуры. 
    Мы также создаем класс Descriptor, который является базовым классом для создания дескрипторов. Дескрипторы attr1 и attr2 создаются в классе MyClass, 
    который является примером использования дескрипторов.
    Когда мы устанавливаем значение атрибута attr1 или attr2 в объекте класса MyClass, соответствующий метод __set__ дескриптора будет вызван, 
    и значение будет установлено в словарь экземпляра объекта. Когда мы читаем значение атрибута attr1 или attr2 в объекте класса MyClass, 
    соответствующий метод __get__ дескриптора будет вызван, и значение будет извлечено из словаря экземпляра объекта.
'''