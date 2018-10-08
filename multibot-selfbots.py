import discord
import asyncio
import os





#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

active_1 = True
active_2 = True
active_3 = True
active_4 = True
active_5 = True
active_6 = True
active_7 = True
active_8 = True
active_9 = True
active_10 = False
active_11 = False
active_12 = True
active_13 = True
active_14 = True
active_15 = True
active_16 = True
active_17 = True
active_18 = True
active_19 = True
active_20 = False



#Shopify Selfbot
selfbot_1 = True
token_1 = str(os.environ.get("TOKEN_1"))
commands_server_id_1 = "416173426252972052"
commands_channel_id_1 = "461496846464843780"

#SNKRS Selfbot
selfbot_2 = True
token_2 = str(os.environ.get("TOKEN_2"))
commands_server_id_2 = "416173426252972052"
commands_channel_id_2 = "461504136840740874"

#Supreme Selfbot
selfbot_3 = True
token_3 = str(os.environ.get("TOKEN_3"))
commands_server_id_3 = "416173426252972052"
commands_channel_id_3 = "483375885983154186"

#DSM Selfbot
selfbot_4 = True
token_4 = str(os.environ.get("TOKEN_4"))
commands_server_id_4 = "416173426252972052"
commands_channel_id_4 = "483037696457965570"

#Restocks Selfbot
selfbot_5 = True
token_5 = str(os.environ.get("TOKEN_5"))
commands_server_id_5 = "416173426252972052"
commands_channel_id_5 = "483041482723295252"



#Funko Selfbot
selfbot_6 = True
token_6 = str(os.environ.get("TOKEN_6"))
commands_server_id_6 = "416173426252972052"
commands_channel_id_6 = "483042673138073600"

#HQ Trivia Selfbot
selfbot_7 = True
token_7 = str(os.environ.get("TOKEN_7"))
commands_server_id_7 = "416173426252972052"
commands_channel_id_7 = "478370073430589442"

#HQ Trivia US
selfbot_8 = True
token_8 = str(os.environ.get("TOKEN_8"))
commands_server_id_8 = "416173426252972052"
commands_channel_id_8 = "484108197410635786"

#HQEU
selfbot_9 = True
token_9 = str(os.environ.get("TOKEN_9"))
commands_server_id_9 = "416173426252972052"
commands_channel_id_9 = "484108219069759524"

#HQDE
selfbot_10 = True
token_10 = str(os.environ.get("TOKEN_10"))
commands_server_id_10 = "416173426252972052"
commands_channel_id_10 = "484108233854943262"



#HQAU
selfbot_11 = True
token_11 = str(os.environ.get("TOKEN_11"))
commands_server_id_11 = "416173426252972052"
commands_channel_id_11 = "484108251345190933"

#Leaks Bot 
selfbot_12 = True
token_12 = str(os.environ.get("TOKEN_12"))
commands_server_id_12 = "416173426252972052"
commands_channel_id_12 = "487924740414242816"

#Sitelists bot 
selfbot_13 = True
token_13 = str(os.environ.get("TOKEN_13"))
commands_server_id_13 = "416173426252972052"
commands_channel_id_13 = "487924835041673216"

#Kith
selfbot_14 = True
token_14 = str(os.environ.get("TOKEN_14"))
commands_server_id_14 = "416173426252972052"
commands_channel_id_14 = "491852118156902400"

#Undefeated
selfbot_15 = True
token_15 = str(os.environ.get("TOKEN_15"))
commands_server_id_15 = "416173426252972052"
commands_channel_id_15 = "491852157260136456"



#bodega
selfbot_16 = True
token_16 = str(os.environ.get("TOKEN_16"))
commands_server_id_16 = "416173426252972052"
commands_channel_id_16 = "491852205029195776"

#Snkrs cn
selfbot_17 = True
token_17 = str(os.environ.get("TOKEN_17"))
commands_server_id_17 = "416173426252972052"
commands_channel_id_17 = "491852243662798854"

#brickseek
selfbot_18 = True
token_18 = str(os.environ.get("TOKEN_18"))
commands_server_id_18 = "416173426252972052"
commands_channel_id_18 = "491852280900091904"

# Customs
selfbot_19 = True
token_19 = str(os.environ.get("TOKEN_19"))
commands_server_id_19 = "000000000000000000"
commands_channel_id_19 = "000000000000000000"

#Leave a comment here with the name and function of the bot (to make it easier to manage all the bots)
selfbot_20 = True
token_20 = str(os.environ.get("TOKEN_20"))
commands_server_id_20 = "000000000000000000"
commands_channel_id_20 = "000000000000000000"


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------





globaldata = {}





client = discord.Client()

bot_1 = discord.Client()
bot_1.unique_id = "001"
bot_1.commands_server_id = commands_server_id_1
bot_1.commands_channel_id = commands_channel_id_1

bot_2 = discord.Client()
bot_2.unique_id = "002"
bot_2.commands_server_id = commands_server_id_2
bot_2.commands_channel_id = commands_channel_id_2

bot_3 = discord.Client()
bot_3.unique_id = "003"
bot_3.commands_server_id = commands_server_id_3
bot_3.commands_channel_id = commands_channel_id_3

bot_4 = discord.Client()
bot_4.unique_id = "004"
bot_4.commands_server_id = commands_server_id_4
bot_4.commands_channel_id = commands_channel_id_4

bot_5 = discord.Client()
bot_5.unique_id = "005"
bot_5.commands_server_id = commands_server_id_5
bot_5.commands_channel_id = commands_channel_id_5

bot_6 = discord.Client()
bot_6.unique_id = "006"
bot_6.commands_server_id = commands_server_id_6
bot_6.commands_channel_id = commands_channel_id_6

bot_7 = discord.Client()
bot_7.unique_id = "007"
bot_7.commands_server_id = commands_server_id_7
bot_7.commands_channel_id = commands_channel_id_7

bot_8 = discord.Client()
bot_8.unique_id = "008"
bot_8.commands_server_id = commands_server_id_8
bot_8.commands_channel_id = commands_channel_id_8

bot_9 = discord.Client()
bot_9.unique_id = "009"
bot_9.commands_server_id = commands_server_id_9
bot_9.commands_channel_id = commands_channel_id_9

bot_10 = discord.Client()
bot_10.unique_id = "010"
bot_10.commands_server_id = commands_server_id_10
bot_10.commands_channel_id = commands_channel_id_10

bot_11 = discord.Client()
bot_11.unique_id = "011"
bot_11.commands_server_id = commands_server_id_11
bot_11.commands_channel_id = commands_channel_id_11

bot_12 = discord.Client()
bot_12.unique_id = "012"
bot_12.commands_server_id = commands_server_id_12
bot_12.commands_channel_id = commands_channel_id_12

bot_13 = discord.Client()
bot_13.unique_id = "013"
bot_13.commands_server_id = commands_server_id_13
bot_13.commands_channel_id = commands_channel_id_13

