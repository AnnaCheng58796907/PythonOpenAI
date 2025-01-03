class BMI:
    def __init__(self, name:str, height:float, weight:float):
        self.name = name
        self.height = height
        self.weight = weight


    def get_BMI(self)->float:
        return round(self.weight/((self.height/100)**2), 2)

    def get_status(self, bmi:float) -> str:
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


def main():
    while(True):
        try:
            name = input("姓名:")
            height = float(input("請輸入身高(公分):"))
            weight = float(input("請輸入體重(公斤):"))
            p1 = BMI(name=name,height=height,weight=weight)   
            break
        except Exception:
            print('輸入格式錯誤,請重新輸入!')

    bmi = p1.get_BMI()
        
    print(f"{name}的BMI值是{bmi}\n您的體重{p1.get_status(bmi)}")
    print("程式結束")

if __name__ == '__main__':
    main()