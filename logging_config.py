import logging
import datetime
import sys 

logging.basicConfig(
    level=logging.INFO,
    filename=f'log/compendium_matura-{datetime.date.today()}.log',
    filemode='a',
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))