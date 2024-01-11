class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, code, name, price):
        self.products[code] = {'name': name, 'price': price}

    def display_menu(self):
        print("Menu:")
        print("Code\tName\tPrice")
        for code, product in self.products.items():
            print(f"{code}\t{product['name']}\t₹{product['price']}")

    def generate_bill(self, order):
        total_amount = 0
        print("\n------------------ RECEIPT ------------------")
        print("Code\tName\tPrice\tQuantity\tTotal")
        for code, quantity in order.items():
            product = self.products[code]
            item_total = quantity * product['price']
            total_amount += item_total
            print(f"{code}\t{product['name']}\t₹{product['price']}\t{quantity}\t\t₹{item_total}")

        print("\nTotal Amount: ₹{:.2f}\n".format(total_amount))


def main():
    store = Store()

    store.add_product('001', 'Bread', 25.00)
    store.add_product('002', 'Chips', 15.00)
    store.add_product('003', 'KitKat', 10.00)
    store.add_product('004', 'Coke', 20.00)
    store.add_product('005', 'Biscuit', 12.00)
    store.add_product('006', 'Butter', 35.00)
    store.add_product('007', 'Rice', 30.00)
    store.add_product('008', 'Lentils', 35.00)
    store.add_product('009', 'Suji', 40.00)
    store.add_product('010', 'Spice', 20.00)

    store.display_menu()

    order = {}
    while True:
        code = input("Enter the product code (or 'done' to finish): ")
        if code.lower() == 'done':
            break
        elif code in store.products:
            quantity = int(input(f"Enter the quantity for {store.products[code]['name']}: "))
            order[code] = quantity
        else:
            print("Invalid product code. Please enter a valid code.")

    store.generate_bill(order)


if __name__ == "__main__":
    main()
