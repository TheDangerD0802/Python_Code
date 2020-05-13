import os
import subprocess


os.system("tput setaf 1")
print("\t\t\twelcome to my tool")
os.system("tput setaf 0")
print("\t\t\t------------------")

print("Where u want to execute (local/remote) : " , end=' ')
ch_platform  = input()
print(ch_platform)

if ch_platform == "local":

	print("""
	Press 1: to check date
	Press 2: to check cal
	Press 3: to check ls
	Press 4: to create user
	Press 5: to create file
	Press 6: exit
	""")


	print("enter ur choice :" , end=' ')
	ch = input()
	print(ch)


	if int(ch) == 1:
		output = subprocess.getoutput("date")
		print(output)

	elif int(ch) == 2:
		print("cal")

	elif int(ch) == 3:
		print("ls")

	elif int(ch) == 4:
		print("enter user name : ", end=' ')
		user_create_in = input()
		print(user_create_in)
		user_create = "useradd  {0}".format(user_create_in)
		x = subprocess.getstatusoutput(user_create)
		if x[0] == 0:
			print("user named {} created successfully".format(user_create_in))
		else:
			print("command for user is NOT success : {}".format(x[1]))

	elif int(ch) == 5:
		print("file")

	elif int(ch) == 6:
		print("exit")
	else:
		print("not found")



elif  ch_platform == "remote":
	print("IP of remote : " , end=' ' )
	remote_ip = input()
	print(remote_ip)

	print("""
	Press 1: to check date
	Press 2: to check cal
	Press 3: to check ls
	Press 4: to create user
	Press 5: to create file
	Press 6: exit
	""")


	print("enter ur choice :" , end=' ')
	ch = input()
	print(ch)

	if int(ch)  ==  1:
		x = subprocess.getoutput("ssh {} date".format(remote_ip))
		print(x)
	else:
		print("not support")


else:
	print("option doesnot support !!")




