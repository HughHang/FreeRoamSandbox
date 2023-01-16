#Hugh Hang 101231265

import pygame
import sys


names = ["Drive Way", "Porch", "Garage", "1st Hallway", "Laundry Room", "Mudroom", "2nd Hallway", "2nd Washroom", "Master Bedroom", 
	"1st Washroom", "3rd Hallway", "Entrance", "Basement", "Living Room", "Kitchen", "Dining Room", "4th Hallway", "3rd Washroom", 
	"1st Bedroom", "1st Closet", "2nd Bedroom", "2nd Closet", "Patio", "Gazebo", "Barbeque", "Garden"] 

edges = [
	#Drive Way Directions
	[[1, "northeast"], [2, "north"]],
	#Porch Directions
	[[0, "southwest"], [11, "north"]], 
	#Garage Direction
	[[0, "south"], [3, "north"]],
	#1st Hallway Directions
	[[2, "south"], [4, "west"], [5, "east"], [6, "north"]], 
	#Laundry Room Direction
	[[3, "east"]], 
	#Mudroom Directions
	[[3, "west"], [11, "east"]], 
	#2nd Hallway Directions
	[[3, "south"], [7, "west"], [8, "north"], [10, "east"]], 
	#2nd Washroom Direction
	[[6, "east"]], 
	#Master Bedroom Directions
	[[6, "south"], [9, "northwest"]], 
	#1st Washroom Direction
	[[8, "east"]], 
	#3rd Hallway Directions
	[[11, "south west"], [15, "south"], [6, "west"], [12, "northwest"], [13, "north"], [14, "northeast"], [16, "east"]], 
	#Entrance Directions
	[[1, "south"], [5, "west"], [10, "north"]], 
	#Basement Direction
	[[10, "east"]], 
	#Living Room Directions
	[[10, "south"], [14, "east"], [22, "north"]], 
	#Kitchen Directions
	[[10, "south"], [13, "west"]], 
	#Dining Room Direction
	[[10, "north"]],
	#4th Hallway Directions
	[[10, "west"], [17, "east"], [18, "north"], [20, "south"]], 
	#3rd Washroom Direction
	[[16, "west"]], 
	#1st Bedroom Directions
	[[16, "south"], [ 19, "southeast"]], 
	#1st Closet Direction
	[[18, "north"]],
	#2nd Bedroom Directions
	[[ 16, "northwest"], [21, "north"]], 
	#2nd Closet Direction
	[[20, "south"]], 
	#Patio Directions
	[[13, "south"], [23, "northwest"], [24, "northeast"], [25, "east"]], 
	#Gazebo Directions
	[[22, "south"], [22, "east"]], 
	#Barbeque Directions
	[[22, "south"], [22, "west"]],
	#Garden Direction
	[[22, "west"]]
	]

