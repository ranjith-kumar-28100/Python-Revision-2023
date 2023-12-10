import logging

logging.basicConfig(filename='mylog.log', filemode='a', level=logging.DEBUG)
logging.critical("Critical")
logging.error("Error")
logging.warning("Warning")
logging.info("Info")
logging.debug("Debug")
