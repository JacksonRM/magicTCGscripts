import os
import sys
import time

date = time.strftime("%x")
current_time = time.strftime("%X")
current_time = current_time.replace(':','.')
out_file_name = "C:\\temp\\price_data_combined." + date.replace('/','.') +"."+current_time+".txt"


out_file = open(out_file_name, 'w')
os.chdir("C:\\temp\\meta_logs")
file_count = 0
all_cards = {}

for file in os.listdir("C:\\temp\\meta_logs"):
	print(file)
	infile = open(file,'r')
	lines = infile.readlines()
	for l in lines :
		card_name = l.split('/')[0]
		percent = l.split('/')[1]
		if(card_name in all_cards):
			all_cards[card_name].append(percent)
		else:
			all_cards[card_name] = []
			for i in range (file_count) :
				all_cards[card_name].append(str(0.0))
			all_cards[card_name].append(percent)
	file_count += 1
	infile.close()
#add zeros if they are missing in the last N files
for a_key, a_list in all_cards.items() :
	if(len(a_list) != file_count) :
		for i in range(file_count - len(a_list)) :
			a_list.append(str(0.0))

s=sorted(all_cards.items(), key=lambda card: float(card[1][0]),reverse=True)
for x in s:
	out_file.write(x[0] + " / ")
	for y in x[1] :
		out_file.write(y + " / ")
	out_file.write("\n")
#\print(all_cards.items())
out_file.close()
sys.exit()
for a_key in all_cards :
	out_file.write(a_key + " / ")
	for p in all_cards[a_key] :
		out_file.write(str(p) + " / ")		
	out_file.write("\n")

out_file.close()


		
# infile1 = open("C:\\temp\\meta_log.03.27.16.txt",'r')
# infile2= open("C:\\temp\\meta_log.03.31.16.14.15.19.txt",'r')

# lines1 = infile1.readlines()
# lines2 = infile2.readlines()

# all_cards = {}
# file_count = 1;
# for l in lines1 :
	# card_name = l.split('/')[0]
	# percent = l.split('/')[1]
	# if(card_name in all_cards):
		# all_cards[card_name].append(percent)
	# else:
		# all_cards[card_name] = []
		# all_cards[card_name].append(percent)
		# #print("there")

# for l in lines2 :
	# card_name = l.split('/')[0]
	# percent = l.split('/')[1]
	# if(card_name in all_cards):
		# all_cards[card_name].append(percent)
		# #print("HERE")
	# else:
		# all_cards[card_name] = []
		# for i in range (file_count) :
			# all_cards[card_name].append(0.0)
		# all_cards[card_name].append(percent)
		# #print("there")
# file_count = 2
# for a_key, a_list in all_cards.items() :
	# if(len(a_list) != file_count) :
		# a_list.append(0.0)
		
# for a_key in all_cards :
	# out_file.write(a_key + " / ")
	# #print("\n"+a_key, end=" ")
	# for p in all_cards[a_key] :
		# out_file.write(str(p) + " / ")
		# #print(p, end=" ")
	# out_file.write("\n")

# out_file.close()
# infile1.close()
# infile2.close()