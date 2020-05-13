import subprocess

def user_create():
	print("enter user name : ", end=' ')
	user_create_in = input()
	print(user_create_in)
	user_create = "useradd  {0}".format(user_create_in)
	x = subprocess.getstatusoutput(user_create)
	if x[0] == 0:
		print("user named {} created successfully".format(user_create_in))
	else:
		print("command for user is NOT success : {}".format(x[1]))