bot_14 = discord.Client()
bot_14.unique_id = "014"
bot_14.commands_server_id = commands_server_id_14
bot_14.commands_channel_id = commands_channel_id_14

bot_15 = discord.Client()
bot_15.unique_id = "015"
bot_15.commands_server_id = commands_server_id_15
bot_15.commands_channel_id = commands_channel_id_15

bot_16 = discord.Client()
bot_16.unique_id = "016"
bot_16.commands_server_id = commands_server_id_16
bot_16.commands_channel_id = commands_channel_id_16

bot_17 = discord.Client()
bot_17.unique_id = "017"
bot_17.commands_server_id = commands_server_id_17
bot_17.commands_channel_id = commands_channel_id_17

bot_18 = discord.Client()
bot_18.unique_id = "018"
bot_18.commands_server_id = commands_server_id_18
bot_18.commands_channel_id = commands_channel_id_18

bot_19 = discord.Client()
bot_19.unique_id = "019"
bot_19.commands_server_id = commands_server_id_19
bot_19.commands_channel_id = commands_channel_id_19

bot_20 = discord.Client()
bot_20.unique_id = "020"
bot_20.commands_server_id = commands_server_id_20
bot_20.commands_channel_id = commands_channel_id_20





async def edit_check(bot):

	global globaldata

	await bot.wait_until_ready()

	await asyncio.sleep(5)
	edit_msg_list = globaldata[bot.unique_id]["edit_msg_list"]

	while not bot.is_closed:
		await asyncio.sleep(0.1)
		for edit_msg in edit_msg_list:
			if edit_msg["copy_message_object"].content != edit_msg["message_content"]:
				try:
					await bot.edit_message(edit_msg["post_message_object"], new_content=text_message_filter(edit_msg["copy_message_object"].content, bot))
					edit_msg_list[edit_msg_list.index(edit_msg)]["message_content"] = edit_msg["copy_message_object"].content
				except Exception:
					pass
				
				
				
				
				
def text_message_filter(original_message, bot):

	global globaldata

	case_sensitive_wordlist = globaldata[bot.unique_id]["filedata"]["case_sensitive_wordlist"]
	wordlist = globaldata[bot.unique_id]["filedata"]["wordlist"]

	local_new_message = original_message
	if case_sensitive_wordlist:
		for word in wordlist:
			local_new_message = local_new_message.replace(word, "")
	else:
		lowercase_message = local_new_message.lower()
		new_letters = list(local_new_message)
		letter_index = 0
		uppercase_letter_indexes = []
		for letter in new_letters:
			if letter.isupper():
				uppercase_letter_indexes.append(letter_index)
			letter_index += 1
		del letter_index
		for word in wordlist:
			replacement_word = len(word) * "�"
			lowercase_message = lowercase_message.replace(word.lower(), replacement_word)
		lowercase_letters = list(lowercase_message)
		for letter_index in uppercase_letter_indexes:
			lowercase_letters[letter_index] = lowercase_letters[letter_index].upper()
		local_new_message = "".join(lowercase_letters)
		local_new_message = local_new_message.replace("�", "")
	return local_new_message





async def on_ready_code(bot):

	global globaldata

	await bot.wait_until_ready()

	globaldata[bot.unique_id] = {
		"filedata" : {
					"setup_info" : {
								"copy_server_ids" : [],
								"copy_channel_ids" : [],
								"post_server_ids" : [],
								"post_channel_ids" : []
								},
					"memberlist" : [],
					"wordlist" : [],
					"case_sensitive_wordlist" : True
					},
		"edit_msg_list" : [],
		"edit_msg_list_length" : 10,
		"adding_copy_server" : False,
		"adding_copy_channel" : False,
		"adding_post_server" : False,
		"adding_post_channel" : False,
		"removing_copy_server" : False,
		"removing_copy_channel" : False,
		"removing_post_server" : False,
		"removing_post_channel" : False
	}


	

	
	if bot.unique_id == "001":
		globaldata[bot.unique_id]["filedata"] = {"setup_info": {"copy_server_ids": ["477315511596744704"], "copy_channel_ids": ["484867968719781900"], "post_server_ids": ["456445523960791042"], "post_channel_ids": ["461494200979030016"]}, "memberlist": [], "wordlist": [], "case_sensitive_wordlist": True, "header_text": "", "footer_text": "Restocks", "footer_icon": ""}

	elif bot.unique_id == "002":
		globaldata[bot.unique_id]["filedata"] = {"setup_info": {"copy_server_ids": ["477315511596744704"], "copy_channel_ids": ["484868847724265485"], "post_server_ids": ["456445523960791042"], "post_channel_ids": ["461635403003199499"]}, "memberlist": [], "wordlist": [], "case_sensitive_wordlist": True, "header_text": "", "footer_text": "Restocks", "footer_icon": ""}

	elif bot.unique_id == "003":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["430997261066174464"], "copy_channel_ids" : ["440240999185252352"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["483061720852594729"]}, "memberlist" : [], "wordlist" : [], "case_sensitive_wordlist" : True, "header_text": "Restocks", "footer_text": "", "footer_icon": ""}
		
	elif bot.unique_id == "004":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["430997261066174464"], "copy_channel_ids" : ["445140469337423882"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["481587952468623370"]}, "memberlist" : [], "wordlist" : [], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "", "footer_icon": ""}
		
	elif bot.unique_id == "005":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["430997261066174464"], "copy_channel_ids" : ["445140672866156545"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["481587970462449664"]}, "memberlist" : [], "wordlist" : [], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "", "footer_icon": ""}

	elif bot.unique_id == "006":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["430997261066174464"], "copy_channel_ids" : ["445140488035631104"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["481587994399342602"]}, "memberlist" : [], "wordlist" : [], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "", "footer_icon": ""}

	elif bot.unique_id == "007":
		globaldata[bot.unique_id]["filedata"] = {"setup_info": {"copy_server_ids": ["437786295595696131"], "copy_channel_ids": ["442475302619316236", "442475616105791508", "461691021248561163", "468819343229059072"], "post_server_ids": ["456445523960791042"], "post_channel_ids": ["459515052765216768"]}, "memberlist": ["463206389527871509"], "wordlist": ["\ud83d\udcb0 Prize is currently $0.01/person", "\ud83d\udcb0 Prize is currently $0.02/person", "@", "!", "-30", "+9", "+8", "+7", "+6", "+5", "+4", "points"], "case_sensitive_wordlist": True, "header_text": "", "footer_text": "", "footer_icon": ""}

	elif bot.unique_id == "008":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["437786295595696131"], "copy_channel_ids" : ["442475302619316236"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["484138369794965535"]}, "memberlist" : ["463206389527871509"], "wordlist" : [], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "", "footer_icon": ""}

	elif bot.unique_id == "009":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["437786295595696131"], "copy_channel_ids" : ["442475616105791508"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["484138383484911627"]}, "memberlist" : ["463206389527871509"], "wordlist" : [], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "", "footer_icon": ""}

	elif bot.unique_id == "010":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["437786295595696131"], "copy_channel_ids" : ["461691021248561163"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["484138397930225664"]}, "memberlist" : ["463206389527871509"], "wordlist" : [], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "", "footer_icon": ""}

	elif bot.unique_id == "011":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["437786295595696131"], "copy_channel_ids" : ["468819343229059072"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["484138416276111375"]}, "memberlist" : ["463206389527871509"], "wordlist" : [], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "", "footer_icon": ""}

	elif bot.unique_id == "012":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["477522374951174146"], "copy_channel_ids" : ["477530276289970196", "478275863415357450", "484571706191773717", "488110555660419072"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["487923777301250048"]}, "memberlist" : ["389630457202868224", "225795746245378049"], "wordlist" : ["BBG"], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "", "footer_icon": ""}

	elif bot.unique_id == "013":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["477522374951174146", "250671450640351232"], "copy_channel_ids" : ["486922812402040850", "482636645078925312", "410843954901286922"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["487923825338613763"]}, "memberlist" : ["398921783119708160", "237899576093179904", "214072601096617984"], "wordlist" : ["BBG"], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "", "footer_icon": ""}

	elif bot.unique_id == "014":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["477315511596744704"], "copy_channel_ids" : ["485907088447373314"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["491854154935959554"]}, "memberlist" : [], "wordlist" : [", Wop"], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "Restocks", "footer_icon": ""}

	elif bot.unique_id == "015":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["477315511596744704"], "copy_channel_ids" : ["485633425403936789"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["491854186737041411"]}, "memberlist" : [], "wordlist" : [", Wop"], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "Restocks", "footer_icon": ""}

	elif bot.unique_id == "016":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["477315511596744704"], "copy_channel_ids" : ["485907138020114434"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["491854201505447956"]}, "memberlist" : [], "wordlist" : [", Wop"], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "Restocks", "footer_icon": ""}

	elif bot.unique_id == "017":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["477315511596744704"], "copy_channel_ids" : ["485633219358621706"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["491854212796383234"]}, "memberlist" : [], "wordlist" : [], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "Restocks", "footer_icon": ""}

	elif bot.unique_id == "018":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["477315511596744704"], "copy_channel_ids" : ["485901935753560066"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["491854232404623360"]}, "memberlist" : [], "wordlist" : [], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "Restocks", "footer_icon": ""}

	elif bot.unique_id == "019":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : ["477315511596744704"], "copy_channel_ids" : ["483356028025438209"], "post_server_ids" : ["456445523960791042"], "post_channel_ids" : ["491854242882256897"]}, "memberlist" : [], "wordlist" : ["Site", "Link"], "case_sensitive_wordlist" : True, "header_text": "Links", "footer_text": "Custom Restocks", "footer_icon": ""}

	elif bot.unique_id == "020":
		globaldata[bot.unique_id]["filedata"] = {"setup_info" : {"copy_server_ids" : [], "copy_channel_ids" : [], "post_server_ids" : [], "post_channel_ids" : []}, "memberlist" : [], "wordlist" : [], "case_sensitive_wordlist" : True, "header_text": "", "footer_text": "", "footer_icon": ""}





	print (bot.user.name + " is ready")
	print ("ID: " + bot.user.id)





