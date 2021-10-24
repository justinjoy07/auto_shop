class Car:
    def __init__(self, speed, regular_price, color):
            self.speed = speed
            self.regular_price = regular_price
            self.color = color

    def __str__(self):
        return f"Car: Speed={self.speed} Regular Price={self.regular_price} Color={self.color}"

    def get_sale_price(self):
        print(self)
        print(f"Sale Price: {self.regular_price}\n")


class Truck(Car):
    def __init__(self, speed, regular_price, color, weight):
        self.weight = weight
        Car.__init__(self, speed, regular_price, color)

    def __str__(self):
        return f"Truck: Speed={self.speed} Regular Price={self.regular_price} Color={self.color} Weight={self.weight}"
    
    def get_sale_price(self):
        print(self)
        if self.weight > 2000:
            result = f"Sale Price: {self.regular_price * 0.90}\n"
        else:
            result = f"Sale Price: {self.regular_price * 0.80}\n"
        print(result)


class Tata(Car):
    def __init__(self, speed, regular_price, color, year, manufacturer_discount):
        self.year = year
        self.manufacturer_discount = manufacturer_discount
        Car.__init__(self, speed, regular_price, color)

    def __str__(self):
        return f"Tata: Speed={self.speed} Regular Price={self.regular_price} Color={self.color}, Year={self.year}, Manufacturer Discount={self.manufacturer_discount}"

    def get_sale_price(self):
        print(self)
        return print(f"Sale Price: {self.regular_price - self.manufacturer_discount}\n")


class Sedan(Car):
    def __init__(self, speed, regular_price, color, length):
        self.length = length
        Car.__init__(self, speed, regular_price, color)
    
    def __str__(self):
        return f"Sedan: Speed={self.speed} Regular Price={self.regular_price} Color={self.color}, Length={self.length}"

    def get_sale_price(self):
        print(self)
        if self.length > 20:
            result = f"Sale Price: {self.regular_price * 0.95}\n"
        else:
            result = f"Sale Price: {self.regular_price * 0.90}\n"
        print(result)


class MyOwnAutoShop:
    def main(self):
        car_obj = Car(220, 15000, "Pink")
        sedan_obj = Sedan(250, 10000, "Blue", 25)
        tata_obj = Tata(200, 20000, "Red", 2010, 5000)
        truck_obj = Truck(150, 3000, "Yellow", 2001)
        car_obj.get_sale_price()
        sedan_obj.get_sale_price()
        tata_obj.get_sale_price()
        truck_obj.get_sale_price()


if __name__ == '__main__':
    MyOwnAutoShop().main()
