import logging


class Logger:
    _logger = logging.getLogger('Logger')
    logging.basicConfig(filename='logs/logs.txt',
                        level=logging.INFO,
                        filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S')

    @staticmethod
    def info(message: str):
        Logger._logger.info(message)

    @staticmethod
    def error(message: str):
        Logger._logger.error(message)