async def on_message_code(bot, message):

	global globaldata

	try:
		filedata = globaldata[bot.unique_id]["filedata"]
	except KeyError as e:
		await asyncio.sleep(3)
		filedata = globaldata[bot.unique_id]["filedata"]

	copy_server_ids = filedata["setup_info"]["copy_server_ids"]
	copy_channel_ids = filedata["setup_info"]["copy_channel_ids"]
	post_server_ids = filedata["setup_info"]["post_server_ids"]
	post_channel_ids = filedata["setup_info"]["post_channel_ids"]
	memberlist = filedata["memberlist"]
	wordlist = filedata["wordlist"]
	case_sensitive_wordlist = filedata["case_sensitive_wordlist"]
	header_text = filedata["header_text"]
	footer_text = filedata["footer_text"]
	footer_icon = filedata["footer_icon"]

	edit_msg_list = globaldata[bot.unique_id]["edit_msg_list"]
	edit_msg_list_length = globaldata[bot.unique_id]["edit_msg_list_length"]

	adding_copy_server = globaldata[bot.unique_id]["adding_copy_server"]
	adding_copy_channel = globaldata[bot.unique_id]["adding_copy_channel"]
	adding_post_server = globaldata[bot.unique_id]["adding_post_server"]
	adding_post_channel = globaldata[bot.unique_id]["adding_post_channel"]

	removing_copy_server = globaldata[bot.unique_id]["removing_copy_server"]
	removing_copy_channel = globaldata[bot.unique_id]["removing_copy_channel"]
	removing_post_server = globaldata[bot.unique_id]["removing_post_server"]
	removing_post_channel = globaldata[bot.unique_id]["removing_post_channel"]

	commands_server_id = bot.commands_server_id
	commands_channel_id = bot.commands_channel_id




	if message.channel != None:
		if message.author.id != bot.user.id:
			if (message.server.id == commands_server_id) and (message.channel.id == commands_channel_id):

				# If block for all the commands.

				if (not adding_copy_server) and (not adding_copy_channel) and (not adding_post_server) and (not adding_post_channel) and (not removing_copy_server) and (not removing_copy_channel) and (not removing_post_server) and (not removing_post_channel):



					####################################################################################################
					####################################################################################################

					if message.content == "ping":
						await bot.send_message(message.channel, "pong")

					elif (message.content[:12] == "!memberlist ") or (message.content == "!memberlist"):
						if (copy_server_ids != []) and (copy_channel_ids != []):

							#!MEMBERLIST ADD

							if (message.content[:16] == "!memberlist add ") or (message.content == "!memberlist add"):
								if (message.content[:20] == "!memberlist add all ") or (message.content == "!memberlist add all"):
									count = 0
									for copy_server_id in copy_server_ids:
										for member in bot.get_server(copy_server_id).members:
											if not (member.id in memberlist):
												memberlist.append(member.id)
												count += 1
									filedata["memberlist"] = memberlist		#SAVE TO FILE
									if count == 1:
										await bot.send_message(message.channel, """**[1] member was added to the memberlist.**""")
									else:
										await bot.send_message(message.channel, """**[{0}] members were added to the memberlist.**""".format(str(count)))
									del count
								else:
									temp_bool = True
									for copy_server_id in copy_server_ids:
										for member in bot.get_server(copy_server_id).members:
											if (message.content[16:] == member.name) or (message.content[16:] == member.id):
												if member.id in memberlist:
													await bot.send_message(message.channel, """**The member *{0} ({1})* is already in the memberlist.**
	**Use the command *!memberlist* to see all the members who have their messages currently being copied.**
	""".format(member.name, member.id))
												else:
													memberlist.append(member.id)
													filedata["memberlist"] = memberlist		#SAVE TO FILE
													await bot.send_message(message.channel, """**The member *{0} ({1})* has been added to the memberlist.**
	""".format(member.name, member.id))
												temp_bool = False
												break
										if (not temp_bool):
											break
									if temp_bool:
										if message.content.strip()[:16] == "!memberlist add ":
											await bot.send_message(message.channel, """**Invalid member - does not exist**""")
										await bot.send_message(message.channel, """**Here are all the members in the copy servers.**
	**Use the command *!memberlist add member* to add a member to the memberlist.**""")
										for copy_server_id in copy_server_ids:
											copy_server_object = bot.get_server(copy_server_id)
											await bot.send_message(message.channel, """**{0} ({1})**""".format(copy_server_object.name, copy_server_object.id))
											for member in copy_server_object.members:
												await bot.send_message(message.channel, """• {0} ({1})""".format(member.name, member.id))
									del temp_bool

							#!MEMBERLIST REMOVE

							elif (message.content[:19] == "!memberlist remove ") or (message.content == "!memberlist remove"):
								if len(memberlist) > 0:
									if (message.content[:23] == "!memberlist remove all ") or (message.content == "!memberlist remove all"):
										count = len(memberlist)
										memberlist = []
										filedata["memberlist"] = memberlist		#SAVE TO FILE
										if count == 1:
											await bot.send_message(message.channel, """**[1] member was removed from the memberlist.**""")
										else:
											await bot.send_message(message.channel, """**[{0}] members were removed from the memberlist.**""".format(str(count)))
										del count
									else:
										temp_bool = True
										for member_id in memberlist:
											for copy_server_id in copy_server_ids:
												try:
													member_object = bot.get_server(copy_server_id).get_member(member_id)
												except Exception:
													pass
												else:
													if (message.content[19:] == member_object.name) or (message.content[19:] == member_object.id):
														memberlist.remove(member_object.id)
														filedata["memberlist"] = memberlist		#SAVE TO FILE
														await bot.send_message(message.channel, """**The member *{0} ({1})* has been removed from the memberlist.**
	""".format(member_object.name, member_object.id))
														temp_bool = False
														break
										if temp_bool:
											if message.content.strip()[:19] == "!memberlist remove ":
												await bot.send_message(message.channel, """**Invalid member - not in memberlist**""")
											await bot.send_message(message.channel, """**Here are all the members in the memberlist (the members who have their messages currently being copied).**
	**Use the command *!memberlist remove member* to remove a member from the memberlist**""")
											for member_id in memberlist:
												for copy_server_id in copy_server_ids:
													try:
														member_object = bot.get_server(copy_server_id).get_member(member_id)
														await bot.send_message(message.channel, """• {0} ({1})""".format(member_object.name, member_object.id))
													except Exception:
														pass
										del temp_bool
								else:
									await bot.send_message(message.channel, """**There are currently no members in the memberlist.**
	**For more commands on the memberlist, use the command *!help*.**""")

							#!MEMBERLIST

							else:
								if len(memberlist) > 0:
									await bot.send_message(message.channel, """**[MEMBERLIST]**
	**These members are currently having their messages copied when they send a message in the copy channels in the copy servers.**
	**For more commands on the memberlist, use the command *!help*.**""")
									for member_id in memberlist:
										for copy_server_id in copy_server_ids:
											try:
												member_object = bot.get_server(copy_server_id).get_member(member_id)
												await bot.send_message(message.channel, """• {0} ({1})""".format(member_object.name, member_object.id))
											except Exception:
												pass
								else:
									await bot.send_message(message.channel, """**There are no members currently in the memberlist.**
	**For more commands on the memberlist, use the command *!help*.**""")



						else:
							await bot.send_message(message.channel, """**The server to copy from and the channel to copy from must be set up before the *!memberlist* command can be used.**""")



					####################################################################################################
					####################################################################################################



					elif (message.content[:10] == "!wordlist ") or (message.content == "!wordlist"):
						if (copy_server_ids != []) and (copy_channel_ids != []):

							#!WORDLIST ADD

							if (message.content[:14] == "!wordlist add ") or (message.content == "!wordlist add"):
								if (message.content.strip()[:14] == "!wordlist add "):
									if (message.content[14:] in wordlist) or ((not case_sensitive_wordlist) and (message.content[14:].lower() in wordlist)):
										if case_sensitive_wordlist:
											await bot.send_message(message.channel, """**The word *{0}* is already in the wordlist.**
	**Use the command *!wordlist* to see all the words that are currently being removed from the copied messages.**""".format(message.content[14:]))
										else:
											await bot.send_message(message.channel, """**The word *{0}* is already in the wordlist.**
	**Use the command *!wordlist* to see all the words that are currently being removed from the copied messages.**""".format(message.content[14:].lower()))
									else:
										if case_sensitive_wordlist:
											wordlist.append(message.content[14:])
											filedata["wordlist"] = wordlist		#SAVE TO FILE
											await bot.send_message(message.channel, """**The word *{0}* has been added to the wordlist.**""".format(message.content[14:]))
										else:
											wordlist.append(message.content[14:].lower())
											filedata["wordlist"] = wordlist		#SAVE TO FILE
											await bot.send_message(message.channel, """**The word *{0}* has been added to the wordlist.**""".format(message.content[14:].lower()))
								else:
									await bot.send_message(message.channel, """**Use the command *!wordlist add word* to add a member to the wordlist.**""")

							#!WORDLIST REMOVE

							elif (message.content[:17] == "!wordlist remove ") or (message.content == "!wordlist remove"):
								if len(wordlist) > 0:
									if (message.content[:21] == "!wordlist remove all ") or (message.content == "!wordlist remove all"):
										count = len(wordlist)
										wordlist = []
										filedata["wordlist"] = wordlist		#SAVE TO FILE
										if count == 1:
											await bot.send_message(message.channel, """**[1] word was removed from the wordlist.**""")
										else:
											await bot.send_message(message.channel, """**[{0}] words were removed from the wordlist.**""".format(str(count)))
										del count
									else:
										if (message.content[17:] in wordlist) or ((not case_sensitive_wordlist) and (message.content[17:].lower() in wordlist)):
											if case_sensitive_wordlist:
												wordlist.remove(message.content[17:])
												filedata["wordlist"] = wordlist		#SAVE TO FILE
												await bot.send_message(message.channel, """**The word *{0}* has been removed from the wordlist.**""".format(message.content[17:]))
											else:
												wordlist.remove(message.content[17:].lower())
												filedata["wordlist"] = wordlist		#SAVE TO FILE
												await bot.send_message(message.channel, """**The word *{0}* has been removed from the wordlist.**""".format(message.content[17:].lower()))
										else:
											if (message.content.strip()[:17] == "!wordlist remove "):
												await bot.send_message(message.channel, """**Invalid word - not in wordlist**""")
											await bot.send_message(message.channel, """**Here are all the words in the wordlist (the words that are currently being removed from the copied messages).**
	**Use the command *!wordlist remove word* to remove a word from the wordlist**""")
											for word in wordlist:
												await bot.send_message(message.channel, """• {0}""".format(word))
								else:
									await bot.send_message(message.channel, """**There are currently no words in the wordlist.**
	**For more commands on the wordlist, use the command *!help*.**""")

							#!WORDLIST TOGGLE CASE

							elif (message.content[:22] == "!wordlist toggle case ") or (message.content == "!wordlist toggle case"):
								if case_sensitive_wordlist:
									if len(wordlist) > 0:
										wordlist = list(word.lower() for word in wordlist)
										for word in wordlist:
											if wordlist.count(word) > 1:
												for x in range(wordlist.count(word) - 1):
													wordlist.remove(word)
									case_sensitive_wordlist = False
									filedata["wordlist"] = wordlist		#SAVE TO FILE
									filedata["case_sensitive_wordlist"] = case_sensitive_wordlist
									await bot.send_message(message.channel, """The wordlist is now case **insensitive**.""")
								else:
									case_sensitive_wordlist = True
									filedata["case_sensitive_wordlist"] = case_sensitive_wordlist		#SAVE TO FILE
									await bot.send_message(message.channel, """The wordlist is now case **sensitive**.""")

							#!WORDLIST

							elif (message.content[:10] == "!wordlist ") or (message.content == "!wordlist"):
								if len(wordlist) > 0:
									await bot.send_message(message.channel, """**[WORDLIST]**
	**These words are currently being removed from the copied messages.**
	**For more commands on the wordlist, use the command *!help*.**""")
									for word in wordlist:
										await bot.send_message(message.channel, """• {0} """.format(word))
								else:
									await bot.send_message(message.channel, """**There are no words currently in the wordlist.**
	**For more commands on the wordlist, use the command *!help*.**""")



						else:
							await bot.send_message(message.channel, """**The server to copy from and the channel to copy from must be set up before the *!wordlist* command can be used.**""")



					####################################################################################################
					####################################################################################################



					elif (message.content[:5] == "!add ") or (message.content == "!add"):
						if (message.content[:17] == "!add copy server ") or (message.content == "!add copy server"):
							temp_bool = False
							for server_object in bot.servers:
								if not (server_object.id in copy_server_ids):
									temp_bool = True
							if temp_bool:
								for server_object in bot.servers:
									if not (server_object.id in copy_server_ids):
										temp_bool
								await bot.send_message(message.channel, """**[ADDING COPY SERVER]**
	**Type one of these servers to add them to the copy server list.**""")
								for server_object in bot.servers:
									if not (server_object.id in copy_server_ids):
										await bot.send_message(message.channel, """• {0} ({1})""".format(server_object.name, server_object.id))
								adding_copy_server = True
							else:
								await bot.send_message(message.channel, """**All the servers I'm in are already in the copy server list.**""")


						elif (message.content[:18] == "!add copy channel ") or (message.content == "!add copy channel"):
							temp_bool = False
							for copy_server_id in copy_server_ids:
								server_object = bot.get_server(copy_server_id)
								for channel_object in server_object.channels:
									if (not (channel_object.id in copy_channel_ids)) and (str(channel_object.type) == "text"):
										temp_bool = True
							if temp_bool:
								await bot.send_message(message.channel, """**[ADDING COPY CHANNEL]**
	**Type one of these channels to add them to the copy channel list.**""")
								for server_object in bot.servers:
									if server_object.id in copy_server_ids:
										await bot.send_message(message.channel, """**{0} ({1})**""".format(server_object.name, server_object.id))
										for channel_object in server_object.channels:
											if (not (channel_object.id in copy_channel_ids)) and (str(channel_object.type) == "text"):
												await bot.send_message(message.channel, """• {0} ({1})""".format(channel_object.name, channel_object.id))
								adding_copy_channel = True
							else:
								await bot.send_message(message.channel, """**All the channels I'm in are already in the copy channel list.**""")


						elif (message.content[:17] == "!add post server ") or (message.content == "!add post server"):
							temp_bool = False
							for server_object in bot.servers:
								if not (server_object.id in post_server_ids):
									temp_bool = True
							if temp_bool:
								await bot.send_message(message.channel, """**[ADDING POST SERVER]**
	**Type one of these servers to add them to the post server list.**""")
								for server_object in bot.servers:
									if not (server_object.id in post_server_ids):
										await bot.send_message(message.channel, """• {0} ({1})""".format(server_object.name, server_object.id))
								adding_post_server = True
							else:
								await bot.send_message(message.channel, """**All the servers I'm in are already in the post server list.**""")


						elif (message.content[:18] == "!add post channel ") or (message.content == "!add post channel"):
							temp_bool = False
							for post_server_id in post_server_ids:
								server_object = bot.get_server(post_server_id)
								for channel_object in server_object.channels:
									if (not (channel_object.id in post_channel_ids)) and (str(channel_object.type) == "text"):
										temp_bool = True
							if temp_bool:
								await bot.send_message(message.channel, """**[ADDING POST CHANNEL]**
	**Type one of these channels to add them to the post channel list.**""")
								for server_object in bot.servers:
									if server_object.id in post_server_ids:
										await bot.send_message(message.channel, """**{0} ({1})**""".format(server_object.name, server_object.id))
										for channel_object in server_object.channels:
											if (not (channel_object.id in post_channel_ids)) and (str(channel_object.type) == "text"):
												await bot.send_message(message.channel, """• {0} ({1})""".format(channel_object.name, channel_object.id))
								adding_post_channel = True
							else:
								await bot.send_message(message.channel, """**All the channels I'm in are already in the post channel list.**""")


						else:
							await bot.send_message(message.channel, """**Use *!add* like this:**
	• *!add copy server* : Adds a server to copy from.
	• *!add copy channel* : Adds a channel (in the copy servers) to copy from.
	• *!add post server* : Adds a server to post to.
	• *!add post channel* : Adds a channel (in the post servers) to post to.
	""")



					####################################################################################################
					####################################################################################################



					elif (message.content[:8] == "!remove ") or (message.content == "!remove"):
						if (message.content[:20] == "!remove copy server ") or (message.content == "!remove copy server"):
							if len(copy_server_ids) > 0:
								await bot.send_message(message.channel, """**[REMOVING COPY SERVER]**
	**Type one of these servers to remove them from the copy server list.**""")
								for copy_server_id in copy_server_ids:
									server_object = bot.get_server(copy_server_id)
									await bot.send_message(message.channel, """• {0} ({1})""".format(server_object.name, server_object.id))
								removing_copy_server = True
							else:
								await bot.send_message(message.channel, """**There are currently no copy servers.**""")



						elif (message.content[:21] == "!remove copy channel ") or (message.content == "!remove copy channel"):
							if len(copy_channel_ids) > 0:
								await bot.send_message(message.channel, """**[REMOVING COPY CHANNEL]**
	**Type one of these channels to remove them from the copy channel list.**""")
								for copy_server_id in copy_server_ids:
									server_object = bot.get_server(copy_server_id)
									temp_bool = False
									for channel_object in server_object.channels:
										if channel_object.id in copy_channel_ids:
											temp_bool = True
									if temp_bool:
										await bot.send_message(message.channel, """**{0} ({1})**""".format(server_object.name, server_object.id))
									for channel_object in server_object.channels:
										if channel_object.id in copy_channel_ids:
											await bot.send_message(message.channel, """• {0} ({1})""".format(channel_object.name, channel_object.id))
								removing_copy_channel = True
							else:
								await bot.send_message(message.channel, """**There are currently no copy channels.**""")



						elif (message.content[:20] == "!remove post server ") or (message.content == "!remove post server"):
							if len(post_server_ids) > 0:
								await bot.send_message(message.channel, """**[REMOVING POST SERVER]**
	**Type one of these servers to remove them from the post server list.**""")
								for post_server_id in post_server_ids:
									server_object = bot.get_server(post_server_id)
									await bot.send_message(message.channel, """• {0} ({1})""".format(server_object.name, server_object.id))
								removing_post_server = True
							else:
								await bot.send_message(message.channel, """**There are currently no post servers.**""")



						elif (message.content[:21] == "!remove post channel ") or (message.content == "!remove post channel"):
								if len(post_channel_ids) > 0:
									await bot.send_message(message.channel, """**[REMOVING POST CHANNEL]**
	**Type one of these channels to remove them from the post channel list.**""")
									for post_server_id in post_server_ids:
										server_object = bot.get_server(post_server_id)
										temp_bool = False
										for channel_object in server_object.channels:
											if channel_object.id in post_channel_ids:
												temp_bool = True
										if temp_bool:
											await bot.send_message(message.channel, """**{0} ({1})**""".format(server_object.name, server_object.id))
										for channel_object in server_object.channels:
											if channel_object.id in post_channel_ids:
												await bot.send_message(message.channel, """• {0} ({1})""".format(channel_object.name, channel_object.id))
									removing_post_channel = True
								else:
									await bot.send_message(message.channel, """**There are currently no post channels.**""")



						else:
							await bot.send_message(message.channel, """**Use *!remove* like this:**
	• *!remove copy server* : Removes a copy server.
	• *!remove copy channel* : Removes a copy channel.
	• *!remove post server* : Removes a post server.
	• *!remove post channel* : Removes a post channel.
	""")


					####################################################################################################
					####################################################################################################

					elif (message.content[:6] == "!help ") or (message.content == "!help"):
						await bot.send_message(message.channel, """**[COMMANDS]**
	• *!memberlist* : Shows you all the members currently in the memberlist.
	• *!memberlist add member* : Adds a member from the copy server to the memberlist.
	• *!memberlist add all* : Adds all the members from the copy server to the memberlist.
	• *!memberlist remove member* : Removes a member from the memberlist.
	• *!memberlist remove all* : Removes all the members from the memberlist.
	• *!wordlist* : Shows all the words currently in the wordlist.
	• *!wordlist add word* : Adds a word to the wordlist.
	• *!wordlist remove word* : Removes a word from the wordlist .
	• *!wordlist remove all* : Removes all the words from the wordlist.
	• *!wordlist toggle case* : Toggles between case insensitive and case sensitive.
	• *!add* : Shows the commands for adding copy/post servers/channels.
	• *!remove* : Shows the commands for removing copy/post servers/channels.
	""")


					####################################################################################################
					####################################################################################################



				elif (message.content[:8].lower() == "!cancel ") or (message.content.strip().lower() == "!cancel"):
					adding_copy_server = False
					adding_copy_channel = False
					adding_post_server = False
					adding_post_channel = False

					removing_copy_server = False
					removing_copy_channel = False
					removing_post_server = False
					removing_post_channel = False

					await bot.send_message(message.channel, "Cancelled.")



				elif adding_copy_server:
					temp_bool = True
					for server_object in bot.servers:
						if (message.content == server_object.name) or (message.content == server_object.id):
							if server_object.id in copy_server_ids:
								await bot.send_message(message.channel, """**Invalid server - already a copy server.**""")
							else:
								copy_server_ids.append(server_object.id)
								filedata["setup_info"]["copy_server_ids"] = copy_server_ids		#SAVE TO FILE
								await bot.send_message(message.channel, """**The copy server *{0} ({1})* has been added.**""".format(server_object.name, server_object.id))
								adding_copy_server = False
							temp_bool = False
							break
					if adding_copy_server and temp_bool:
						await bot.send_message(message.channel, """**Invalid server - does not exist.**""")



				elif adding_copy_channel:
					temp_bool = True
					for server_id in copy_server_ids:
						for channel_object in bot.get_server(server_id).channels:
							if (message.content == channel_object.name) or (message.content == channel_object.id):
								if channel_object.id in copy_channel_ids:
									await bot.send_message(message.channel, """**Invalid channel - already a copy channel.**""")
								else:
									copy_channel_ids.append(channel_object.id)
									filedata["setup_info"]["copy_channel_ids"] = copy_channel_ids		#SAVE TO FILE
									await bot.send_message(message.channel, """**The copy channel *{0} ({1})* has been added.**""".format(channel_object.name, channel_object.id))
									adding_copy_channel = False
								temp_bool = False
								break
					if adding_copy_channel and temp_bool:
						await bot.send_message(message.channel, """**Invalid channel - does not exist.**""")



				elif adding_post_server:
					temp_bool = True
					for server_object in bot.servers:
						if (message.content == server_object.name) or (message.content == server_object.id):
							if server_object.id in post_server_ids:
								await bot.send_message(message.channel, """**Invalid server - already a post server.**""")
							else:
								post_server_ids.append(server_object.id)
								filedata["setup_info"]["post_server_ids"] = post_server_ids		#SAVE TO FILE
								await bot.send_message(message.channel, """**The post server *{0} ({1})* has been added.**""".format(server_object.name, server_object.id))
								adding_post_server = False
							temp_bool = False
							break
					if adding_post_server and temp_bool:
						await bot.send_message(message.channel, """**Invalid server - does not exist.**""")



				elif adding_post_channel:
					temp_bool = True
					for server_id in post_server_ids:
						for channel_object in bot.get_server(server_id).channels:
							if (message.content == channel_object.name) or (message.content == channel_object.id):
								if channel_object.id in post_channel_ids:
									await bot.send_message(message.channel, """**Invalid channel - already a post channel.**""")
								else:
									post_channel_ids.append(channel_object.id)
									filedata["setup_info"]["post_channel_ids"] = post_channel_ids		#SAVE TO FILE
									await bot.send_message(message.channel, """**The post channel *{0} ({1})* has been added.**""".format(channel_object.name, channel_object.id))
									adding_post_channel = False
								temp_bool = False
								break
					if adding_post_channel and temp_bool:
						await bot.send_message(message.channel, """**Invalid channel - does not exist.**""")






				elif removing_copy_server:
					for server_object in bot.servers:
						if (message.content == server_object.name) or (message.content == server_object.id):
							if server_object.id in copy_server_ids:
								copy_server_ids.remove(server_object.id)
								filedata["setup_info"]["copy_server_ids"] = copy_server_ids		#SAVE TO FILE
								await bot.send_message(message.channel, """**The copy server *{0} ({1})* has been removed.**""".format(server_object.name, server_object.id))
								removing_copy_server = False
					if removing_copy_server:
						await bot.send_message(message.channel, """**Invalid server - not a copy server.**""")



				elif removing_copy_channel:
					for server_object in bot.servers:
						for channel_object in server_object.channels:
							if (message.content == channel_object.name) or (message.content == channel_object.id):
								if channel_object.id in copy_channel_ids:
									copy_channel_ids.remove(channel_object.id)
									filedata["setup_info"]["copy_channel_ids"] = copy_channel_ids		#SAVE TO FILE
									await bot.send_message(message.channel, """**The copy channel *{0} ({1})* has been removed.**""".format(channel_object.name, channel_object.id))
									removing_copy_channel = False
					if removing_copy_channel:
						await bot.send_message(message.channel, """**Invalid channel - not a copy channel.**""")



				elif removing_post_server:
					for server_object in bot.servers:
						if (message.content == server_object.name) or (message.content == server_object.id):
							if server_object.id in post_server_ids:
								post_server_ids.remove(server_object.id)
								filedata["setup_info"]["post_server_ids"] = post_server_ids		#SAVE TO FILE
								await bot.send_message(message.channel, """**The post server *{0} ({1})* has been removed.**""".format(server_object.name, server_object.id))
								removing_post_server = False
					if removing_post_server:
						await bot.send_message(message.channel, """**Invalid server - not a post server.**""")



				elif removing_post_channel:
					for server_object in bot.servers:
						for channel_object in server_object.channels:
							if (message.content == channel_object.name) or (message.content == channel_object.id):
								if channel_object.id in post_channel_ids:
									post_channel_ids.remove(channel_object.id)
									filedata["setup_info"]["post_channel_ids"] = post_channel_ids		#SAVE TO FILE
									await bot.send_message(message.channel, """**The post channel *{0} ({1})* has been removed.**""".format(channel_object.name, channel_object.id))
									removing_post_channel = False
					if removing_post_channel:
						await bot.send_message(message.channel, """**Invalid channel - not a post channel.**""")

			# Checks if the message being sent is in the copy server and in the copy channel,
			# and if it is, then it posts that same message to the post server.

			if message.server.id in copy_server_ids:
				if message.channel.id in copy_channel_ids:
					if (message.author.id in memberlist) or (not(message.author in message.server.members)):
						if (message.content).strip() != "":
							for post_server_id in post_server_ids:
								for post_channel_id in post_channel_ids:
									server_object = bot.get_server(post_server_id)
									channel_object = server_object.get_channel(post_channel_id)
									if channel_object in server_object.channels:
										if len(edit_msg_list) > 0:
											for x in range(len(edit_msg_list)):
												if (x == 0) and (len(edit_msg_list) != edit_msg_list_length):
													edit_msg_list.append(edit_msg_list[len(edit_msg_list) - 1])
												else:
													edit_msg_list[len(edit_msg_list) - 1 - x] = edit_msg_list[len(edit_msg_list) - 2 - x]
											edit_msg_list[0] = {"copy_message_object" : message,
																"post_message_object" : None,
																"message_content" : message.content,
																"message_type" : "text"}
										else:
											edit_msg_list.append({"copy_message_object" : message,
																"post_message_object" : None,
																"message_content" : message.content,
																"message_type" : "text"})

										new_message = text_message_filter(message.content, bot)
										edit_msg_list[0]["post_message_object"] = await bot.send_message(channel_object, new_message)

						if message.attachments != []:
							for attachment in message.attachments:
								for post_server_id in post_server_ids:
									for post_channel_id in post_channel_ids:
										server_object = bot.get_server(post_server_id)
										channel_object = server_object.get_channel(post_channel_id)
										if channel_object in server_object.channels:
											await bot.send_message(channel_object, attachment["url"])
						if message.embeds != []:

							for original_embed_info in message.embeds:
								new_embed_info = {}
								
								if "title" in original_embed_info:
									new_embed_info["title"] = original_embed_info["title"]
								if "url" in original_embed_info:
									new_embed_info["url"] = original_embed_info["url"]
								if "description" in original_embed_info:
									new_embed_info["description"] = original_embed_info["description"]
								if "color" in original_embed_info:
									new_embed_info["color"] = original_embed_info["color"]
								if "timestamp" in original_embed_info:
									new_embed_info["timestamp"] = message.timestamp
								embed=discord.Embed(**new_embed_info)
									
								if "thumbnail" in original_embed_info:
									embed.set_thumbnail(url=original_embed_info["thumbnail"]["url"])

								if "fields" in original_embed_info:
									for embed_field in original_embed_info["fields"]:
										embed.add_field(name=embed_field["name"], value=embed_field["value"], inline=embed_field["inline"])
								
								if "footer" in original_embed_info:
									if footer_text.strip() != "":
										original_embed_info["footer"]["text"] = footer_text
									if footer_icon.strip() != "":
										original_embed_info["footer"]["icon_url"] = footer_icon
									embed.set_footer(**original_embed_info["footer"])
									
								if "author" in original_embed_info:
									if header_text.strip() != "":
										original_embed_info["author"]["name"] = header_text
									embed.set_author(**original_embed_info["author"])

								for post_server_id in post_server_ids:
									for post_channel_id in post_channel_ids:
										server_object = bot.get_server(post_server_id)
										channel_object = server_object.get_channel(post_channel_id)
										if channel_object in server_object.channels:
											try:
												await bot.send_message(channel_object, embed=embed)
											except Exception as e:
												print(e)
												print("EMBED: {0}".format(original_embed_info))





	globaldata[bot.unique_id]["filedata"] = filedata

	globaldata[bot.unique_id]["edit_msg_list"] = edit_msg_list
	globaldata[bot.unique_id]["edit_msg_list_length"] = edit_msg_list_length

	globaldata[bot.unique_id]["adding_copy_server"] = adding_copy_server
	globaldata[bot.unique_id]["adding_copy_channel"] = adding_copy_channel
	globaldata[bot.unique_id]["adding_post_server"] = adding_post_server
	globaldata[bot.unique_id]["adding_post_channel"] = adding_post_channel

	globaldata[bot.unique_id]["removing_copy_server"] = removing_copy_server
	globaldata[bot.unique_id]["removing_copy_channel"] = removing_copy_channel
	globaldata[bot.unique_id]["removing_post_server"] = removing_post_server
	globaldata[bot.unique_id]["removing_post_channel"] = removing_post_channel





