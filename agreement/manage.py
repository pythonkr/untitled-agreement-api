from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from agreement import app

manager = Manager(app)


@manager.command
def runserver():
    app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    manager.run()
