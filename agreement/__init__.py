from logging.config import dictConfig

from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.cfg', silent=True)


def _startup():
    dictConfig(app.config['LOGGING'])
    from agreement.controllers import test


_startup()