@bot_1.event
async def on_ready():
	await on_ready_code(bot_1)

@bot_2.event
async def on_ready():
	await on_ready_code(bot_2)

@bot_3.event
async def on_ready():
	await on_ready_code(bot_3)

@bot_4.event
async def on_ready():
	await on_ready_code(bot_4)

@bot_5.event
async def on_ready():
	await on_ready_code(bot_5)

@bot_6.event
async def on_ready():
	await on_ready_code(bot_6)

@bot_7.event
async def on_ready():
	await on_ready_code(bot_7)

@bot_8.event
async def on_ready():
	await on_ready_code(bot_8)

@bot_9.event
async def on_ready():
	await on_ready_code(bot_9)

@bot_10.event
async def on_ready():
	await on_ready_code(bot_10)

@bot_11.event
async def on_ready():
	await on_ready_code(bot_11)

@bot_12.event
async def on_ready():
	await on_ready_code(bot_12)

@bot_13.event
async def on_ready():
	await on_ready_code(bot_13)

@bot_14.event
async def on_ready():
	await on_ready_code(bot_14)

@bot_15.event
async def on_ready():
	await on_ready_code(bot_15)

@bot_16.event
async def on_ready():
	await on_ready_code(bot_16)

@bot_17.event
async def on_ready():
	await on_ready_code(bot_17)

