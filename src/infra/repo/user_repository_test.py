from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """
        Should insert user
    """

    # Generates random data
    name = faker.name()
    password = faker.word()

    # Creates the connection handler
    engine = db_connection_handler.get_engine()

    # Insert a new user into db
    new_user = user_repository.insert_user(name, password)
    # Selects the new user inserted
    query_user = engine.execute(
        "SELECT * FROM users WHERE id = '{}';".format(new_user.id)
    ).fetchone()
    # Deletes the new user
    engine.execute(
        "DELETE FROM users WHERE id='{}';".format(new_user.id)
    )
    # Compares the inserted user and the selected user, should be the same
    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
