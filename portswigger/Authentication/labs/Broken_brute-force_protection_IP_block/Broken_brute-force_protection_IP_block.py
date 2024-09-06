usr_username = "wiener"
usr_password = "peter"
vic_username = "carlos"

password_list = open("passwords", 'r')

new_username_list = []
new_password_list = []

for password in password_list:
    new_username_list.append(usr_username)
    new_username_list.append(vic_username)

    new_password_list.append(usr_password)
    new_password_list.append(password.rstrip())

password_list.close()

f = open("username_list", 'w')
for username in new_username_list:
    f.write(username)
    f.write("\n")
f.close()

f = open("password_list", 'w')
for password in new_password_list:
    f.write(password)
    f.write("\n")
f.close()
