a=input("Введите целое число для определения его чётности/нечётности") #запрос от пользователя числа и присваивание числа в переменную a
a=int(a) #изменение типа данных str в int
i=a%2 #переменная, в которой присваивается остаток
if i==0 :
    print(f"Число {a} является чётным. ") 
else :
    print(f"Число {a} является нечётным. ") 
