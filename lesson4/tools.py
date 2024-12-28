PI = 3.1415962


class Person:
    def __init__(self, name:str, age:int):
        #建立attribute
        self.name = name
        self.age = age


    #實體方法(instance method)
    def echo(self):
        print(f'我的姓名是{self.name}')
        print(f'我的年齡是{self.age}')


class Student(Person):
    def __init__(self,name:str, age:int, score:int):
        super().__init__(name=name, age=age)#呼叫父Person的__init__
        self.__score = score

    
    #property在執行時不用()
    @property
    def score(self)->int:
        return self.__score

    def echo(self):
        super().echo()
        print(f'我的分數是{self.score}')


def get_status(bmi: float) -> str:

    if bmi >= 35:
        bmi_str = '重度肥胖'
    elif bmi >= 30:
        bmi_str = '中度肥胖'
    elif bmi >= 27:
        bmi_str = '輕度肥胖'
    elif bmi >= 24:
        bmi_str = '過重'
    elif bmi >= 18.5:
        bmi_str = '正常範圍'
    else:
        bmi_str = '過輕'
    return bmi_str


def BMI_math(height_cm: float, weight_kg: float) -> tuple[float, str]:
    height_m = round(height_cm/100, 2)
    bmi_kg_m2 = round(weight_kg/(height_m**2), 2)
    bmi_str = get_status(bmi_kg_m2)
    return bmi_kg_m2, bmi_str
