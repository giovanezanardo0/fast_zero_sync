from sqlalchemy import select

from fast_zero.models import User


def test_creat_user(session):
    user = User(username='gaz', email='mail@mail.com', password='123')
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'mail@mail.com'))
    assert result.username == 'gaz'
