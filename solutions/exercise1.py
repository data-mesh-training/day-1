import csv
from datetime import date

dataset = []
with open('generated_data1.csv', newline='\n') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',', quotechar='\\')
  for row in csvreader:
    dataset += [row]

sales_count_june = 0
for order_position in dataset:
  order_date = order_position[2]
  if '2023-06-01' <= order_date <= '2023-06-30':
    sales_count_june += 1

print("---------sales counts june---------")
print(sales_count_june)

#revenue in germany in july 2023
from decimal import Decimal

revenue_germany_july = Decimal(0.0)
for order_position in dataset:
  order_date = order_position[2]
  country = order_position[3]
  discounted_price = Decimal(order_position[5])
  if '2023-07-01' <= order_date <= '2023-07-31' and country == 'DE':
    revenue_germany_july += discounted_price
  if order_date == "null":
    for order_lookup in dataset:
      if order_lookup[0] == order_position[0] and '2023-07-01' <= order_lookup[2] <= '2023-07-31':
        revenue_germany_july += discounted_price
        break

print("---------revenue germany july---------")
print(revenue_germany_july)

# average order value
from decimal import Decimal

order_id_tracker = set()
order_counter_august = 0
total_order_value_august = Decimal(0.0)
for order_position in dataset:
  order_id = order_position[0]
  order_date = order_position[2]
  discounted_price = Decimal(order_position[5])
  if '2023-08-01' <= order_date <= '2023-08-31':
    total_order_value_august += discounted_price
    if order_id not in order_id_tracker:
      order_id_tracker.add(order_id)
      order_counter_august += 1
  if order_date == "null":
    for order_lookup in dataset:
      if order_lookup[0] == order_position[0] and '2023-08-01' <= order_lookup[2] <= '2023-08-31':
        total_order_value_august += discounted_price
        if order_id not in order_id_tracker:
          order_id_tracker.add(order_id)
          order_counter_august += 1
        break

average_order_value = round(total_order_value_august / order_counter_august, 2)

print("---------average order value august---------")
print(average_order_value)

