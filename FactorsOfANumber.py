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

def print_factors(x):
    print("The Factors Of",x,"are:")
    for i in range (1, x + 1):
        if x % i ==0:
            print(i)

num=int(input("Enter a Number to Find The Factors: \n"))
print_factors(num)                