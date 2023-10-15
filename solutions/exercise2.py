
#-------------------------------------------------------------------------------
#------------------------- Loadt updated "new" dataset -------------------------
#-------------------------------------------------------------------------------

import csv
from datetime import date

new_dataset = []
with open('generated_data2.csv', newline='\n') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',', quotechar='\\')
  for row in csvreader:
    new_dataset += [row]

#-------------------------------------------------------------------------------
#------------------------- Number of sold items in June ------------------------
#-------------------------------------------------------------------------------

sold_items_june = 0
for new_order_position in new_dataset:
  order_date = new_order_position[2]
  if '2023-06-01' <= order_date <= '2023-06-30':
    sold_items_june += 1

print("---------sold items june---------")
print(sold_items_june)

#-------------------------------------------------------------------------------
#-------------------------- Revenue in Germany in July -------------------------
#-------------------------------------------------------------------------------

from decimal import Decimal

revenue_germany_july = Decimal(0.0)
for new_order_position in new_dataset:
  order_date = new_order_position[2]
  country = new_order_position[3]
  sales_price = Decimal(new_order_position[4])
  if '2023-07-01' <= order_date <= '2023-07-31' and country == 'DACH_DE':
    revenue_germany_july += sales_price
# "DateFix" no longer works

print("---------revenue germany july---------")
print(revenue_germany_july)

#-------------------------------------------------------------------------------
#------------------------ Average order value in August ------------------------
#-------------------------------------------------------------------------------

from decimal import Decimal

order_id_tracker = set()
order_counter_august = 0
total_order_value_august = Decimal(0.0)
for new_order_position in new_dataset:
  order_id = new_order_position[0]
  order_date = new_order_position[2]
  discounted_price = Decimal(new_order_position[4])
  if '2023-08-01' <= order_date <= '2023-08-31':
    total_order_value_august += discounted_price
    if order_id[:-1] not in order_id_tracker:
      order_id_tracker.add(order_id[:-1])
      order_counter_august += 1
# "DateFix" no longer works

average_order_value = round(total_order_value_august / order_counter_august, 2)

print("---------average order value august---------")
print(average_order_value)