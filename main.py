from models import Car, AutoSalon


def main():
    salon = AutoSalon()


    users = {
        "admin": "1234",
        "student": "1111"
    }


    sold_cars = {
        "admin": [],
        "student": []
    }

    
    car1 = Car("BMW", "320d", 2018, 35000, 2)
    car2 = Car("Mercedes", "C220", 2019, 42000, 1)
    car3 = Car("Volkswagen", "Golf 7", 2017, 23000, 3)

    salon.add_car(car1)
    salon.add_car(car2)
    salon.add_car(car3)

    print("\nДобре дошли в системата на автосалона!")

    username = input("Въведете потребителско име: ")
    password = input("Въведете парола: ")

    if username not in users or users[username] != password:
        print("Грешно потребителско име или парола.")
        return

    print("Успешен вход в системата.")

    while True:
        print("\n===== МЕНЮ АВТОСАЛОН =====")
        print("1. Покажи всички автомобили")
        print("2. Добави нов автомобил")
        print("3. Потърси автомобил по модел")
        print("4. Продай автомобил")
        print("5. Промени цена на автомобил")
        print("6. Сортирай автомобили по цена")
        print("7. Покажи продадени автомобили")
        print("0. Изход")

        choice = input("Изберете опция: ")

        if choice == "1":
            salon.show_all_cars()

        elif choice == "2":
            brand = input("Въведете марка: ")
            model = input("Въведете модел: ")

            try:
                year = int(input("Въведете година: "))
                price = float(input("Въведете цена: "))
                quantity = int(input("Въведете брой автомобили: "))

                new_car = Car(brand, model, year, price, quantity)
                salon.add_car(new_car)

            except ValueError:
                print("Грешка! Годината, цената и броят трябва да бъдат числа.")

        elif choice == "3":
            model = input("Въведете модел за търсене: ")
            found_car = salon.search_car(model)

            if found_car is not None:
                print("\nАвтомобилът е намерен:")
                found_car.show_info()
            else:
                print("Автомобилът не е намерен.")

        elif choice == "4":
            model = input("Въведете модел на автомобила за продажба: ")
            found_car = salon.search_car(model)

            if found_car is not None:
                success = found_car.sell_car()

                if success:
                    sold_cars[username].append(found_car.brand + " " + found_car.model)
            else:
                print("Няма такъв автомобил в автосалона.")

        elif choice == "5":
            model = input("Въведете модел на автомобила: ")
            found_car = salon.search_car(model)

            if found_car is not None:
                try:
                    new_price = float(input("Въведете нова цена: "))
                    found_car.change_price(new_price)
                except ValueError:
                    print("Грешка! Цената трябва да бъде число.")
            else:
                print("Няма такъв автомобил.")

        elif choice == "6":
            salon.sort_cars_by_price()

        elif choice == "7":
            if len(sold_cars[username]) == 0:
                print("Няма продадени автомобили.")
            else:
                print("Продадени автомобили:")
                for car_name in sold_cars[username]:
                    print("-", car_name)

        elif choice == "0":
            print("Изход от програмата.")
            break

        else:
            print("Невалидна опция. Опитайте отново.")


main()