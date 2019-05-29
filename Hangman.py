import random

words = []

with open('dict.txt', 'r') as f:
    line = f.readline().strip()
    words.append(line)
    
    while line:
        line = f.readline().strip()
        words.append(line)
        
rand_num = random.randint(0, len(words))
#print(words[rand_num])

text = words[rand_num]
#text = list(text)
words = [i for i in text]

my_list = []

for i in range(len(words)):
    my_list.append('_')
    
new_list = []    

def guess(letter):
    if letter.upper() in new_list:
        print("Already guessesd")
        
    elif letter.upper() in words:
        for j in range(len(words)):
            if words[j] == letter.upper():
                my_list[j] = letter.upper()
        print(my_list)
       
    else:
        print("\nIncorrect!\n")
        flag = True
        count(flag)    

        
        
    new_list.append(letter.upper())
        
    for k in range(len(my_list)):
        if '_' in my_list:
            return 1
        
        else:
            return 0
        
  
def count(flag):
    global x
    
    if (flag == True):
        x-=1
        print("You have" + str(x) + "guesses left")
        
        if x == 0:
            print("GAME OVER")
            exit(0)
        
               
if __name__ == "__main__":
     
    x = 6

    letter = input("Guess your letter:")
    #count = 6
#    count -=1
 #   print (str(count) + "guesses left")

    while guess(letter):
        
        letter = input("Guess your letter:")
        #count -=1
   #     print (str(count) + "guesses left")
    #    if count == 1 :
     #       print("Game Over")
    print("Total guessess: " + str(x))
        
        
            
            
        
