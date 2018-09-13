import os
import logging
import datetime
'''
    logFile預設為當天日期
    level要記錄的等級
    format訊息格式
    datefmt時間格式
'''
class Logger:
    def __init__(self,
                 logFile = str(datetime.date.today()).replace("-", ""),
                 level = logging.DEBUG,
                 format = '%(asctime)-15s %(name)-12s [%(levelname)-8s] %(message)s',
                 datefmt = '%Y-%m-%d %H:%M:%S'):
        if not os.path.isdir("./Log"):
            os.mkdir("./Log")
            file = open("./Log/"+logFile + ".log","w",encoding="utf8")
        if os.getenv("HOSTNAME"):
            self.name = os.getenv("HOSTNAME")    # linux
        else:
            self.name = os.getenv("COMPUTERNAME")    # windows
        self.level = level
        self.foramt = format
        self.datefmt = datefmt
        self.handlers = [logging.FileHandler('./Log/' + logFile + ".log", 'a', encoding='utf-8'),]
        logging.basicConfig(level = self.level,
                            format = self.foramt,
                            datefmt = self.datefmt,
                            handlers = self.handlers)
        self.logger = logging.getLogger(self.name)
    def setDebug(self,msg):
        self.logger.debug(msg)
    def setInfo(self,msg):
        self.logger.info(msg)
    def setWarning(self,msg):
        self.logger.warning(msg)
    def setError(self,msg):
        self.logger.error(msg)
