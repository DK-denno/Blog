from app import create_app
from flask_script import Manager,Server

manager=Manager()
manager = Manager(app)
manager.add_command('server',Server)


create_app('development')


if __name__=='__main__':
    manager.run()