import logging
import logging.config
import yaml

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
# Basically, this function can only be called once.

logging.warning('This will get logged to a file')
logging.debug('This is a debug message')
logging.info('Admin logged in')
# logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

name = 'John'

logging.error(f'{name} raised an error')

a = 5
b = 0

try:
  c = a / b
except Exception as e:
    logging.exception("Exception occurred")
    logging.error("Exception occurred", exc_info=True)
# If exc_info is not set to True, the output of the above program 
# would not tell us anything about the exception
# Using logging.exception() would show a log at the level of ERROR. 
# If you don’t want that, you can call any of the other logging methods 
# from debug() to critical() and pass the exc_info parameter as True.



# You can (and should) define your own logger by creating an object of the Logger class
logger = logging.getLogger('example_logger')
logger.warning('This is a warning')

# The most commonly used classes defined in the logging module are the following:
# Logger: This is the class whose objects will be used in the application code directly to call the functions.
# LogRecord: Loggers automatically create LogRecord objects that have all the information related to the event being logged, 
#            like the name of the logger, the function, the line number, the message, and more.
# Handler: Handlers send the LogRecord to the required output destination, like the console or a file. 
#          Handler is a base for subclasses like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. 
#          These subclasses send the logging outputs to corresponding destinations, like sys.stdout or a disk file.
# Formatter: This is where you specify the format of the output by specifying a string format 
#            that lists out the attributes that the output should contain.

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')

# In case you want to change your logging configuration in a running application.
logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)
logger.debug('This is a debug message')


with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')