descriptions = [
	#Drive way description 0
	"The drive way has nice black pavement. If you look east and west you can see the nicest patch of green grass ever. The garage is to the north. The porch is northeast.",
	#Porch description 1
	"The lime brick porch is smooth. If you look east, you can see nice porch furniture. Two chairs with comfortable padding and a nice coffee table. The drive way is southwest. The entrance is north.",
	#Garage description 2
	"It's very spacious in here. There's a boat and two cars. You can take the trash can in the corner if you would like. The drive way is south. The 1st Hallway is north.",
	#1st Hallway desciption 3
	"It's kind of cramped and small here. It's also dark but it's okay. Ouuuu, you can take that broom if you want at the corner. The garage is south. The laundry room is west. The mudroom is east. The 2nd hallway is north.",
	#Laundry room description 4
	"At the back corner theres the dryer and right beside it is the washer. There's a nice ironing board against the wall there and the sink right beside it. The 1st hallway is east.",
	#Mudroom desciption 5
	"It's smelly in here. So many shoes. Majority of them are actually my moms but I think the smellier ones are my brother's. There's three shoe racks and somehow all of them are full. You can definitely take one of my brother's pairs of sneakers if you want. The 1st hallway is west. The entrance is east.",
	#2nd Hallway description 6
	"There's a nice painting hanging on the wall! It's a family portrait. It's me, my brother, and parents! There's also a nice night light on the wall that turns on when there is movement. The 1st hallway is south. The 2nd washroom is west. The master bedroom is north. The 3rd hallway is east.",
	#2nd Washroom description 6
	"This is the smallest washroom in the house. It's only got a toilet and sink but it's still a fan favourite for guests. If you look to your left there's a tissue box if you would like to take it. The 2nd hallway is east.", 
	#Master Bedroom description 7
	"Welcome to my parent's room. They got a king sized bed there and you can see my dad's ping pong trophy on the drawer against the wall. The 1st washroom is northwest. The 2nd hallway is south.",
	#1st Washroom description 8
	"There's a tub to your right, in the corner there. You like the double sinks? Oh and in the corner, there's my parent's closet if you were wondering. The master bedroom is east.",
	#3rd Hallway desciption 9
	"This is the main part of the house. The piano there is mine but it could be yours to take if you really want to. If you look straight up you'll see two ceiling fans. The entrance is southwest. The dining room is south. The 2nd hallway is west. The basement is northwest. The living room is north. The kitchen is northeast. The 4th hallway is east.",
	#Entrance description 10
	"Double doors for the front doors are always blessed. I don't know why but my mom really likes the plant in the corner there but I guess I don't mind it. There's a little bench there if you wanna rest. The porch is south. The mudroom is west. The 3rd hallway is north.",
	#Basement description 11
	"Dang it's dark down here. I wonder if you like the cute little coffee table we have in the corner there? We had an extra coffee table so we just decided to put it there. The basement is actually unfinished so I'd prefer if we didn't have to continue down here. The 3rd hallway is east.",
	#Living Room desciption 12
	"We got a huge L shaped couch. It's comfortable and has good material too! The only problem is that I think we have too many pillows but my mom loves them. You like the 70 inch tv? The 3rd hallway is south. The kitchen is east. The backyard patio is north.",
	#Kitchen description 13
	"I love the island here. My favourite part of the kitchen. We have this huge fridge too. When we first bought this house, my brother and I couldn't get over how big the fridge is. We got a toaster, rice cooker of course, espresso machine, dishwasher, sink, and second sink, oven, and stove. The 3rd hallway is south. The living room is west.",
	#Dining Room description 14
	"We've had this circular dining table for as long as I can remember. It's in really nice condition for being like 15+ years old. I really like the little chandlier we have if you look straight up. The 3rd hallway is north.",
	#4th Hallway description 15
	"Small and empty hallway but it does it's job I guess. The 3rd hallway is west. The 3rd washroomm is east. The 1st bedroom is north. The 2nd bedroom is south.",
	#3rd Washroom description 16
	"This is the washroom I share with my brother. The double sink is blessed. The shower is there but it's definitely not as nice as my parent's. The toilet in the corner there. The 4th hallway is west.",
	#1st Bedroom description 17
	"This is my room! I got a twin size bed sadly. I want a queen size but not yet. I got my PC in the corner there and my electronic keyboard on against the wall there. The 4th hallway is south. The 1st closet is southeast.",
	#1st Closet description 18
	"Sorry I got a lot of boxes in here because I like to keep the boxes of things I buy. You could take one if you would like. Also if you look up there's also a stacks of clothes that I don't wear anymore because I outgrew them. The 1st bedroom is north.",
	#2nd Bedroom description 19
	"This is my brother's room. He has a queen size bed in the middle with his PC in the corner. I love his mounted 40 inch TV. He's got his PS4 and Nintendo Switch right under it. The 4th hallway is northwest. The 2nd closet is north.",
	#2nd Closet description 20
	"My brother's closet is just full of clothes. I can't comprehend how he keeps it organized. Also if you look up he keeps the boxes of the things he buys. The 2nd bedroom is south.",
	#Patio description 21
	"You can see everything from here. The trees if you look north. I wish our house was fenced out but sadly it isn't. The living room is south. The gazebo is northwest. The barbeque is northeast. The garden is east.",
	#Gazebo description 22
	"Theres two chairs for one, there's a chair for three, and a coffee table. Don't worry about the plants surrounding the gazebo. My mom just loves plants. The patio is south and east.",
	#Barbeque description 23
	"This is where you can find happiness. This barbeque is old but still works like a charm. There's meat in the barbeque if you wanna have some to eat. The patio is south and west.",
	#Garden description 24
	"This is my mom's happy place. She grows all types of plants here. She switches it up every year. You can take one of the plants if you wish. The patio is west."
	]

