guess = 0
while True:
    print("What were my first words")
    print("Type your answer or type 'I don't know' below.")
    answer = input()
    guess += 1 
    
    if answer == "Hello World":
        print ("Hello World! How Are You?")
        break

    elif answer == "I don't know":
        print("How sad....Better luck next time!")
        break

    else:
        pass
