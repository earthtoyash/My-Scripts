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

print("Enter the number of Rows: \n", end="")
row = int(input())
num = 1
max_digits = len(str(row * (row+1)//2))
for i in range(row):
    for j in range(i+1):
        print(str(num).ljust(max_digits), end=" ")
        num = num+1
    print()
