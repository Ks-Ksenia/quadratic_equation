import logging

logging.basicConfig(filename='log.log', filemode="w", format="%(asctime)s %(levelname)s %(message)s")

log = logging.getLogger()
