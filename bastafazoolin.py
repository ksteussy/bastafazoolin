import datetime

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + " will be served between " + str(self.start_time) + " and " + str(self.end_time)

  def calculate_bill(self, purchased_items):
    self.purchased_items = purchased_items
    total = 0
    for item in self.purchased_items:
      total += self.items[item]
    return total

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if menu.start_time <= datetime.time(time) and menu.end_time >= datetime.time(time):
        available.append(menu)
    return available

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


brunch = Menu('Brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, datetime.time(11), datetime.time(4))

early_bird = Menu('Early-Bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, datetime.time(15), datetime.time(18))

dinner = Menu('Dinner', {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, datetime.time(17), datetime.time(23))

kids = Menu('Kids', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, datetime.time(11), datetime.time(21))

arepas_menu = Menu('Take a\' Arepa', {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, datetime.time(10), datetime.time(20))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

takeaarepa = Business("Take a' Arepa", [arepas_place])

#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(dinner)
#print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
#print(kids)
#print(arepas_place)
#print(flagship_store.available_menus(12))
#print(new_installment.available_menus(17))

