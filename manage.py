from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from apps import create_app, db


# 创建flask对象
app = create_app('develop')
manager = Manager(app)


# 创建数据库迁移脚本
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()