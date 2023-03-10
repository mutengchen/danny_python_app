#TODO 读取配置文件里面的东西
import configparser
config = configparser.ConfigParser()
config.read('config/config.ini')
def getValue(section,key):
    return config.get(section,key)

