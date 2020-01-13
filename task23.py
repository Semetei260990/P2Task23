def leap_year(year):

    if year % 4 == 0:
        print(str(year) + "Год високосный! ")
    else:
        print(str(year) + "Год обычный! ")
year_ = int(input("Введите год: "))   
leap_year(year_)