data = open("quarter_year_data.txt", mode="r")

d_curry = dict({'steph curry':'Curry',\
	'steven curry':'Curry',\
	'steph':'Curry',\
	'steven':'Curry',\
	'curry':'Curry'})

# print d_curry.keys()
d_lebron = dict({"lebron james":"Lebron",\
	"lebron":"Lebron",\
	"lbj":"Lebron"})

d_klay = dict({"klay":"Klay",\
	"klay thompson":"Klay",\
	"thompson":"Klay"})
d_irving = dict({"irving":"KI",\
	"kyrie":"KI",\
	"kyrie irving":"KI"})
d_mcgee = dict({"mcgee":"Mcgee",\
	"javale mcgee":"Mcgee",\
	"javale":"Mcgee"})
d_love = dict({"love":"Love",\
	"kevin love":"Love",\
	"kevin":"Love"})

d_green = dict({"green":"Green",\
	"draymond":"Green",\
	"draymond green":"Green"})

d_kd = dict({"kd":"Durant",\
	"kevin durant":"Durant",\
	"durant":"Durant"})

d_iguodala = dict({"iguodala":"Iguodala",\
	"andre":"Iguodala",\
	"andre iguodala":"Iguodala"})

d_jr = dict({"jr.smith":"Smith",\
	"smith":"Smith"})

count = 0
detect_flag = False
save_flag = False
no_name_flag =False
another_name_exist = False


for line in data:
	detect_flag = False
	count = count + 1
	line = line.replace('\\n',' ')
	if line.find("---------------------------------") != -1:
		save_flag = False
		detect_flag = True
		continue

	if (line.find("---------------------------------") != -1 and no_name_flag == True):
		no_name_flag = False
		detect_flag = True
		continue

	line_cut = line[line.find('(')+2 : line.find(')')-1]

	# print line_cut
	line_type = line_cut[: line_cut.find(',')-1]
	line_content = line_cut[line_cut.find('u')+2:]
	# print line_type,line_content
	another_name_exist = False
	for detect_name in d_irving.keys():
		if(line_type.find("Title") != -1 and detect_flag == False):
			if(line_content.lower().find(detect_name) != -1):
				detect_flag = True
				save_flag = True
			else:
				no_name_flag =True
		elif(line_type.find("Comment") != -1 and save_flag == True and detect_flag == False):

			for detect_name2 in d_mcgee.keys():
				if(line_content.lower().find(detect_name2) != -1 and another_name_exist == False):
					another_name_exist = True
					#print count," ",1
			for detect_name3 in d_lebron.keys():
				if(line_content.lower().find(detect_name3) != -1 and another_name_exist == False):
					another_name_exist = True
					#print count," ",2
			for detect_name4 in d_iguodala.keys():
				if(line_content.lower().find(detect_name4) != -1 and another_name_exist == False):
					another_name_exist = True
					#print count," ",3
			for detect_name5 in d_curry.keys():
				if(line_content.lower().find(detect_name5) != -1 and another_name_exist == False):
					another_name_exist = True
					#print count," ",4
			for detect_name6 in d_kd.keys():
				if(line_content.lower().find(detect_name6) != -1 and another_name_exist == False):
					another_name_exist = True
					#print count," ",5
			for detect_name7 in d_love.keys():
				if(line_content.lower().find(detect_name7) != -1 and another_name_exist == False):
					another_name_exist = True
					#print count," ",6
			for detect_name8 in d_klay.keys():
				if(line_content.lower().find(detect_name8) != -1 and another_name_exist == False):
					another_name_exist = True
					#print count," ",7
			for detect_name9 in d_green.keys():
				if(line_content.lower().find(detect_name9) != -1 and another_name_exist == False):
					another_name_exist = True
					#print count," ",8
			for detect_name10 in d_jr.keys():
				if(line_content.lower().find(detect_name10) != -1 and another_name_exist == False):
					another_name_exist = True
					#print count," ",9

			if(another_name_exist == False):
				#print count
				write_txt = open("irving_2.txt", mode='a')
				write_txt.write(line_content)
				write_txt.write("\n")
				detect_flag = True
			else:
				detect_flag = True

		elif(no_name_flag == True and detect_flag == False):
			if(line_type.find("Comment") != -1):
				if(line_content.lower().find(detect_name) != -1):
					for detect_name2 in d_mcgee.keys():
						if(line_content.lower().find(detect_name2) != -1 and another_name_exist == False):
							another_name_exist = True
							#print count," ",1
					for detect_name3 in d_lebron.keys():
						if(line_content.lower().find(detect_name3) != -1 and another_name_exist == False):
							another_name_exist = True
							#print count," ",2
					for detect_name4 in d_iguodala.keys():
						if(line_content.lower().find(detect_name4) != -1 and another_name_exist == False):
							another_name_exist = True
							#print count," ",3
					for detect_name5 in d_curry.keys():
						if(line_content.lower().find(detect_name5) != -1 and another_name_exist == False):
							another_name_exist = True
							#print count," ",4
					for detect_name6 in d_kd.keys():
						if(line_content.lower().find(detect_name6) != -1 and another_name_exist == False):
							another_name_exist = True
							#print count," ",5
					for detect_name7 in d_love.keys():
						if(line_content.lower().find(detect_name7) != -1 and another_name_exist == False):
							another_name_exist = True
							#print count," ",6
					for detect_name8 in d_klay.keys():
						if(line_content.lower().find(detect_name8) != -1 and another_name_exist == False):
							another_name_exist = True
							#print count," ",7
					for detect_name9 in d_green.keys():
						if(line_content.lower().find(detect_name9) != -1 and another_name_exist == False):
							another_name_exist = True
							#print count," ",8
					for detect_name10 in d_jr.keys():
						if(line_content.lower().find(detect_name10) != -1 and another_name_exist == False):
							another_name_exist = True
							#print count," ",9
					# print line_content
					if(another_name_exist == False):
						#print count
						write_txt = open("irving_example.txt", mode='a')
						write_txt.write(line_content)
						write_txt.write("\n")
						detect_flag = True
					else:
						detect_flag = True

# print count
write_txt.close()
data.close()
