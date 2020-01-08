car_started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit game
        """)
    elif command == "start":
        if not car_started:
            car_started = True
            print("Car started. Ready to go!")
        else:
            print("Car was already started")
    elif command == "stop":
        if car_started:
            car_started = False
            print("Car stopped.")
        else:
            print("Car was already stopped")
    elif command == "quit":
        break
    else:
        print("I don't understand that")
