import os
import sys
import logging

# logging string format
# asctime -> date time
# level name -> level of log message
# module -> from which file this log is generated
# message -> log message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# creating log dir to log save log file
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_log.log")
os.makedirs(log_dir, exist_ok=True)

# define log instance
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# creating custom logger
logger = logging.getLogger("MlProjectLogger")
