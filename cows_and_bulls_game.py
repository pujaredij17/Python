import random

def cows_and_bulls(user_input, num):
    
    for i in range(len(user_input)):
        
        if user_input[i] == num[i]:
            
            global cows
            cows +=1
                        
        if ((user_input[i] in num) and (user_input[i] != num[i])):
                
                global bulls
                bulls +=1      
                
if __name__ == '__main__' :
    cows = 0
    bulls = 0
    count = 0
    
    #user_input = input("Enter a num")
    num = str(random.randint(1000, 10000))
    
    while True:
        
        cows = 0
        bulls = 0
        
        user_input = input("\nEnter a num")
        print(num)
        
        cows_and_bulls(user_input, num)
        count += 1
        
        print("No of cows : " + str(cows) + "\nNo of Bulls : " + str(bulls))
        print("\nTotal no of guesses :" +str(count))
        
        
        if cows == 4 :
            print("Winner")
            exit(0)
    
    