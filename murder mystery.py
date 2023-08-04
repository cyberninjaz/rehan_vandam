
def intro():
	
	choice=input("Pick the number of the option you choose:\n1. meet the suspects\n2. go to the shooting site\n").lower()
	return choice


def guesing_the_suspects():
	choice=input("Do you think its rehan,jake,johny, mick, bonny, piankhi, or kon. ").lower()
	if choice == "rehan":
		print ("youre wrong")
		return False
	if choice =="johny":
		print ("you won congrats")
		return True
	if choice =="jake":
		print ("youre wrong")
		return False
	if choice == "piankhi":
		print ("youre wrong")
	if choice == "bonny":
		print ("youre wrong")
	if choice== "kon":
		print ("youre wrong")

def talk_to_suspects():
	print('You will get a story from each of the suspects, which is proven true from a lie detector.\n First Rehan who was having a picknick ')
	print ("Second Jake who was camping all alone in the forest.\n Third johny who was trying to find animals.\nFourth mick who was hiking  Fifth piankhi who was punching trees \n Sixth bonny who was dancing.Seventh Kon was jumping in the forest. ")

def go_to_cops_house():
	print("You run into a cop and they found it might be connected to a gang being hired on the black market. \nThe cop asks do you want to go to the gang ")
	choice=input ("Do you want to join the cop?")
	if choice == "yes":
		print ("Congrats you go tricked and now are in a jail cell")
		choice =input ("Escape through the windows, or take the guards key or take the guards keys and run")
		if choice == "take the guards keys and run":
			return False
		if choice == "Escape through the windows":
			choice =input ("Continue the research")
	
	return True


def people_sneak_in():
	print ("Lets go to sleep now ah people broke in")
	rol=input("run,hide,or attack them")
	if rol =="attack them":
		print ("you died")
	if rol == "hide":
		print ("you died")
	if rol=="run":
		print ("We escaped and found a card then researched it")
		print ("The card only says the initials j and b and has an addres on it") 
		


def going_to_the_address():
	print('\n--------Arrived at the adress--------\n')
	print("Their is one guy in a huge underground lab")
	print("He is leaving, Its time to investigate")
	print("Theres a victim on the board")
	print("Also a stack of guns")
	print("He is coming back we should go away")
	print("The next day the victim was murdered")
	print("The cops said the murder happend on a ship. ")
	print("The only thing found was a goat used to kill the person.")
	print("This is ridiculous ")

	rol = input("Report their secret base to the cops yes or no").lower()
	if rol== "yes":
		print ("The cops got some info")
		print ("They Got the goats dna. ")
		print ("The dna matches to 3 of the suspects pets")
		print ("It matches to Johny the animal researcher pet ,bonny the hunter pet, and kon the builder pet")
		
	
def huge_clue():
	print ("the card was researched even more ")

def go_to_shooting():
	print ("The cops got some information, that Johny said we were just walking around the forest and a guy suddenly\ncame up from behind. Then puched me in the stomach from behind. I imiedly ran away")


def The_ending():
	print ("There is a murder curently happening near us, lets go there.")
	print ("we arrived, and we see the murderer")
	mur = input('Choose the Number of the option you want:\n1. run from them,\n2.Dance in front of them, and\n3.secretly follow them. ')
	if mur == "2":
		print ("you died")
		return False
	if mur == "1":
		print ("you died")
		return False
	if mur == "3":
		print ("We followed him to the murderes underground tunnel.")


	print ("It looks like he is leaving. Lets look at his base, it looks like he has alot of pets")
	print ("Oh he is now behind you threathining you with a gun. ")
	mur=input("He is saying to follow him. Follow him or atack him").lower()
	if mur == "follow him":
		print ("you died")
		return False
	if mur == "attack him":
		print ("You jumped on him, and his gun fell in the pond")
		mur=input("Stand there, or run away.").lower()
	if mur == "stand there":
		print ("you died")
		return False
	if mur == "run away":
		print ("You ran away, and now you are in the forest with a murderer chasing you. Then you see a bear.")
	mur=input("Attack the bear, or throw the man to the bear.").lower()
	if mur == "attack the bear":
		print ("you died")
		return False
	if mur== "Throw the man to the bear":
		print ("The man died and now the bear is chasing you.")
		mur=input("Run away from the bear, or hide from the bear.").lower()
	if mur== "run away from the bear":
		print ("you died")
		return False
	if mur == "hide from the bear":
		print ("You survived, and escpaped the forest but now they think you did the murder. Your in jail, and It was also a diffrent murderer.")
	mur=input("dont try to escape or escape jail").lower()
	if mur == "dont try to escape":
		print ("you died")
		return False
	if mur == "escape jail":
		print ("You escaped jail but now you dont have anything.")
	mur=input("get some money or research now ").lower()
	if mur == "research now":
		print ("you starved")
		return False
	if mur == "get some money":
		print ("You get a hotel for the night, but now cops are knocking on your door.")
	mur=input('Punch the cops, and escape or hide ').lower()
	if mur =="hide":
		print ("you died")
		return False
	if mur =="punch the cops and escape":
		print ('You escaped, and the cops are not on you')
	mur=input('There is a murder, two minutes away go there or stay here').lower()
	if mur =="stay here":
		print ("you died")
		return False
	if mur == "go the where the murder is.":
		print ("You punched the same murderer ,and got all your trust back. Also got even more money then you had before.You also now now know the name of the murder starts with a j and o.")
		return True







print ("2 days ago there was a murder in the middle of the forest.\n There are 7 suspects so far,all with no criminal record. Its your job to find the murderer.")

while True:
	print('\n----------------------------------------\n')
	player = intro()
	if player == '1': 
		talk_to_suspects()
	if player == '2':
		go_to_shooting()

	choice = input ("do you want to guess the suspects? ").lower()
	if choice == "yes":
		guesing=guesing_the_suspects()
		if guesing == True:
			print ("congrats you got the suspect")
			break 
		else:
			print ("you did not coreclty gues the murderer. The murderer wins")
			break 

	place=input ("a cop invited you to what he claims is the murders house do you want to go? ").lower()
	if place=="yes":
		if go_to_cops_house():
			print('You were killed. Game over!')
			break

		mur = input("do you want to gues the suspects").lower()
		if mur== "yes":
			guessing = guesing_the_suspects()
			if guessing == True:
				print ("congrats you got the murderer")
				break
			else:
				print('That is not the murderer. You lose!')
				break

		
	rol =input ("do you want to go to the address? ").lower()
	if rol== "yes": 
		going_to_the_address()
		people_sneak_in()

	rol = input ("do you want to guess the suspects? ").lower()
	if rol== "yes":
		guesing = guesing_the_suspects()
		if guesing == True:
			print ("congrats you got the suspects!")
			break
		else:
			print ("you did not corecly guess the murder. The murderer wins")
			break
	
	death = The_ending()
	if death == False:
		break
	else:
		print('This is your last chance to guess the suspect')
		guesing = guesing_the_suspects()
		if guesing == True:
			print ("congrats you got the suspects!")
			break
		else:
			print ("you did not corecly guess the murder. The murderer wins")
			break



		

