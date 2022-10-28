money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

money = money_capital + salary - spend
while money >= spend:
    money = money + salary - spend - (spend * increase)
    month +=1


print(month)

