"""
App orchestration file for PL_Stat app.
Author: Maciej Cisowski
"""
from flask import Flask
from config import logger_root_config
from logging import getLogger
from logging.config import dictConfig as loggerConfig
from app.main import main as main_bp

app = Flask(__name__)

loggerConfig(config=logger_root_config)
logger = getLogger(__name__)


app.register_blueprint(main_bp)


if __name__ == '__main__':
    app.run()
