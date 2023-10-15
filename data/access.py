

def grant_access(user = "no_user", dataset = "no_dataset", access="no_access"):
	if user == "no_user":
		print("User name needed, try to provide user=\"user\" as argument.")
		return
	if " " in user:
		print("User name should only be one word.")
		return
	if not user.islower():
		print("User name should be all lowercase.")
		return
	if user != "mschultze":
		if "schultze" in user:
			print("User names are constructed from the first letter of first name + the full last name.")
			return
		else:
			print("Please note, the function only works for the user from the exercise request \"Max Schultze\".")
			return
	if user == "mschultze":
		print("Correct user name!")
		if dataset == "no_dataset":
			print("Please provide a dataset by specifying dataset=\"dataset\" as additional parameter.")
			return
		if " " in dataset:
			print("Dataset should not contain any spaces.")
			return
		if not dataset.islower():
			print("Dataset should be all lowercase.")
			return
		if dataset != "order_positions":
			if "order" in dataset and "positions" in dataset:
				print("Datasets can contain \'_\' as word separator.")
				return
			else:
				print("Please note, the function only works for the dataset from the exercise request \"Order Positions\".")
				return
		if dataset == "order_positions":
			print("Correct dataset!")
			switcher = {
				"no_access": "Please provide access mode by specifying access=\"access\" as additional parameter.",
				"read": "Read access has been granted.",
				"write": "Are you sure the user needs write permissions? Maybe \"read\" is enough.",
				"full": "Are you sure the user needs full permissions? Maybe \"read\" is enough."
			}
			print(switcher.get(access, "Invalid access method. Available options: full, write, read"))
			return

def search_catalog(argument = "no_argument"):
	switcher = {
		"no_argument": "Please specify either \"list\" to list existing datasets or provide the name of an existing dataset.",
		"list": "Existing datasets:\norder_positions, articles, customer_details",
		"order_positions": "The Order_positions dataset contains all information related to the sales made through our platform. For each order placed by our customers multiple records are created that each represent one item bought within that order. A single record can always be identified by its order_id and a line_number, its position within that order. Please note, if all content of an order is returned by the customer, a reference to the order is kept through a record with the order_id, but empty remaining attributes.\n" + 
			"For each ordered item you will find additional article information. An article_id is kept as a reference that identifies the article, as well as the article_group, for analytical grouping. Please note, the upstream service that provides this information is not fully reliable which can lead to empty article_group values even for known articles.\n" + 
			"The sales_price represents the actual sales value after applying discounts and before taxes.",
		"articles": "Article dataset.",
		"customer_details": "Confidential customer details."
	}
	print(switcher.get(argument, "Unknown dataset. speficy \"list\" as an argument to list existing datasets."))

def request_access(user_text = "no_user_text", user = "no_users", dataset = "no_dataset", request_text = "no_request_text", access_mode = "no_access_mode"):
	if user != "mschultze":
		print("invalid user")
		return
	if dataset != "order_positions":
		print("invalid dataset")
		return
	if access_mode != "read":
		print("invalid access mode")
		return
	print("User text: " + user_text)
	print("User: " + user)
	print("Dataset: " + dataset)
	print("Request text: " + request_text)
	print("Access mode: " + access_mode)
	print("Request accepted!")

def check_requests():
	print("Open requests for team ABC:")
	print("User text: Max Schultze")
	print("User: mschultze")
	print("Dataset: order_positions")
	print("Request text: \"As a member of team XYZ, in order to fulfill the business purpose of providing reorder recommendations to our planners to increase availability over the season, I need access to this data of H120 and H220 to make some analysis on budget spent/planned and availability of our assortment, so that we can identify how could we better support our users based on the availability of the assortment data that we have now.\"")
	print("Access mode: read")
	arg = input("Accept request [Y/n]?")
	if arg == "Y":
		print("Request accepted!")
	elif arg == "n":
		print("Request denied!")
	else:
		print("Invalid argument.")

if __name__ == '__main__':
	#grant_access()
	#grant_access(user="Max Schultze")
	#grant_access(user="MaxSchultze")
	#grant_access(user="maxschultze")
	#grant_access(user="awider")
	#grant_access(user="mschultze")
	#grant_access(user="mschultze", dataset="Order Positions")
	#grant_access(user="mschultze", dataset="OrderPositions")
	#grant_access(user="mschultze", dataset="orderpositions")
	#grant_access(user="mschultze", dataset="articles")
	#grant_access(user="mschultze", dataset="order_positions")
	#grant_access(user="mschultze", dataset="order_positions", access="test123")
	grant_access(user="mschultze", dataset="order_positions", access="read")
