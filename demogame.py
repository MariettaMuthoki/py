command =""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
             print("Car has already started")
        else:
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car has already been stopped")
        else:
            started = False
            print("Car stopped")
    elif command == ("help"):
        print("""
    start - to get the car started   
    stop - to stop the car
    quit - to exit the game """
        )
    elif command =="quit":
        break
    else:
        print("I do not know what that is!")