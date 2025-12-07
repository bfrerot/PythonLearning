########## LOGGING MODULE ##########


# Python Standard Library provides a useful module called logging to log events occurring in the application
# Logs are most often used to find the cause of an error
# By default, Python and its modules provide many logs informing you of the causes of errors
# However, it's good practice to create our own logs that may be useful to you or other programmers

# In Python, weu can store logs in different places
# Most often it's in the form of a file
# it can also be an output stream, or even an external service


## Importing the logging module
import logging



## Logger object - different ways to create loggers
import logging

logger = logging.getLogger()
hello_logger = logging.getLogger('hello')
hello_world_logger = logging.getLogger('hello.world')
recommended_logger = logging.getLogger(__name__)


## Logging levels

#default logging levels provided by the logging module are as follows:
'''
Level name	  Value
CRITICAL	  50
ERROR	      40
WARNING	      30
INFO	      20
DEBUG	      10
NOTSET	       0
'''

# default log format includes the level, the logger name and the message we define
import logging

logging.basicConfig()

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')
# CRITICAL:root:Your CRITICAL message
# ERROR:root:Your ERROR message
# WARNING:root:Your WARNING message

# => INFO and DEBUG messages are not shown by default because the default logging level is WARNING
# To see INFO and DEBUG messages, we need to set the logging level to a lower level
# This can be done by passing the setLevel method to the logger object

import logging

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')
'''
CRITICAL:root:Your CRITICAL message
ERROR:root:Your ERROR message
WARNING:root:Your WARNING message
INFO:root:Your INFO message
DEBUG:root:Your DEBUG message
'''


## Logging to a file

import logging

logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a')
# basicConfig method takes three arguments
#   1st = logging level equal to CRITICAL ==> only messages with this level will be processed
#   2nd = passing a filename to the second argument creates a FileHandler object instead of a StreamHandler object
#         the logs no longer appear in the console, after setting the filename argument, all logs will be directed to the specified file
#   3rd = passing the last filemode argument with the value 'a' (default mode) means that new logs will be appended to this file


logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

# Only the CRITICAL message will be logged to the 'prod.log' file
# files contains:
'''
CRITICAL:root:Your CRITICAL message
'''


## Logging with a specific format

import logging   # import the logging module

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'  # define the log format

logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a', format=FORMAT) # configure logging to write to 'prod.log' with CRITICAL level and specified format

logger = logging.getLogger() # get the root logger

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')
'''
CRITICAL:root:Your CRITICAL message
root:CRITICAL:2025-11-21 07:40:51,630:Your CRITICAL message
root:CRITICAL:2025-11-21 07:40:54,991:Your CRITICAL message
root:CRITICAL:2025-11-21 07:41:10,462:Your CRITICAL message
root:CRITICAL:2025-11-24 08:12:40,642:Your CRITICAL message
'''


## use of FileHandler to log messages to a file

import logging

logger = logging.getLogger(__name__) # create a logger object with the name of the current module

handler = logging.FileHandler('prod.log', mode='w') # create a FileHandler object to write logs to 'prod.log' in write mode
handler.setLevel(logging.CRITICAL) # set the logging level of the handler to CRITICAL; by default, the level is NOTSET, and all messages are processed since WARNING (default level)

logger.addHandler(handler) # add the handler to the logger

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

# Each logger can have several handlers added
# One handler can save logs to a file, while another can send them to an external service


## Complete example

import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s' # define the log format

logger = logging.getLogger(__name__) # get a named logger

handler = logging.FileHandler('prod.log', mode='a') # create a FileHandler to write logs to 'prod.log' in append mode, write 'w' would overwrite existing logs
handler.setLevel(logging.CRITICAL) # set the logging level of the handler to CRITICAL

formatter = logging.Formatter(FORMAT) # create a Formatter object with the specified format
handler.setFormatter(formatter) # set the formatter for the handler

logger.addHandler(handler) # add the handler to the logger

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

# log line example
# __main__:CRITICAL:2019-10-10 20:40:05,119:Your CRITICAL message
# logger name: log level: timestamp: message