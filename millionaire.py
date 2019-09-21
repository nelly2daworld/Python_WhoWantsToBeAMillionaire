# Who wants to be a Millionaire??

# The progression in this "short" version of millionaire should be:
# 1 answer correct: $500
# 2 answers correct: $1000
# 3 answers correct: $5000
# 4 answers correct: $20000
# 5 answers correct: $50000
# 6 answers correct: $250000
# 7 answers correct: $500000
# 8 answers correct: $1000000
# Your code here!
money_made = 0
question_num = 1
not_finished = True
name = input("Welcome to Millionaire! What is your name? ")

answers_file = "answers.txt"
with open(answers_file) as af:
    answer = af.readline()
    line_num = 1
    while answer:
        print("\nCurrently you have made $"+ str(money_made))
        print("\nWhat crime is 'larceny'?")
        print("a. Starting fires")
        print("b. Kidnapping")
        print("c. Murder")
        print("d. Theft") #Correct
        user_response_one = input(">> ") 
        #Important to not consider the new line
        if(user_response_one == answer[0]):
            print("Correct!")
            money_made = 500
            line_num += 1
        else:
            print("I'm sorry, that is incorrect")
            break
        
        
        print("\nCurrently you have made $"+ str(money_made))
        print("\nIf someone asked to see your 'i.d.', what might you show them?")
        print("a. Your tongue")
        print("b. Your teeth")
        print("c. Your passport") #c - Correct
        print("d. The door")
        user_response_two = input(">> ")
        answer = af.readline()
        if(user_response_two == answer[0]):
            print("Correct!")
            money_made = 1000
            line_num += 1
        else:
            print("I'm sorry, that is incorrect")
            break
        
        
        print("\nCurrently you have made $"+ str(money_made))
        print("\nWhich of these worde describes a particular group of vegetables??")
        print("a. Purse")
        print("b. Pulse")#b- Correct
        print("c. Beat")
        print("d. Throb")
        user_response_three = input(">> ")
        answer = af.readline()
        if(user_response_three == answer[0]):
            print("Correct!")
            money_made = 5000
            line_num += 1
        else:
            print("I'm sorry, that is incorrect")
            break
        
        
        print("\nCurrently you have made $"+ str(money_made))
        print("\nWhat does the word 'dulce' indicate on a Spanish wine label?")
        print("a. Dry")
        print("b. Sweet")#b - Correct
        print("c. White")
        print("d. Sparkling")
        user_response_four = input(">> ")
        answer = af.readline()
        if(user_response_four == answer[0]):
            print("Correct!")
            money_made = 20000
            line_num += 1
        else:
            print("I'm sorry, that is incorrect")
            break
        
        
        
        print("\nCurrently you have made $"+ str(money_made))
        print("\nWhat words represents the letter 'Q' in the phonetic alphabet?")
        print("a. Queen")
        print("b. Quebec")#b
        print("c. Quarter")
        print("d. Quiz")
        user_response_five = input(">> ")
        answer = af.readline()
        if(user_response_five == answer[0]):
            print("Correct!")
            money_made = 50000
            line_num += 1
        else:
            print("I'm sorry, that is incorrect")
            break
        

        print("\nCurrently you have made $"+ str(money_made))
        print("\nWhich abbreviation means 'and so on'?")
        print("a. e.g")
        print("b. etc.")#b
        print("c. viz")
        print("d. i.e.")
        user_response_six = input(">> ")
        answer = af.readline()
        if(user_response_six == answer[0]):
            print("Correct!")
            money_made = 250000
            line_num += 1
        else:
            print("I'm sorry, that is incorrect")
            break
        
        
        print("\nCurrently you have made $"+ str(money_made))
        print("\nWhat name is given to the calm area at the centre of a hurricane?")
        print("a. Ear")
        print("b. Mouth")
        print("c. Nose")
        print("d. Eye") #d
        user_response_seven = input(">> ")
        answer = af.readline()
        if(user_response_seven == answer[0]):
            print("Correct!")
            money_made = 500000
            line_num += 1
        else:
            print("I'm sorry, that is incorrect")
            break
        
        
        print("\nCurrently you have made $"+ str(money_made))
        print("\nWhat is a 'funambulist'?")
        print("a. A tightrope walker")#a
        print("b. A sleepwalker")
        print("c. A firewalker")
        print("d. A fell walker")
        user_response_eight = input(">> ")
        answer = af.readline()
        if(user_response_eight == answer[0]):
            print("Correct!")
            money_made = 1000000
            line_num += 1
            print("You are a millionaire!")
            break
        else:
            print("I'm sorry, that is incorrect")
            break
        
af.close()