@bot_18.event
async def on_ready():
	await on_ready_code(bot_18)

@bot_19.event
async def on_ready():
	await on_ready_code(bot_19)

@bot_20.event
async def on_ready():
	await on_ready_code(bot_20)





@bot_1.event
async def on_message(message):
	await on_message_code(bot_1, message)

@bot_2.event
async def on_message(message):
	await on_message_code(bot_2, message)

@bot_3.event
async def on_message(message):
	await on_message_code(bot_3, message)

@bot_4.event
async def on_message(message):
	await on_message_code(bot_4, message)

@bot_5.event
async def on_message(message):
	await on_message_code(bot_5, message)

@bot_6.event
async def on_message(message):
	await on_message_code(bot_6, message)

@bot_7.event
async def on_message(message):
	await on_message_code(bot_7, message)

@bot_8.event
async def on_message(message):
	await on_message_code(bot_8, message)

@bot_9.event
async def on_message(message):
	await on_message_code(bot_9, message)

@bot_10.event
async def on_message(message):
	await on_message_code(bot_10, message)

@bot_11.event
async def on_message(message):
	await on_message_code(bot_11, message)

@bot_12.event
async def on_message(message):
	await on_message_code(bot_12, message)

@bot_13.event
async def on_message(message):
	await on_message_code(bot_13, message)

