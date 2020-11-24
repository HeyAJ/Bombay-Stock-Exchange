from bsedata.bse import BSE
import json
b = BSE()
print(b)

b = BSE(update_codes = True)

while True:
	main_input = int(input("\nWhat You Want To Do\nPress 1 to Get The List Of Todays Top Gainers\nPress 2 to Get The List Of Todays Top Losers\nPress 3 to Get The List of the Scrip Code Of The Respective Companies\nPress 4 to Get the Information About The Company Stock by Providing the Scrip Code: "))
	scrip_code = b.getScripCodes()
	Gainers = b.topGainers()
	Losers = b.topLosers()
	if main_input == 1:
		print(json.dumps(Gainers,sort_keys=True,indent=4))
	if main_input == 2:
		print(json.dumps(Losers,sort_keys=True,indent=4))
	if main_input == 3:
		print(json.dumps(scrip_code,sort_keys=True,indent=4))
	if main_input == 4:
		Quote = b.getQuote(input("Please Enter The Scrip Code To Get The Information About The Company Stock: "))
		print(json.dumps(Quote,sort_keys=True,indent=4))

	con = int(input("\nDo You Want to Continue\nPress 1 For Yes\nPress 2 For No: "))

	if con == 2:
		break






