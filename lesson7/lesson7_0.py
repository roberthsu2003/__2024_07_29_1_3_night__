#計算完成後,問使用者還要繼續('q':離開,enter:繼續)嗎?


while True:
    try:
        name=str(input("請輸入姓名"))
        height=float(input('請輸入身高'))
        weight=float(input('請輸入體重'))
        bmi=weight/(((height*0.01))**2)
        if bmi<18.5:
            grade="體重過輕"
        elif bmi<24:
            grade="正常範圍"
        elif bmi<27:
            grade="過重"
        elif bmi<30:
            grade="輕度肥胖"
        elif bmi<35:
            grade="中度肥胖"
        elif bmi>=35:
            grade="重度肥胖"
        print(f"{name} 的 bmi 為 {bmi},為{grade}")
    except ValueError:
        print("格式錯誤")
        continue
    stuff = input("請問是否繼續輸入資料 ('q':離開,任意鍵:繼續)?")

    if stuff == 'q':
        break
    

print("應用程式結束")