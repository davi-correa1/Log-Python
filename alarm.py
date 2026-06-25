import re 

padroes_suspeitos = {
    "Brute Force": r"Erro de login|Falha na autenticação|Senha incorreta",

    "SQL Ijection Attack (SQLi)": r"SELECT \* FROM|UNION SELECT|OR '1'='1|DROP TABLE",

    "Path Attack": r"\.\./\.\./|\.\.\\\.\.\\|/etc/passwd",
}

def analyzing_logs(way):
    print("Analyzing...\n")

    try:
        with open(way, "r", encoding="utf-8") as arquivo:
            for num_line, line in enumerate(arquivo, 1):
                for threat_type, regex in padroes_suspeitos.items():
                    if re.search(regex, line, re.IGNORECASE):
                        alarm()
    except FileNotFoundError:
        print(f"Error: The archive ´{way}´ do not can be found.")

def alarm():
    print("ALERT")

analyzing_logs("log.txt")