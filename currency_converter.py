import time

#RM = 1
#USD = 0.24
#EUR = 0.21
#IR = 3519.40
#NZD = 0.36

def header():

	print("\n--------------------------------------------------------------------")
	print("           Welcome to ZumTheZazaKing's Currency Converter!            ")
	print("--------------------------------------------------------------------\n")

	time.sleep(2)

	print("                                NOTICE:                               ")
	time.sleep(1)
	print("   The default currency to be converted is Malaysian Ringgit (RM)     ")
	time.sleep(1)
	print("                        This CANNOT be changed                        ")



def main():

	time.sleep(2)
	print("\n")

	print("Choices:")
	time.sleep(0.25)
	print("1. USD (United States Dollars)")
	time.sleep(0.25)
	print("2. EUR (Euro)")
	time.sleep(0.25)
	print("3. IR (Indonesian Rupiah)")
	time.sleep(0.25)
	print("4. NZD (New Zealand Dollars)")

	time.sleep(1)

	ans = str(input("""
Please select a currency you would like to convert to
(1/2/3/4):"""))

	if ans == "1":

		time.sleep(1)

		print("\n")
		print("-" * 70)
		print("You have chosen to convert RM to USD (United States Dollars)")
		print("-" * 70)

		time.sleep(1)

		amount = round(float(input("""
Please enter the amount of RM you would like to convert:""")))
		print("\n")

		time.sleep(0.5)

		print("-" * 70)
		print("Processing...")
		print("-" * 70)

		time.sleep(2)

		print("\n")
		print(amount, "RM is equivalent to ", round((amount) * 0.24, 2), "USD", "\n")

	elif ans == "2":

		time.sleep(1)

		print("\n")
		print("-" * 70)
		print("You have chosen to convert RM to EUR (Euro)")
		print("-" * 70)

		time.sleep(1)

		amount = round(float(input("""
Please enter the amount of RM you would like to convert:""")))
		print("\n")

		time.sleep(0.5)

		print("-" * 70)
		print("Processing...")
		print("-" * 70)

		time.sleep(2)

		print("\n")
		print(amount, "RM is equivalent to ", round((amount) * 0.21, 2), "Euro", "\n")

	elif ans == "3":

		time.sleep(1)

		print("\n")
		print("-" * 70)
		print("You have chosen to convert RM to IR (Indonesian Rupiah)")
		print("-" * 70)

		time.sleep(1)

		amount = round(float(input("""
Please enter the amount of RM you would like to convert:""")))
		print("\n")

		time.sleep(0.5)

		print("-" * 70)
		print("Processing...")
		print("-" * 70)

		time.sleep(2)

		print("\n")
		print(amount, "RM is equivalent to ", round((amount) * 3519.40, 2), "IR", "\n")

	elif ans == "4":

		time.sleep(1)

		print("\n")
		print("-" * 70)
		print("You have chosen to convert RM to NZD (New Zealand Dollars)")
		print("-" * 70)

		time.sleep(1)

		amount = round(float(input("""
Please enter the amount of RM you would like to convert:""")))
		print("\n")

		time.sleep(0.5)

		print("-" * 70)
		print("Processing...")
		print("-" * 70)

		time.sleep(2)

		print("\n")
		print(amount, "RM is equivalent to ", round((amount) * 0.36, 2), "NZD", "\n")

	else:
		print("\nThat's not a valid answer. You'll be kicked automatically for that.\n")
		time.sleep(2)
		exit()



header()

while True:
    main()
    time.sleep(2)
    if str(input("""Would you like to convert again?
(Type Y(Yes) or N(No))\n
""")).strip().upper() != "Y":
      print("\nGoodbye!\n")
      time.sleep(1)
      break
