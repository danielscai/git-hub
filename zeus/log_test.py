#!/usr/bin/python 

import logging

class zlogger(logging):
    def __init__(self,logfile="/var/log/zeus_api.log",
                 level='DEBUG'):
        ''' initialize log , return a log object'''
        logger=logging.getLogger()
        handler=logging.FileHandler(logfile)
        formatter=logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        self.logger=logger

    def error(self,message):
        self.logger.error(message)

    def info(self,message):
        self.logger.info(message)

    def debug(self,message):
        self.logger.debug(message)

    def warning(self,message):
        self.logger.debug(message)

logger=Zeuslogger('/var/log/zeus.log','DEBUG')
message='hello +++++ error'
logger.error(message)
message='hi ---- info'
logger.info(message)
message='wo ---- warning'
logger.warning(message)