@bot_14.event
async def on_message(message):
	await on_message_code(bot_14, message)

@bot_15.event
async def on_message(message):
	await on_message_code(bot_15, message)

@bot_16.event
async def on_message(message):
	await on_message_code(bot_16, message)

@bot_17.event
async def on_message(message):
	await on_message_code(bot_17, message)

@bot_18.event
async def on_message(message):
	await on_message_code(bot_18, message)

@bot_19.event
async def on_message(message):
	await on_message_code(bot_19, message)

@bot_20.event
async def on_message(message):
	await on_message_code(bot_20, message)





args = []
if active_1:
	args.append(bot_1.start(token_1, bot=not(selfbot_1)))
	bot_1.loop.create_task(edit_check(bot_1))
if active_2:
	args.append(bot_2.start(token_2, bot=not(selfbot_2)))
	bot_2.loop.create_task(edit_check(bot_2))
if active_3:
	args.append(bot_3.start(token_3, bot=not(selfbot_3)))
	bot_3.loop.create_task(edit_check(bot_3))
if active_4:
	args.append(bot_4.start(token_4, bot=not(selfbot_4)))
	bot_4.loop.create_task(edit_check(bot_4))
if active_5:
	args.append(bot_5.start(token_5, bot=not(selfbot_5)))
	bot_5.loop.create_task(edit_check(bot_5))
