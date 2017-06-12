import random

cards = random.randint(0,51)
river = []
players = {"p1": 500, "p2": 500, "p3": 500, "p4": 500, "p5": 500}
choices = ["check", "bet", "raise", "fold"]
history = {}
chips = 500
pot = 0
# Used to see what each players current bet is. 
bet = {"p1": 0, "p2": 0, "p3": 0, "p4": 0, "p5": 0}
def dealcards():
	# p1 can't bet unless it's not the first time p1 can make a choice for the phase.
	p1canraise = "no"
	##for (player in players)
		##if  !((bet["p1"] == 0 and bet["p2"] == 0 and bet["p3"] == 0 and bet["p4"] == 0) or (bet["p1"] != bet["p2"] != bet["p3"] != bet["p4"])):
			##break
		
		currchoice = random.choice(choices)
		print(player + " would like to " + currchoice) 
		if currchoice is "check":
			maxbid = players[str(player)]
		elif currchoice is "bet": 
			randbet = random.randint{1,maxbid}
			# Takes out the money that the player bets from their chips.
			players[str(player)] -= randbet
			maxbid = players[str(player)]
			pot += randbet
			print(player + " would like to bet " + randbet)
		# This if statement is used if the player is first betting and wants to raise the current bet.
		elif (currchoice is "raise") and !(history.contains(player + ": " + "raise")) and !(player is p1) and !(bet.contains(player)):
			history[player] = "raise"
			randraise = random.randint{1,players[str(player)]}
			# Takes out the money that the player bets from their chips.
			players[str(player)] -= (randbet + randraise)
			maxbid = players[str(player)]
			pot += (randbet + randraise)
			print(player + " would like to raise " + randbet)
		# This if statement is used if the player already betted, but is raising on another phase.
		elif (currchoice is "raise") and !(history.contains(player + ": " + "raise")) and !(player is p1) and (bet.contains(player)):
			history[player] = "raise"
			randraise = random.randint{1,players[str(player)]}
			# Takes out the money that the player bets from their chips.
			players[str(player)] -= randraise
			maxbid = players[str(player)]
			pot += randraise
			print(player + " would like to raise " + randbet)
			
			for player in players
			
				if .count
			
		# If p1 is able to raise, therefore it's no longer the first choice able to be made for the current phase of the hand.
		elif (currchoice is "raise") and !(history.contains(player + ": " + "raise")) and (player is p1) and (p1canraise is "yes"):
			history[player] = "raise"
			randraise = random.randint{1,players[str(player)]}
			# Takes out the money that the player bets from their chips.
			players[str(player)] -= (randbet + randraise)
			maxbid = players[str(player)]
			print(player + " would like to raise " + randbet)
			
		elif currchoice is "fold":
			del players[str(player)]
			del bet[str(player)] 
	
	# The river is distributed.	
	# There are 0 cards on the river.
	if river == 0:
		river.append(cards)
		river.append(cards)
		river.append(cards)
		print(river)
		dealcards()
		
	# There are 3 cards on the river.
	elif river.len() == 3:
		river.append(cards)
		print(river)
		dealcards()
		
	# There are 4 cards on the river.	
	elif river.len() == 4:
		river.append(cards)
		print(river)
		dealcards()