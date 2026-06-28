import re, os

# Set some 
padroes_suspeitos = {
    "Brute Force": r"Logging error|Falha na autenticação|Incorrect password",

    "SQL Ijection Attack (SQLi)": r"SELECT \* FROM|UNION SELECT|OR '1'='1|DROP TABLE",

    "Path Attack": r"\.\./\.\./|\.\.\\\.\.\\|/etc/passwd",
}

def analyzing_logs(way):
    # Clean the terminal
    os.system('cls')
    print("Analyzing...\n")

    try:
        # Open the file in read mode("r")
        with open(way, "r", encoding="utf-8") as file:

            # Considers the file contaminated until verified
            anyThreatFound = False

            # Take it one line at a time
            for num_line, line in enumerate(file, 1):

                # Checks if the line contains a threat
                for threat_type, regex in padroes_suspeitos.items():

                    # Triggers the alarm if there is a threat
                    if re.search(regex, line, re.IGNORECASE):
                        alarm(num_line, threat_type)
                        # It only changes the file attribute to the code.
                        anyThreatFound = True 

            # Sends a message if there is no threat
            if not anyThreatFound:
                print("No threats were found!")

    # Sends a message if the file cannot be found
    except FileNotFoundError:
        print(f"ERROR| The flie ´{way}´ does not exist.")
        
def alarm(num_line, threat_type):
    print(f"🚨 ALERT | A possible ´{threat_type}´ found in line ´{num_line}´!", "\n"*5)

# Call the function and pass the "way"
analyzing_logs("app.log")