import discord
import pyodbc
import os

#set up
client = discord.Client()

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\xls\CFD.accdb;')

update_info = open(r"C:\xls\update_info.txt")
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

	#lists awakening mats to awaken the given unit
	if message.content.startswith('$awaken_from '):
		#send query to database
		query = "{CALL AwakenFrom(?)}"
		input1 = message.content[13:]
		cursor = conn.execute(query,input1)
		#initialize variables
		awake_short = ""
		awake_full = ""
		#gather information about each awakening
		for row in cursor:
			#get names for unit that is being awakened to
			query2 = "{CALL Title(?)}"
			input2 = ""
			input2 = row[1]
			cursor2 = conn.execute(query2,input2)
			#set names for unit that is being awakened to
			for subrow in cursor2:
				awake_short = subrow[1]
				awake_full = subrow[2]
			cursor2.close()
			#create embed with title stating beginning form and ending form, with full titles listed as well
			embed = discord.Embed(title=row[13] + "   ->   " + awake_short, description=row[14] + "   ->   " + awake_full, color=0x00ff00)
			#if first mat exists, add it's information
			if row[2] != "n/a":
				#get mat names
				temp_query = "{CALL Title(?)}"
				temp_input = row[2]
				temp_cursor = conn.execute(temp_query,temp_input)
				temp_short = ""
				temp_full = ""
				#set mat names
				for subrow in temp_cursor:
					temp_short = subrow[1]
					temp_full = subrow[2]
				temp_cursor.close()
				#add mat info to embed
				embed.add_field(value="x" + str(int(row[3])) + " " + temp_short, name=temp_full,inline=False)
			#if second mat exists, add it's information
			if row[4] != "n/a":
				#get mat names
				temp_query = "{CALL Title(?)}"
				temp_input = row[4]
				temp_cursor = conn.execute(temp_query,temp_input)
				temp_short = ""
				temp_full = ""
				#set mat names
				for subrow in temp_cursor:
					temp_short = subrow[1]
					temp_full = subrow[2]
				temp_cursor.close()
				#add mat info to embed
				embed.add_field(value="x" + str(int(row[5])) + " " + temp_short, name=temp_full,inline=False)
			#if third mat exists, add it's information
			if row[6] != "n/a":
				#get mat names
				temp_query = "{CALL Title(?)}"
				temp_input = row[6]
				temp_cursor = conn.execute(temp_query,temp_input)
				temp_short = ""
				temp_full = ""
				#set mat names
				for subrow in temp_cursor:
					temp_short = subrow[1]
					temp_full = subrow[2]
				temp_cursor.close()
				#add mat info to embed
				embed.add_field(value="x" + str(int(row[7])) + " " + temp_short, name=temp_full,inline=False)
			#if fourth mat exists, add it's information
			if row[8] != "n/a":
				#get mat names
				temp_query = "{CALL Title(?)}"
				temp_input = row[8]
				temp_cursor = conn.execute(temp_query,temp_input)
				temp_short = ""
				temp_full = ""
				#set mat names
				for subrow in temp_cursor:
					temp_short = subrow[1]
					temp_full = subrow[2]
				temp_cursor.close()
				#add mat info to embed
				embed.add_field(value="x" + str(int(row[9])) + " " + temp_short, name=temp_full,inline=False)
			#if fifth mat exists, add it's information
			if row[10] != "n/a":
				#get mat names
				temp_query = "{CALL Title(?)}"
				temp_input = row[10]
				temp_cursor = conn.execute(temp_query,temp_input)
				temp_short = ""
				temp_full = ""
				#set mat names
				for subrow in temp_cursor:
					temp_short = subrow[1]
					temp_full = subrow[2]
				temp_cursor.close()
				#add mat info to embed
				embed.add_field(value="x" + str(int(row[11])) + " " + temp_short, name=temp_full,inline=False)
			#send embed to channel
			await message.channel.send(embed=embed)
		#if the names for the unit that is being awakened to weren't obtained (because no results were found), return an error message
		if not awake_short:
			#create embed for warning
			embed = discord.Embed(title="Awakening Mats for " + input1, description="No information found. Use $awaken_search to find a valid input, or message Deeakron M#6310 if you think there has been an error.", color=0x00ff00)
			#send embed to channel
			await message.channel.send(embed=embed)
		#finish connection
		conn.commit()
		cursor.close()

	#same as above, except user enters unit being awakened to rather than from
	if message.content.startswith('$awaken_to '):
		#send query to database
		query = "{CALL AwakenTo(?)}"
		input1 = message.content[11:]
		cursor = conn.execute(query,input1)
		#initialize variables
		base_short = ""
		base_full = ""
		#gather information about each awakening
		for row in cursor:
			#get names for unit that is being awakened from
			query2 = "{CALL Title(?)}"
			input2 = row[0]
			cursor2 = conn.execute(query2,input2)
			#set names for unit that is being awakened from
			for subrow in cursor2:
				base_short = subrow[1]
				base_full = subrow[2]
			cursor2.close()
			#create embed with title listing beginning and ending unit, with full names included
			embed = discord.Embed(title=base_short + "   ->   " + row[13], description=base_full + "   ->   " + row[14], color=0x00ff00)
			#if first mat exists, get its info
			if row[2] != "n/a":
				#get mat names
				temp_query = "{CALL Title(?)}"
				temp_input = row[2]
				temp_cursor = conn.execute(temp_query,temp_input)
				temp_short = ""
				temp_full = ""
				#set mat names
				for subrow in temp_cursor:
					temp_short = subrow[1]
					temp_full = subrow[2]
				temp_cursor.close()
				#add mat info to embed
				embed.add_field(value="x" + str(int(row[3])) + " " + temp_short, name=temp_full,inline=False)
			#if second mat exists, get its info
			if row[4] != "n/a":
				#get mat names
				temp_query = "{CALL Title(?)}"
				temp_input = row[4]
				temp_cursor = conn.execute(temp_query,temp_input)
				temp_short = ""
				temp_full = ""
				#set mat names
				for subrow in temp_cursor:
					temp_short = subrow[1]
					temp_full = subrow[2]
				temp_cursor.close()
				embed.add_field(value="x" + str(int(row[5])) + " " + temp_short, name=temp_full,inline=False)
			if row[6] != "n/a":
				temp_query = "{CALL Title(?)}"
				temp_input = row[6]
				temp_cursor = conn.execute(temp_query,temp_input)
				temp_short = ""
				temp_full = ""
				for subrow in temp_cursor:
					temp_short = subrow[1]
					temp_full = subrow[2]
				temp_cursor.close()
				embed.add_field(value="x" + str(int(row[7])) + " " + temp_short, name=temp_full,inline=False)
			if row[8] != "n/a":
				temp_query = "{CALL Title(?)}"
				temp_input = row[8]
				temp_cursor = conn.execute(temp_query,temp_input)
				temp_short = ""
				temp_full = ""
				for subrow in temp_cursor:
					temp_short = subrow[1]
					temp_full = subrow[2]
				temp_cursor.close()
				embed.add_field(value="x" + str(int(row[9])) + " " + temp_short, name=temp_full,inline=False)
			if row[10] != "n/a":
				temp_query = "{CALL Title(?)}"
				temp_input = row[10]
				temp_cursor = conn.execute(temp_query,temp_input)
				temp_short = ""
				temp_full = ""
				for subrow in temp_cursor:
					temp_short = subrow[1]
					temp_full = subrow[2]
				temp_cursor.close()
				embed.add_field(value="x" + str(int(row[11])) + " " + temp_short, name=temp_full,inline=False)
			await message.channel.send(embed=embed)
			#await message.channel.send(row[14])
		if not base_short:
			embed = discord.Embed(title="Awakening Mats for " + input1, description="No information found. Use $awaken_search to find a valid input, or message Deeakron M#6310 if you think there has been an error.", color=0x00ff00)
			await message.channel.send(embed=embed)
		conn.commit()
		cursor.close()

	if message.content.startswith('$awaken_search '):
		query = "{CALL AwakenSearch(?)}"
		input1 = message.content[15:]
		embed = discord.Embed(title="Inputs that contain '" + input1 + "':", description="", color=0x00ff00)
		cursor = conn.execute(query,input1)
		valid_check = ""
		i = 0
		for row in cursor:
			if i < 20:
				embed.add_field(value=row[5],name=row[2],inline=False)
				valid_check = row[5]
				i += 1
		if i >= 20:
			embed.add_field(value="Search limit exceeded.",name="End of Results",inline=False)
		cursor.close()
		if valid_check:
			await message.channel.send(embed=embed)
		else:
			embed.add_field(value="No inputs found. Please double check you spelled it right, or contact Deeakron M#6310 if you think there is an error.", name="No results found.",inline=False)
			await message.channel.send(embed=embed)
		conn.commit()

	if message.content.startswith('$awaken_mat '):
		query = "{CALL MatsInfo(?)}"
		input1 = message.content[12:]
		cursor = conn.execute(query,input1)
		unit_short = ""
		unit_full = ""
		unit_origin = ""
		unit_cost = ""
		for row in cursor:
			unit_short = row[1]
			unit_full = row[2]
			unit_origin = row[3]
			unit_cost = int(row[4])
		if unit_short:
			embed = discord.Embed(title="Information for " + unit_short, description = "", color=0x00ff00)
			embed.add_field(value=unit_full,name="Unit Full Title:",inline=False)
			embed.add_field(value=unit_origin,name="Unit's Base form obtained from:",inline=False)
			embed.add_field(value=unit_cost,name="Unit Cost:",inline=False)
			await message.channel.send(embed=embed)
		else:
			embed = discord.Embed(title="Information for " + input1, description = "No information found.", color = 0x00ff00)
			await message.channel.send(embed=embed)
		cursor.close()
		conn.commit()

	if message.content.startswith('$awaken_mat_used '):	
		query = "{CALL MatsUsed(?)}"
		input1 = message.content[17:]
		cursor = conn.execute(query,input1)
		unit_short = ""
		unit_full = ""
		i = 0
		embed = discord.Embed(title=input1 + " is used to awaken:",description=" ",color=0x00ff00)
		for row in cursor:
			unit_short = row[13]
			unit_full = row[14]
			
			#for new_row in cursor:
			if i < 20:
				temp_query = "{CALL Title(?)}"
				temp_input = row[0]
				temp_cursor = conn.execute(temp_query,temp_input)
				for subrow in temp_cursor:
					embed.add_field(value=subrow[1],name=subrow[2],inline=False)
				i += 1
				temp_cursor.close()
		if i >= 20:
				embed.add_field(value="Number of awakenings exceeded message limit.",name="End of Results ",inline=False)
		if not unit_short:
			unit_temp = ""
			temp_query = "{CALL MatsInfo(?)}"
			temp_input = input1
			temp_cursor = conn.execute(temp_query,temp_input)
			for subrow in temp_cursor:
				unit_temp = subrow[0]
			if unit_temp:
				embed.add_field(value="No awakenings found.",name="No Results",inline=False)
			else:	
				embed.add_field(value="No unit found; please make sure you gave the right input.",name="No Results ",inline=False)
		cursor.close()
		await message.channel.send(embed=embed)
		conn.commit()

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
		embed = discord.Embed(title="   ", description="  ", color=0x00ff00)
		embed.set_image(url="https://cdn.discordapp.com/attachments/681578371666280463/681704912526377030/Unit1368.png")
		await message.channel.send(embed=embed)

	if message.content == ('$thicc'):
		embed = discord.Embed(title="   ", description="  ", color=0x00ff00)
		embed.set_image(url="https://cdn.discordapp.com/attachments/681578371666280463/682011823553511431/Screenshot_20200225-0152162.png")
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
		await client.logout()
client.run(os.environ.get('CBOT_TOKEN'))