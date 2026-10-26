# Mini Project (W3): Billing System (OOP-Based)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=18):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        return sum(product.calculate_total()
                   for product in self.products)

    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate / 100

    def calculate_grand_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        print("\n" + "=" * 72)
        print("                         CUSTOMER BILL")
        print("=" * 72)

        print(f"{'Product':<25}{'Price':>12}{'Quantity':>12}"
              f"{'Total':>15}")
        print("-" * 72)

        for product in self.products:
            total = product.calculate_total()
            print(f"{product.name:<25}"
                  f"Rs. {product.price:>7.2f}"
                  f"{product.quantity:>12}"
                  f"Rs. {total:>10.2f}")

        print("-" * 72)
        print(f"{'Subtotal:':>49} Rs. {self.calculate_subtotal():>10.2f}")
        print(f"{'Tax (' + str(self.tax_rate) + '%):':>49} "
              f"Rs. {self.calculate_tax():>10.2f}")
        print("-" * 72)
        print(f"{'Grand Total:':>49} "
              f"Rs. {self.calculate_grand_total():>10.2f}")
        print("=" * 72)
        print("             Thank you for shopping!")
        print("=" * 72)


# Main program
bill = Bill(tax_rate=18)

product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 500, 2)
product3 = Product("Keyboard", 1200, 1)

bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)

bill.display_bill()