#Items to take
items = ["Trash can. ", "Broom. ", "Sneakers. ", "Tissue box. ", "Piano. ", "Box. ", "Meat. "]

#For whether items can be taken of not
garage = True
first_hallway = True
mudroom = True
second_washroom = True
third_hallway = True
first_closet = True
barbeque = True

#Inventory
inventory = []

graph = (names, edges)

#Load the image
img = pygame.image.load(sys.argv[1])

#Get the size of the image
(w, h) = img.get_size()
win = pygame.display.set_mode((w, h))

#Fill background with white
win.fill((255, 255, 255))

#Blit image
win.blit(img, (0, 0))

pygame.display.update()

clock = pygame.time.Clock()

#Starting area
current = "Drive Way"

#Adventure time
flag = True

while flag:
	
	#Tell where user is
	print("You are currently in ", current, ".", sep = '')
	print()
	
	exits = []
	location_index = []
	
	
	index_location = names.index(current)
	#Description
	print(descriptions[index_location])
	
	print()
	
	#Used later to get to the next area
	for each in edges[index_location]:
		start, end = each
		
		location_index.append(start)
		exits.append(end)
	
	
	decision = input("What would you like to do? ")
	print()
	
	#If user wants to move
	try: 
		if decision.lower() == "move":
			next_location = input("Which direction would you like to go? ")
			
			if next_location.lower() in exits:
				
				#Set everything up into the next location
				
				navigate = exits.index(next_location.lower())
				navigate2 = location_index[navigate]
				current = names[navigate2]
				print()
				
	#If they put in a direction that's not an option
	except ValueError:
		print()
		print("You cannot go this way.")
		print()
	
	#If user wants help
	if decision.lower() == "help":
		print("HELP:")
		print()
		print('To move, you must input "move" and then choose a compass direction to go.')
		print('The directions you can go are:')
		print('"north"')
		print('"northeast"')
		print('"east"')
		print('"southeast"')
		print('"south"')
		print('"southwest"')
		print('"west"')
		print('"northwest"')
		print()
		print('To take an item if there is one available, you must input "take" and then the item will be added to your inventory.')
		print()
		print('To check your inventory, you must input "inventory" and your inventory will list your items.')
		print()
		print('To quit, you must input "quit" and you will close the game.')
		print()
		
	#If user wants to take
	elif decision.lower() == "take":
		
		#If user are in the correct area
		if garage == True and current == "Garage":
			
			print("You've taken the trash can.")
			print()
			
			#Append from items list
			inventory.append(items[0])
			
			#Replace description with description without the take option
			descriptions.remove("It's very spacious in here. There's a boat and two cars. You can take the trash can in the corner if you would like. The drive way is south. The 1st Hallway is north.")
			descriptions.insert(2, "It's very spacious in here. There's a boat and two cars. The drive way is south. The 1st Hallway is north.")
			
			#Make if statement invalid because item is gone
			garage = False
		
		#If user are in the correct area
		elif first_hallway == True and current == "1st Hallway":
			
			print("You've taken the broom.")
			print()
			
			#Append from items list
			inventory.append(items[1])
			
			#Replace description with description without the take option
			descriptions.remove("It's kind of cramped and small here. It's also dark but it's okay. Ouuuu, you can take that broom if you want at the corner. The garage is south. The laundry room is west. The mudroom is east. The 2nd hallway is north.")
			descriptions.insert(3, "It's kind of cramped and small here. It's also dark but it's okay. The garage is south. The laundry room is west. The mudroom is east. The 2nd hallway is north.")
			
			#Make if statement invalid because item is gone
			first_hallway = False
		
		#If user are in the correct area
		elif mudroom == True and current == "Mudroom":
			
			print("You've taken a pair of sneakers.")
			print()
			
			#Append from items list
			inventory.append(items[2])
			
			#Replace description with description without the take option
			descriptions.remove("It's smelly in here. So many shoes. Majority of them are actually my moms but I think the smellier ones are my brother's. There's three shoe racks and somehow all of them are full. You can definitely take one of my brother's pairs of sneakers if you want. The 1st hallway is west. The entrance is east.")
			descriptions.insert(5, "It's smelly in here. So many shoes. Majority of them are actually my moms but I think the smellier ones are my brother's. There's three shoe racks and somehow all of them are full. The 1st hallway is west. The entrance is east.")
			
			#Make if statement invalid because item is gone
			mudroom = False
		
		#If user are in the correct area
		elif second_washroom == True and current == "2nd Washroom":
		
			print("You've taken the tissue box.")
			print()
			
			#Append from items list
			inventory.append(items[3])
			
			#Replace description with description without the take option
			descriptions.remove("This is the smallest washroom in the house. It's only got a toilet and sink but it's still a fan favourite for guests. If you look to your left there's a tissue box if you would like to take it. The 2nd hallway is east.")
			descriptions.insert(7, "This is the smallest washroom in the house. It's only got a toilet and sink but it's still a fan favourite for guests. The 2nd hallway is east.")
			
			#Make if statement invalid because item is gone
			second_washroom = False
		
		#If user are in the correct area		
		elif third_hallway == True and current == "3rd Hallway":
		
			print("You've taken and somehow put a whole piano into your inventory.")
			print()
			
			#Append from items list
			inventory.append(items[4])
			
			#Replace description with description without the take option
			descriptions.remove("This is the main part of the house. The piano there is mine but it could be yours to take if you really want to. If you look straight up you'll see two ceiling fans. The entrance is southwest. The dining room is south. The 2nd hallway is west. The basement is northwest. The living room is north. The kitchen is northeast. The 4th hallway is east.")
			descriptions.insert(10, "This is the main part of the house. If you look straight up you'll see two ceiling fans. The entrance is southwest. The dining room is south. The 2nd hallway is west. The basement is northwest. The living room is north. The kitchen is northeast. The 4th hallway is east.")
			
			#Make if statement invalid because item is gone
			third_hallway = False
		
		#If user are in the correct area
		elif first_closet == True and current == "1st Closet":
			
			print("You've taken one of my boxes.")
			print()
			
			#Append from items list
			inventory.append(items[5])
			
			#Replace description with description without the take option
			descriptions.remove("Sorry I got a lot of boxes in here because I like to keep the boxes of things I buy. You could take one if you would like. Also if you look up there's also a stacks of clothes that I don't wear anymore because I outgrew them. The 1st bedroom is north.")
			descriptions.insert(19, "Sorry I got a lot of boxes in here because I like to keep the boxes of things I buy. Also if you look up there's also a stacks of clothes that I don't wear anymore because I outgrew them. The 1st bedroom is north.")
			
			#Make if statement invalid because item is gone
			first_closet = False
	
		#If user is in the correct area
		elif barbeque == True and current == "Barbeque":
		
			print("You've taken a piece of meat.")
			print()
			
			#Append from list
			inventory.append(items[6])
			
			#Replace description with description without the take option
			descriptions.remove("This is where you can find happiness. This barbeque is old but still works like a charm. There's meat in the barbeque if you wanna have some to eat. The patio is south and west.")
			descriptions.insert(24, "This is where you can find happiness. This barbeque is old but still works like a charm. The patio is south and west.")
		
			#Make if statement invalid because item is gone
			barbeque = False
		else:
		
			print("Nothing to take here.")
			print()
			
	#If user wants to see inventory	
	elif decision.lower() == "inventory":
		print("Inventory: ",*inventory)
		print()
		
	#If user wants to close program
	elif decision.lower() == "quit":
		
		flag = False
