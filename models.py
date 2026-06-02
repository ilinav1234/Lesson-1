class Car:
    def __init__(self, brand, model, year, price, quantity):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модел: {self.model}")
        print(f"Година: {self.year}")
        print(f"Цена: {self.price} €.")
        print(f"Налични бройки: {self.quantity}")

    def sell_car(self):
        if self.quantity > 0:
            self.quantity -= 1
            print("Автомобилът беше продаден успешно.")
            return True
        else:
            print("Няма налични бройки от този автомобил.")
            return False

    def change_price(self, new_price):
        self.price = new_price
        print("Цената беше променена успешно.")


class AutoSalon:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print("Автомобилът беше добавен успешно.")

    def show_all_cars(self):
        if len(self.cars) == 0:
            print("В автосалона няма автомобили.")
        else:
            for number, car in enumerate(self.cars, start=1):
                print(f"\nАвтомобил номер {number}:")
                car.show_info()

    def search_car(self, model):
        for car in self.cars:
            if car.model.lower() == model.lower():
                return car
        return None

    def sort_cars_by_price(self):
        self.cars.sort(key=lambda car: car.price)
        print("Автомобилите бяха сортирани по цена.")