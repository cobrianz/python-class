command = input(">").upper()
if command == "HELP":
    print('Start - To start the car')
    print('stop - To stop the car')
    print('Quit - To Exit')
    command = input(">")
elif command == "START":
    print('Car Started...')
    command = input(">")
elif command == "STOP":
    print('Car stopped...')
    command = input(">")
elif command == "QUIT":
    print('Exiting...')
    exit(0)
else:
    print('Invalid command')
    command = input(">")