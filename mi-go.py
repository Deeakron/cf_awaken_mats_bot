import discord
#import pyodbc
import os
import random
import xml.etree.ElementTree as ET

#set up
client = discord.Client()

#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\xls\CFD.accdb;')

units_tree = ET.parse('units.xml')
awakenings_tree = ET.parse('awakenings.xml')
units_root = units_tree.getroot()
awakenings_root = awakenings_tree.getroot()


update_info = open(r"update_info.txt")
info_line = []
for line in update_info:
	info_line.append(line)


#send message that bot is logged in
@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	game=discord.Game(name='$awaken_help for commands')
	await client.change_presence(activity=game)

@client.event
async def on_message(message):
	#ignores messages from self
	if message.author == client.user:
		return

	#testing concepts
	#if message.content.startswith('$awaken_test '):
	#	input1 = message.content[13:]
	#	for elem in units_root:
	#		if elem[5].text.lower() == input1.lower():
	#			print(elem[2].text)


	#lists awakening mats to awaken the given unit
	if message.content.startswith('$awaken_from '):
		#get input from message
		input1 = message.content[13:]

		#initialize some variables
		unit_target = ""

		target_short = ""
		target_full = ""

		#find the unit in question
		for elem in units_root:
			if elem[5].text.lower() == input1.lower():
				unit_target = elem[0].text
				target_short = elem[1].text
				target_full = elem[2].text
				break

		#initialize more variables
		unit_target2 = ""
		awake_short = ""
		awake_full = ""

		#find all units that target unit awakens to
		for elem in awakenings_root:
			if elem[0].text == unit_target:
				unit_target2 = elem[1].text
				for elem2 in units_root:
					if elem2[0].text == unit_target2:
						awake_short = elem2[1].text
						awake_full = elem2[2].text
						break
				embed = discord.Embed(title=target_short + "   ->   " + awake_short, description=target_full + "   ->   " + awake_full, color=0x00ff00)
				#if first mat exists, get its info
				if elem[2].text != "n/a":
					#get mat names
					temp_input = elem[2].text

					temp_short = ""
					temp_full = ""
					#set mat names
					for elem2 in units_root:
						if elem2[0].text == temp_input:
							temp_short = elem2[1].text
							temp_full = elem2[2].text
							break
					#add mat info to embed
					embed.add_field(value="x" + str(int(elem[3].text)) + " " + temp_short, name=temp_full,inline=False)
				#if second mat exists, get its info
				if elem[4].text != "n/a":
					#get mat names
					temp_input = elem[4].text

					temp_short = ""
					temp_full = ""
					#set mat names
					for elem2 in units_root:
						if elem2[0].text == temp_input:
							temp_short = elem2[1].text
							temp_full = elem2[2].text
							break
					#add mat info to embed
					embed.add_field(value="x" + str(int(elem[5].text)) + " " + temp_short, name=temp_full,inline=False)
				#if third mat exists, get its info
				if elem[6].text != "n/a":
					#get mat names
					temp_input = elem[6].text

					temp_short = ""
					temp_full = ""
					#set mat names
					for elem2 in units_root:
						if elem2[0].text == temp_input:
							temp_short = elem2[1].text
							temp_full = elem2[2].text
							break
					#add mat info to embed
					embed.add_field(value="x" + str(int(elem[7].text)) + " " + temp_short, name=temp_full,inline=False)
				#if fourth mat exists, get its info
				if elem[8].text != "n/a":
					#get mat names
					temp_input = elem[8].text

					temp_short = ""
					temp_full = ""
					#set mat names
					for elem2 in units_root:
						if elem2[0].text == temp_input:
							temp_short = elem2[1].text
							temp_full = elem2[2].text
							break
					#add mat info to embed
					embed.add_field(value="x" + str(int(elem[9].text)) + " " + temp_short, name=temp_full,inline=False)
				#if fifth mat exists, get its info
				if elem[10].text != "n/a":
					#get mat names
					temp_input = elem[10].text

					temp_short = ""
					temp_full = ""
					#set mat names
					for elem2 in units_root:
						if elem2[0].text == temp_input:
							temp_short = elem2[1].text
							temp_full = elem2[2].text
							break
					#add mat info to embed
					embed.add_field(value="x" + str(int(elem[11].text)) + " " + temp_short, name=temp_full,inline=False)

				await message.channel.send(embed=embed)
		#error case if the unit in question doesn't exist:
		if not awake_short:
			#create embed for warning
			embed = discord.Embed(title="Awakening Mats for " + input1, description="No information found. Make sure you include the rarity! Use $awaken_search to find a valid input, or message Deeakron M#6310 if you think there has been an error.", color=0x00ff00)
			#send embed to channel
			await message.channel.send(embed=embed)


	#same as above, except user enters unit being awakened to rather than from
	if message.content.startswith('$awaken_to '):
		#get input from message
		input1 = message.content[11:]

		#initialize some variables
		unit_target = ""

		target_short = ""
		target_full = ""

		#find the unit in question
		for elem in units_root:
			if elem[5].text.lower() == input1.lower():
				unit_target = elem[0].text
				target_short = elem[1].text
				target_full = elem[2].text
				break

		#initialize more variables
		unit_target2 = ""
		base_short = ""
		base_full = ""

		#find all units that target unit awakens to
		for elem in awakenings_root:
			if elem[1].text == unit_target:
				unit_target2 = elem[0].text
				for elem2 in units_root:
					if elem2[0].text == unit_target2:
						base_short = elem2[1].text
						base_full = elem2[2].text
						break
				embed = discord.Embed(title=base_short + "   ->   " + target_short, description=base_full + "   ->   " + target_full, color=0x00ff00)
				#if first mat exists, get its info
				if elem[2].text != "n/a":
					#get mat names
					temp_input = elem[2].text

					temp_short = ""
					temp_full = ""
					#set mat names
					for elem2 in units_root:
						if elem2[0].text == temp_input:
							temp_short = elem2[1].text
							temp_full = elem2[2].text
							break
					#add mat info to embed
					embed.add_field(value="x" + str(int(elem[3].text)) + " " + temp_short, name=temp_full,inline=False)
				#if second mat exists, get its info
				if elem[4].text != "n/a":
					#get mat names
					temp_input = elem[4].text

					temp_short = ""
					temp_full = ""
					#set mat names
					for elem2 in units_root:
						if elem2[0].text == temp_input:
							temp_short = elem2[1].text
							temp_full = elem2[2].text
							break
					#add mat info to embed
					embed.add_field(value="x" + str(int(elem[5].text)) + " " + temp_short, name=temp_full,inline=False)
				#if third mat exists, get its info
				if elem[6].text != "n/a":
					#get mat names
					temp_input = elem[6].text

					temp_short = ""
					temp_full = ""
					#set mat names
					for elem2 in units_root:
						if elem2[0].text == temp_input:
							temp_short = elem2[1].text
							temp_full = elem2[2].text
							break
					#add mat info to embed
					embed.add_field(value="x" + str(int(elem[7].text)) + " " + temp_short, name=temp_full,inline=False)
				#if fourth mat exists, get its info
				if elem[8].text != "n/a":
					#get mat names
					temp_input = elem[8].text

					temp_short = ""
					temp_full = ""
					#set mat names
					for elem2 in units_root:
						if elem2[0].text == temp_input:
							temp_short = elem2[1].text
							temp_full = elem2[2].text
							break
					#add mat info to embed
					embed.add_field(value="x" + str(int(elem[9].text)) + " " + temp_short, name=temp_full,inline=False)
				#if fifth mat exists, get its info
				if elem[10].text != "n/a":
					#get mat names
					temp_input = elem[10].text

					temp_short = ""
					temp_full = ""
					#set mat names
					for elem2 in units_root:
						if elem2[0].text == temp_input:
							temp_short = elem2[1].text
							temp_full = elem2[2].text
							break
					#add mat info to embed
					embed.add_field(value="x" + str(int(elem[11].text)) + " " + temp_short, name=temp_full,inline=False)

				await message.channel.send(embed=embed)
		#error case if the unit in question doesn't exist:
		if not base_short:
			#create embed for warning
			embed = discord.Embed(title="Awakening Mats for " + input1, description="No information found. Make sure you include the rarity! Use $awaken_search to find a valid input, or message Deeakron M#6310 if you think there has been an error.", color=0x00ff00)
			#send embed to channel
			await message.channel.send(embed=embed)

	if message.content.startswith('$awaken_search '):
		#get input from message
		input1 = message.content[15:]

		embed = discord.Embed(title="Inputs that contain '" + input1 + "':", description="", color=0x00ff00)

		valid_check = ""
		i = 0

		#find the unit in question
		for elem in units_root:
			if i < 20:
				if input1.lower() in elem[5].text.lower():
					embed.add_field(value=elem[5].text,name=elem[2].text,inline=False)
					valid_check = elem[5].text
					i += 1
			else:
				embed.add_field(value="Search limit exceeded.",name="End of Results",inline=False)
				break

		if valid_check:
			await message.channel.send(embed=embed)
		else:
			embed.add_field(value="No inputs found. Please double check you spelled it right, or contact Deeakron M#6310 if you think there is an error.", name="No results found.",inline=False)
			await message.channel.send(embed=embed)

	if message.content.startswith('$awaken_mat '):
		#get input from message
		input1 = message.content[12:]

		#initialize some variables
		unit_target = ""

		target_short = ""
		target_full = ""
		target_origin = ""
		target_cost = ""

		#find the unit in question
		for elem in units_root:
			if elem[5].text.lower() == input1.lower():
				target_short = elem[1].text
				target_full = elem[2].text
				target_origin = elem[3].text
				target_cost = int(elem[4].text)
				break
		if target_short:
			embed = discord.Embed(title="Information for " + target_short, description = "", color=0x00ff00)
			embed.add_field(value=target_full,name="Unit Full Title:",inline=False)
			embed.add_field(value=target_origin,name="Unit's Base form obtained from:",inline=False)
			embed.add_field(value=target_cost,name="Unit Cost:",inline=False)
			await message.channel.send(embed=embed)
		else:
			embed = discord.Embed(title="Information for " + input1, description = "No information found.", color = 0x00ff00)
			await message.channel.send(embed=embed)

	if message.content.startswith('$awaken_mat_used '):	

		input1 = message.content[17:]
		unit_target = ""

		target_short = ""
		target_full = ""
		i = 0

		#find the unit in question
		for elem in units_root:
			if elem[5].text.lower() == input1.lower():
				unit_target = elem[0].text
				target_short = elem[1].text
				target_full = elem[2].text
				break

		embed = discord.Embed(title=input1 + " is used to awaken:",description=" ",color=0x00ff00)
		unit_found = False
		for elem in awakenings_root:
			valid_check = False
			if elem[2].text == unit_target:
				valid_check = True
			elif elem[4].text == unit_target:
				valid_check = True
			elif elem[6].text == unit_target:
				valid_check = True
			elif elem[8].text == unit_target:
				valid_check = True
			elif elem[10].text == unit_target:
				valid_check = True
			if valid_check:
				unit_found = True
				j = 2
				unit_count = 0
				while j < 12:
					if elem[j].text == unit_target:
						unit_count += int(elem[j + 1].text)
					j += 2
				if i < 20:
					temp_input = elem[0].text
					temp_short = ""
					temp_full = ""
					#set mat names
					for elem2 in units_root:
						if elem2[0].text == temp_input:
							temp_short = elem2[1].text
							temp_full = elem2[2].text
							unit_statement = elem2[1].text + " - needs " + str(int(unit_count)) + "x to awaken"
							embed.add_field(value=unit_statement,name=elem2[2].text,inline=False)
							break
					i += 1
				if i >= 20:
					embed.add_field(value="Number of awakenings exceeded message limit.",name="End of Results ",inline=False)
					break
		if not unit_found:
			if target_short:
				embed.add_field(value="No awakenings found.",name="No Results",inline=False)
			else:	
				embed.add_field(value="No unit found; please make sure you gave the right input.",name="No Results ",inline=False)
		await message.channel.send(embed=embed)


	#get current bot version as well as list recent updates
	if message.content == ('$awaken_info'):
		embed = discord.Embed(title="Awakening Bot Mi-Go Information", description="", color=0x00ff00)
		embed.add_field(name="Current Bot Version", value=info_line[0],inline=False)
		embed.add_field(name="Bot Last Updated", value=info_line[1],inline=False)
		embed.add_field(name="Latest Global version info added", value=info_line[2],inline=False)
		embed.add_field(name="Latest Japanese version info added", value=info_line[3],inline=False)
		embed.add_field(name="Latest Taiwanese version info added", value=info_line[4],inline=False)
		embed.add_field(name="Database Last Updated", value=info_line[5],inline=False)
		await message.channel.send(embed=embed)


	if message.content == ('$waifu'):
		if(random.randint(1,2) == 1):
			embed = discord.Embed(title="   ", description="  ", color=0x00ff00)
			embed.set_image(url="https://cdn.discordapp.com/attachments/681578371666280463/681704912526377030/Unit1368.png")
			await message.channel.send(embed=embed)
		else:
			embed = discord.Embed(title="   ", description="  ", color=0x00ff00)
			embed.set_image(url="https://cdn.discordapp.com/attachments/681578371666280463/878352118724059157/Unit15073.png")
			await message.channel.send(embed=embed)

	if message.content == ('$thicc'):
		if(random.randint(1,2) == 1):
			embed = discord.Embed(title="   ", description="  ", color=0x00ff00)
			embed.set_image(url="https://cdn.discordapp.com/attachments/681578371666280463/682011823553511431/Screenshot_20200225-0152162.png")
			await message.channel.send(embed=embed)
		else:
			embed = discord.Embed(title="   ", description="  ", color=0x00ff00)
			embed.set_image(url="https://cdn.discordapp.com/attachments/681578371666280463/878353613427212338/Screenshot_20210820-1502522.png")
			await message.channel.send(embed=embed)
		#pic = discord.File("bernoulli.png",filename="bernoulli.png",spoiler=False)
		#await message.channel.send(pic)

	if message.content == ('$awaken_help'):
		embed = discord.Embed(title="Crash Fever Awakening Materials Bot Commands", description="  ", color=0x00ff00)
		embed.add_field(name="$awaken_to <unit name>", value = "Lists the awakening mats for the given unit; <unit name> should list the unit that is being awakened to (i.e. 6 Star form).", inline=False)
		embed.add_field(name="$awaken_from <unit name>", value = "Lists the awakening mats for the given unit; <unit name> should list the unit that is being awakened from (i.e. 5 Star form).", inline=False)
		embed.add_field(name="$awaken_mat <unit name>", value = "Lists information about the given material/unit.", inline=False)
		embed.add_field(name="$awaken_mat_used <unit name>", value = "Lists all units that the specific form of the unit given is used for.", inline=False)
		embed.add_field(name="$awaken_search <unit name>", value = "Lists all valid inputs with the given string.", inline=False)
		embed.add_field(name="$awaken_info", value="Lists information about the bot and database and when it was last updated.",inline=False)
		embed.add_field(name="$waifu or $thicc", value = "Shows a picture of best waifu.", inline=False)
		embed.add_field(name ="credits", value = "Bot and spreadsheet created by Deeakron M#6310; some assistance was given by Laice#0002. Server setup was mostly done by Deeakron M's other brother (not Deeakron L)", inline=False)
		await message.channel.send(embed=embed)

	if message.content == "$stop" and message.author.id == 318154934132670464:
		await message.channel.send("Shutting down...")
		await client.close()
client.run(os.environ.get('CBOT_TOKEN'))