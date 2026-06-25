import re 

padroes_suspeitos = {
    "Brute Force": r"Erro de login|Falha na autenticação|Senha incorreta",

    "Attack jection (SQLi)": r"SELECT \* FROM|UNION SELECT|OR '1'='1|DROP TABLE",

    "Ataque Path Traversal": r"\.\./\.\./|\.\.\\\.\.\\|/etc/passwd",
}

def analyzing_logs(log.txt):
    print("Analyzing...\n")

    try:
        with open(log.txt, "r", enconding="utf-8") as arquivo:
            for num_line, line in enumerate(arquivo, 1):
                for 