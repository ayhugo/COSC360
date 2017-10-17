import sys
import itertools

		

#Globals
untidy_input = ""
temp_cards = []
card_order = ['2','3','4','5','6','7','8','9','0','J','Q','K','A']
#bad code but running out of ideas
deckOfCards = ['1H','2H','3H','4H','5H','6H','7H','8H','9H','10H','11H','12H','13H','TH','JH','QH','KH','AH','1D','2D','3D','4D','5D','6D','7D','8D','9D','10D','11D','12D','13D','TD','JD','QD','KD','AD','1C','2C','3C','4C','5C','6C','7C','8C','9C','10C','11C','12C','13C','TC','JC','QC','KC','AC','1S','2S','3S','4S','5S','6S','7S','8S','9S','10S','11S','12S','13S','TS','JS','QS','KS','AS']
sorted_cards = []
cards_output = []

def check_hand(hand):
	if hand in deckOfCards:
		return True
	else: return False
#checking for more than one of the same cards
def check_dups(cards, untidy_input):
	s = set(cards)

	if (len(s) < len(cards)):
		print("Invalid: "+untidy_input)
	else:
		sort_cards(cards, untidy_input)

#error checking
def check_validity(cards, untidy_input):
	i = 0
	validBool = True
	for item in cards:
		if(check_hand(item) != True):
			validBool = False
			print("Invalid: "+untidy_input)
			break
		if len(item) > 3 or item == "":
			validBool = False
			print("Invalid: "+untidy_input)
			break
		elif len(item) == 3:
			try:
				 i = int(item[1])
				 j = int(item[0]) 
				 if (i > 3):
				 	validBool = False
				 	print("Invalid: "+untidy_input)
				 	break
				 if (j != 1):
				 	validBool = False
				 	print("Invalid: "+untidy_input)
				 	break
			except:
				validBool = False
				print("Invalid: "+untidy_input)
	if(validBool):
		ready_cards_for_sort(cards, untidy_input)
			
			

#convert '0' cards to '10' cards and print out the output
def output(sortedCards):
	cards_output=[]
	for i in sortedCards:
		if (i.find('0') != -1):
			if (i.find('H') != -1):
		  		cards_output.append('10H')
		  		continue
		  	elif (i.find('D') != -1):
		  		cards_output.append('10D')
		  		continue
		  	elif (i.find('C') != -1):
		  		cards_output.append('10C')
		  		continue		
		  	elif (i.find('S') != -1):
		  		cards_output.append('10S')	
		  		continue	 	
		else:
			cards_output.append(i)
	for i in cards_output:
		sys.stdout.write(i+" ")
	print('')
	sys.stdout.flush()

#sorts the cards... I have no idea how it does it. Thanks stackoverflow
def sort_cards(cards, untidy_input):
	sorted_cards =[]
	try:
		sort_map = {c: i for i, c in enumerate(card_order)}
		sorted_cards = sorted(cards, key=lambda card: (sort_map[card[0]], card[1]))
	#sorted_cards = cards.sort(key=lambda c:card_order.index(c[0]))
		output(sorted_cards)
	except:
		print("Invalid: "+untidy_input)

#converts all 10's 11's 1's etc... to the appropriate card to be sorted.
def ready_cards_for_sort(userinput, untidy_input):
	temp_cards=[]
	for i in userinput:
		if (i.find('10')!= -1):
		  	if (i.find('H') != -1):
		  		temp_cards.append('0H')
		  		continue
		  	elif (i.find('D') != -1):
		  		temp_cards.append('0D')
		 		continue
		  	elif (i.find('C') != -1):
		  		temp_cards.append('0C')
		  		continue
		  	elif (i.find('S') != -1):
		  		temp_cards.append('0S')
		 		continue

		if (i.find('11')!= -1):
			if (i.find('H') != -1):
				temp_cards.append('JH')
				continue
			elif (i.find('D') != -1):
				temp_cards.append('JD')
				continue
			elif (i.find('C') != -1):
				temp_cards.append('JC')
				continue
			elif (i.find('S') != -1):
				temp_cards.append('JS')
				continue
		
		if (i.find('12')!= -1):
			if (i.find('H') != -1):
				temp_cards.append('QH')
				continue
			elif (i.find('D') != -1):
				temp_cards.append('QD')
				continue
			elif (i.find('C') != -1):
				temp_cards.append('QC')
				continue
			elif (i.find('S') != -1):
				temp_cards.append('QS')
				continue

		if (i.find('13')!= -1):
			if (i.find('H') != -1):
				temp_cards.append('KH')
				continue
			elif (i.find('D') != -1):
				temp_cards.append('KD')
				continue
			elif (i.find('C') != -1):
				temp_cards.append('KC')
				continue
			elif (i.find('S') != -1):
				temp_cards.append('KS')
				continue
		if (i.find('1')!= -1):
			if (i.find('H') != -1):
				temp_cards.append('AH')
				continue
			elif (i.find('D') != -1):
				temp_cards.append('AD')
				continue
			elif (i.find('C') != -1):
				temp_cards.append('AC')
				continue
			elif (i.find('S') != -1):
				temp_cards.append('AS')
				continue
		if (i.find('T') != -1):
			if (i.find('H') != -1):
		  		temp_cards.append('0H')
		  		continue
		  	elif (i.find('D') != -1):
		  		temp_cards.append('0D')
		 		continue
		  	elif (i.find('C') != -1):
		  		temp_cards.append('0C')
		  		continue
		  	elif (i.find('S') != -1):
		  		temp_cards.append('0S')
		 		continue
		else:
			temp_cards.append(i)
	check_dups(temp_cards, untidy_input)
			
	

#main
if __name__ == "__main__":
	for userinput in sys.stdin:
		untidy_input = ""
		untidy_input += userinput.rstrip()
		
		#issue of .split where it adds a magic 'D' to at the split

		if (untidy_input.find('/') != -1):
			cards = untidy_input.upper().split('/')
			if (len(cards) < 5 or len(cards) > 5):
				print("Invalid: "+untidy_input)
				continue
			else:
				check_validity(cards, untidy_input)
				continue

		elif (untidy_input.find(' ') != -1): 
			cards = untidy_input.upper().split(' ')
			if (len(cards) < 5 or len(cards) > 5):
				print("Invalid: "+untidy_input)
				continue
			else:
				check_validity(cards, untidy_input)
				continue

		elif (untidy_input.find('-') != -1):
			cards = untidy_input.upper().split('-')
			if (len(cards) < 5 or len(cards) > 5):
				print("Invalid: "+untidy_input)
				continue
			else:
				check_validity(cards, untidy_input)
				continue
		else:
			print("Invalid: "+untidy_input)



	





