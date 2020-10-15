from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser


def test_add_user():
    user = PasswordUser(models.User())
    user.username = 'admin'
    user.email = 'admin@test.cn'
    user.password = 'admin'
    user.superuser = 1
    session = settings.Session()
    session.add(user)
    session.commit()
    session.close()