if active_6:
	args.append(bot_6.start(token_6, bot=not(selfbot_6)))
	bot_6.loop.create_task(edit_check(bot_6))
if active_7:
	args.append(bot_7.start(token_7, bot=not(selfbot_7)))
	bot_7.loop.create_task(edit_check(bot_7))
if active_8:
	args.append(bot_8.start(token_8, bot=not(selfbot_8)))
	bot_8.loop.create_task(edit_check(bot_8))
if active_9:
	args.append(bot_9.start(token_9, bot=not(selfbot_9)))
	bot_9.loop.create_task(edit_check(bot_9))
if active_10:
	args.append(bot_10.start(token_10, bot=not(selfbot_10)))
	bot_10.loop.create_task(edit_check(bot_10))
if active_11:
	args.append(bot_11.start(token_11, bot=not(selfbot_11)))
	bot_11.loop.create_task(edit_check(bot_11))
if active_12:
	args.append(bot_12.start(token_12, bot=not(selfbot_12)))
	bot_12.loop.create_task(edit_check(bot_12))
if active_13:
	args.append(bot_13.start(token_13, bot=not(selfbot_13)))
	bot_13.loop.create_task(edit_check(bot_13))
if active_14:
	args.append(bot_14.start(token_14, bot=not(selfbot_14)))
	bot_14.loop.create_task(edit_check(bot_14))
if active_15:
	args.append(bot_15.start(token_15, bot=not(selfbot_15)))
	bot_15.loop.create_task(edit_check(bot_15))
if active_16:
	args.append(bot_16.start(token_16, bot=not(selfbot_16)))
	bot_16.loop.create_task(edit_check(bot_16))
if active_17:
	args.append(bot_17.start(token_17, bot=not(selfbot_17)))
	bot_17.loop.create_task(edit_check(bot_17))
if active_18:
	args.append(bot_18.start(token_18, bot=not(selfbot_18)))
	bot_18.loop.create_task(edit_check(bot_18))
if active_19:
	args.append(bot_19.start(token_19, bot=not(selfbot_19)))
	bot_19.loop.create_task(edit_check(bot_19))
if active_20:
	args.append(bot_20.start(token_20, bot=not(selfbot_20)))
	bot_20.loop.create_task(edit_check(bot_20))

client.loop.run_until_complete(asyncio.gather(*args))
