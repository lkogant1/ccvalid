class CreditCard:
	card_number = str() 

	def __init__(self,card_number):
		self.card_number = card_number

	def card_type(self):
		try:
			int(self.card_number)
		#pull the first two digits
			self.two_digits = self.card_number[0:2]
			#create a dictionary of first two digits
			self.keys = ["34","37","60","40", "41", "42", "43", "44", "45", "46", "47", "48", "49","51","52","53","54","55"]
			self.values = ["Amex","Amex","Discover","Visa","Visa","Visa","Visa","Visa","Visa","Visa","Visa","Visa","Visa","MasterCard","MasterCard","MasterCard","MasterCard","MasterCard"]
			self.dictionary = dict(zip(self.keys,self.values))
			#return self.dictionary

			for key,value in self.dictionary.items():
				if key == self.two_digits:		
					return self.card_number, "is", value
				
			for key,value in self.dictionary.items():
				if key !=self.two_digits:
					return self.card_number, "is INVALID card type"

		except ValueError:
			return Self.card_number, "is not NUMERIC"

	#check length of card number and #luhn algorithm		
	def valid(self):
	# #https://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except
		try:
			int(self.card_number)
			if len(self.card_number) > 0:
				if len(self.card_number) == 16 or len(self.card_number) == 15:
					#convert string to list format
					self.number_strings = list(self.card_number)
					#convert list "string" format to list "int" format
					self.number_strings = list(map(int,self.number_strings))
					#https://stackoverflow.com/questions/10351772/converting-list-of-string-to-list-of-integer
					#print(self.number_strings)
					#----------------------------------------------
					#Creates two lists: 
					#first list:From the right most digit, 
					#double the value of every second digit. 
					list1 = []
					#Loop through indices,add the elements of indices to list: 
					for i in range((len(self.card_number)-2),-1,-2):
						new = (self.number_strings[i])*2
						list1.append(new)		
					#print(list1)
					#second list: list of left out elements in the above loop
					list5 =[]
					for i in range((len(self.card_number)-1),-1,-2):
						new = (self.number_strings[i])
						list5.append(new)		
					#print(list5)	
					#----------------------------------------------
					list2=[]
					list3=[]
					#for the integers that are >=10 in list1
					for i in list1:
						if i >= 10:
							list2.append(i)
						else:
							list3.append(i)
					#print(list2)
					#print(list3)
					#----------------------------------------------
					#sum the strings in list2 for numbers >=10
					#https://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python
					list4=[]
					for i in list2:
						list4.append(sum(map(int,str(i))))
					#print(list4)

					#sum the integers in list3
					sum1 =0
					for i in list3:
						sum1 = sum1+i
					#https://stackoverflow.com/questions/12964460/adding-numbers-in-a-range-with-for-loop
					#print(sum1)

					#sum the integers in list4
					sum2 =0
					for i in list4:
						sum2 = sum2+i
					#print(sum2)

					#sum the integers in list 5
					sum3 = 0
					for i in list5:
						sum3 = sum3+i
					#print(sum3)

					#sum of sums
					total = sum1+sum2+sum3
					#print(total)
					#----------------------------------------------
					#check if total is divisible by 10
					if total % 10 == 0:
						return self.card_number, "is VALID card number"
					else:
						return self.card_number, "INVALID card number"
				#----------------------------------------------
				else:
					return self.card_number, "INVALID length"
			else:
				return self.card_number, "INVALID length"
		except ValueError:
			return self.card_number, "Input is not NUMERIC"

		#----------------------------------------------
cc = CreditCard('9999999999999999')
print(cc.valid())
print(cc.card_type())

cc = CreditCard('4440')
print(cc.valid())
print(cc.card_type())

cc = CreditCard('5515460934365316')
print(cc.valid())
print(cc.card_type())

cc = CreditCard('6011053711075799')
print(cc.valid())
print(cc.card_type())

cc = CreditCard('379179199857686')
print(cc.valid())
print(cc.card_type())

cc = CreditCard('4929896355493470')
print(cc.valid())
print(cc.card_type())

cc = CreditCard('4329876355493470')
print(cc.valid())
print(cc.card_type())

cc = CreditCard('339179199857685')
print(cc.valid())
print(cc.card_type())

#OUTPUT
# ('9999999999999999', 'INVALID card number')
# ('9999999999999999', 'is INVALID card type')
# ('4440', 'INVALID length')
# ('4440', 'is', 'Visa')
# ('5515460934365316', 'is VALID card number')
# ('5515460934365316', 'is', 'MasterCard')
# ('6011053711075799', 'is VALID card number')
# ('6011053711075799', 'is', 'Discover')
# ('379179199857686', 'is VALID card number')
# ('379179199857686', 'is', 'Amex')
# ('4929896355493470', 'is VALID card number')
# ('4929896355493470', 'is', 'Visa')
# ('4329876355493470', 'INVALID card number')
# ('4329876355493470', 'is', 'Visa')
# ('339179199857685', 'is VALID card number')
# ('339179199857685', 'is INVALID card type')




