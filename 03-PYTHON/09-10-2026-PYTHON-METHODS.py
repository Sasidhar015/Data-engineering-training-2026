class product:
  name = ""
  price = 0
  date_of_expiry = 0

  def display(self):
    print(f"product: {self.name}")
    print(f"price: {self.price}")

p1 = product()

p1.name = "moni"
p1.price = 899

p1.display()





class product:
    name = ""
    price = 0
    quantity = 0

    def tot_amount(self):
        return self.price*self.quantity




p1 =product()

p1.name = "moni"
p1.price = 899
p1.quantity=7

print(p1.tot_amount())
