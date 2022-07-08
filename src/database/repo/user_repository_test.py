from faker import Faker
from src.database.config import DBConnectionHandler
from src.database.entities import Users as UsersModel
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


def test_select_user():
    """
        Should select a user by id or name or both
    """

    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()

    new_user = UsersModel(id=user_id, name=name, password=password)

    print(new_user)

    engine = db_connection_handler.get_engine()
    engine.execute(
        "INSERT INTO users (id, name, password) VALUES ('{}', '{}', '{}');".format(
            user_id, name, password
        )
    )

    query_user_by_id = user_repository.select_user(user_id=user_id)
    query_user_by_name = user_repository.select_user(name=name)
    query_user_by_both = user_repository.select_user(user_id=user_id, name=name)

    assert new_user in query_user_by_id
    assert new_user in query_user_by_name
    assert new_user in query_user_by_both

    engine.execute(
        "DELETE FROM users WHERE id='{}';".format(user_id)
    )
