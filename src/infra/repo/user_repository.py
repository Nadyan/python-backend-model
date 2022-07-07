from src.domain.models import Users
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel


class UserRepository:
    """
        Class to manage user repository in db
    """

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """
            Insert data into user entity
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                # Returns a named tuple with the inserted user data
                return Users(
                    id=new_user.id,
                    name=new_user.name,
                    password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
