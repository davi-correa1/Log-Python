import logging, os, time

logging.basicConfig(
    format="%(levelname)s| %(asctime)s - %(message)s",
    level=logging.DEBUG,
    filename='app.log',
    filemode='w'
)


# sign up
def interface():

    # Clean the terminal
    os.system('cls')

    # Choose the password
    password = input("Choose a password: ")
    print("=" * 25, "\n")
    password2 = input("Confirm the password, please: ")

    # Sends a message if the password is correct
    if password == password2:
        logging.info("Client's active!")
        print("You're active!")
        time.sleep(1.5)
        os.system('cls')

    # Sends a message if the password is incorrect
    else:
        logging.error("Logging error!")
        print("password incorrect, try again...")
        time.sleep(1)

        # Call the function again
        return interface()

interface()