import logging, io, os

strm = io.StringIO()

logging.basicConfig(
    stream=strm,
    format="%(levelname)s| %(asctime)s - %(message)s",
    level=logging.DEBUG
)


# sign up
def interface():

    # Clean the terminal
    os.system('cls')

    # Choose the password
    password = input("Choose a password: ")
    print("_" * 25, "\n")
    password2 = input("Confirm the password, please: ")

    # Sends a message if the password is correct
    if password == password2:
        logging.info("Client's active!")
        print("You're active!")

    # Sends a message if the password is incorrect
    else:
        logging.error("Logging error1")
        print("password incorrect, try again...")

        # Call the function again
        return interface()

# recive the value from log
value_log = strm.getvalue()
def sendMessage(value_log):
    with open("app.log", "a", encoding="utf-8") as arquivo:
        arquivo.write(value_log)



interface()
