class BMI():
    def __init__(self, name:str, height:float, weight:float):
        self.name = name
        self.height = height
        self.weight = weight

    def getName(self)->str:
        return self.name
    
    def getBMI(self)->float:
        return round(self.weight / ((self.height * 0.01) ** 2), ndigits=2)
    
    def get_status_message(self)->str:
        self.bmi = self.getBMI()
        
        if self.bmi < 18.5:
            return "體重過輕"
        elif self.bmi < 24:
            return "正常範圍"
        elif self.bmi < 27:
            return "過重"
        elif self.bmi < 30:
            return "輕度肥胖"
        elif self.bmi < 35:
            return "中度肥胖"
        else:
            return "重度肥胖"

while True:
    try:
        name = input("請輸入姓名: ")
        height = float(input('請輸入身高（cm）: '))
        weight = float(input('請輸入體重（kg）: '))
        
        #這裏建立一個BMI的實體
        myBMI = BMI(name=name, height=height, weight=weight)
        print(f"{myBMI.getName()} 的 BMI 為{myBMI.getBMI()}, 為{myBMI.get_status_message()}")
    except ValueError:
        print("格式錯誤，請重新輸入數據")
        continue

    stuff = input("請問是否繼續輸入資料 ('q': 離開, 任意鍵: 繼續)? ")

    if stuff == 'q':
        break

print("應用程式結束")