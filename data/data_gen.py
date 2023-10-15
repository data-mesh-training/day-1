import random
import decimal
import datetime
import csv

#-------------------------------------------------------------------------------
#-------------------- section to generate order constants --------------------
#-------------------------------------------------------------------------------

# countries of order placement
COUNTRIES = ["DE", "AT", "CH", "BE", "NL", "FR", "EN", "DK", "FI", "IT", "PL", "PT", "ES", "SE", "NO"]

# earliest orders are from 2023-06-01
START_DATE = datetime.date(2023, 6, 1)

# add random weights to the number of items bought per order
LINE_NUMBER_COUNT_WEIGHTS = [0]*1 + [1]*30 + [2]*30 + [3]*20 + [4]*15 + [5]*4

# add random discounts between 0 and 50% to each ordered item
DISCOUNT_WEIGHTS = [1]*50 + [0.95]*20 + [0.90]*15 + [0.80]*10 + [0.50]*5

# fix random prices for 100 articles
PRICES = {}
for x in range(100):
  PRICES[x] = random.randrange(500, 5000)/100

#-------------------------------------------------------------------------------
#-------------------- section for generating order positions -------------------
#-------------------------------------------------------------------------------

# random original prices between 5.00 and 50.00
def generate_original_price():
  return random.randrange(500, 5000)/100

#dates can be randomly empty in 5% of the cases to simulate a source data quality issue
def get_final_order_date(order_date):
  empty_group_weight = [0]*1 + [1]*19
  if (random.choice(empty_group_weight) == 0):
    return "null"
  else:
    return order_date

#non-empty order line
def generate_order_line(order_id, line_number, order_date, country):
  final_order_date = get_final_order_date(order_date) # random date between 2023-06-01 and 2023-08-31, can be empty in 5% cases
  original_price = random.choice(PRICES) # random original prices between 5.00 and 50.00
  discounted_price = round(original_price*random.choice(DISCOUNT_WEIGHTS),2) # actual price factoring in a random discount
  earnings_after_taxes = round(discounted_price*0.81, 2) # earnings after deducting 19% taxes
  order_line = [[
    str(order_id),
    str(line_number),
    str(final_order_date),
    country,
    str(original_price),
    str(discounted_price),
    str(earnings_after_taxes)]]
  return order_line

def generate_orders(number_of_orders):
  order_positions = []
  for order_id in range(1, number_of_orders+1):
    line_numbers = random.choice(LINE_NUMBER_COUNT_WEIGHTS) # randomly select between 0 and 5 items per order. Orders can be empty!
    if line_numbers == 0: # handling of empty orders
      order_positions += [[str(order_id), "", "", "", "0.00", "0.00", "0.00"]]
    else:
      order_date = START_DATE + datetime.timedelta(random.randint(0,91)) # random date between 2023-06-01 and 2023-08-31
      country = random.choice(COUNTRIES) # randomly selected country of order placement
      for line_number in range(1, line_numbers+1):
        order_positions += generate_order_line(order_id, line_number, order_date, country)
  return order_positions

#-------------------------------------------------------------------------------
#------------- section for executing data generation and persisting ------------
#-------------------------------------------------------------------------------
number_of_orders = 10000
records = generate_orders(number_of_orders)
#for x in records: print(x)

with open('generated_data1.csv', 'w', newline='\n') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=',',
              quotechar='\\', quoting=csv.QUOTE_MINIMAL)
  for record in records:
    csvwriter.writerow(record)

INVERTED_PRICES = {str(value): key for key, value in PRICES.items()}
REGION_COUNTRIES = {"DE": "DACH_DE", "AT": "DACH_AT", "CH": "DACH_CH", "BE": "BNL_BE", "NL": "BNL_NL", "FR": "MED_FR", "EN": "UK_EN", "DK": "NORD_DK", "FI": "NORD_FI", "IT": "MED_IT", "PL": "VIS_PL", "PT": "MED_PT", "ES": "MED_ES", "SE": "NORD_SE", "NO": "NORD_NO"}

def generate_new_order(order_line):
  if order_line[1] == "":
    return [[order_line[0], "", "", "", 0.00]]
  else:
    order_line_id = order_line[0] + order_line[1]
    article_id = INVERTED_PRICES[order_line[4]]
    order_date = order_line[2]
    country = REGION_COUNTRIES[order_line[3]]
    sales_price = order_line[5]
    new_order = [[
      order_line_id,
      str(article_id),
      order_date,
      country,
      sales_price]]
    return new_order

new_records = []
for record in records:
  new_records += generate_new_order(record)

#for x in new_records: print(x)

with open('generated_data2.csv', 'w', newline='\n') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=',',
              quotechar='\\', quoting=csv.QUOTE_MINIMAL)
  for new_record in new_records:
    csvwriter.writerow(new_record)