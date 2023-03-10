import logging
import os.path

from config.config_util import getValue
from logging.handlers import TimedRotatingFileHandler
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__) #返回一个新的以文件名为名的logger

#获取当天最新的时间
fh = TimedRotatingFileHandler(filename=os.path.join(getValue("log","save_folder"),"log"),when="MIDNIGHT",interval=1)
# 定义日志输出格式
fh.setFormatter(
    logging.Formatter(
        "[%(asctime)s] [%(process)d] [%(levelname)s] - %(module)s.%(funcName)s (%(filename)s:%(lineno)d) - %(message)s"
    )
)
logger.addHandler(fh)



