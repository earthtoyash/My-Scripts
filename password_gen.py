# Banner
# This Project is a Copyright to Morse.industries
print(r"""          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    
          $$    _____      _____     __________     _________      _______     __________      $$             
          $$   |      \  /      |   /   ____   \   |   ____   \   /  ____  \  |   ______/      $$                          
          $$   |   |\  \/  /|   |  /   /    \   \  |  |    \   | |  |    |__| |  |             $$                   
          $$   |   | \    / |   | |   |      |   | |  |____/ _/  |  |_____    |  |______       $$                        
          $$   |   |  \__/  |   | |   |      |   | |    _   \     \______  \  |   ______|      $$                    
          $$   |   |        |   | |   |      |   | |   | \   \    __     |  | |  |             $$          
          $$   |   |        |   |  \   \____/   /  |   |  \   \  |  |____|  | |  |_______      $$                     
          $$   |___|        |___|   \__________/   |___|   \___\  \________/  |__________\     $$        
          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ """)


# For Generating Random Passwords!
# Code by Yashwant Singh

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	length = int(input("Enter password length: "))
	random.shuffle(characters)
	password = []

	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)

	print("".join(password))

generate_random_password()