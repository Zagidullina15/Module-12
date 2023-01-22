tickets = int(input("Введите количество билетов, которое хотите приобрести:"))#Введите количество билетов
age = [int(input('Введите возраст каждого посетителя:')) for i in range(tickets)] #Вводим возраст для каждого билета
prise = []
for i in age:
    if i in range(0, 18):
        prise.append(0)
    elif i in range(18, 25):
        prise.append(990)
    else:
        prise.append(1390)
print(prise)
if tickets > 3:
    print("Сумма с учетом скидки составит:", sum(prise) - (sum(prise)*10/100), "рублей")
else:
    print("Сумма к оплате:",sum(prise))