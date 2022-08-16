def fc():
    while True:
        feeling = input("How are you? ")
        if feeling.isalpha():    
            if feeling.lower() == 'great':
                print("That's good for you.")
            else:
                print("So what?")
        else:
            print("What the fuck are you talking about?")
            break
fc()
