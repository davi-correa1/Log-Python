import logging, io

strm = io.StringIO()

logging.basicConfig(
    stream=strm,
    format="%(levelname)s | %(asctime)s - %(message)s",
    level=logging.INFO
)

# create a message to log.info
logging.info("Client on!")

# recive the value from log
value_log = strm.getvalue()

with open("log.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(value_log)
