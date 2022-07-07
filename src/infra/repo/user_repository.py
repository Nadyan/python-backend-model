from typing import List
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

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """
            Select data from user entity
        """

        with DBConnectionHandler() as db_connection:
            try:
                data = None
                query_data = None

                if user_id and not name:
                    data = db_connection.session.query(UsersModel).filter_by(id=user_id).one()
                elif not user_id and name:
                    data = db_connection.session.query(UsersModel).filter_by(name=name).one()
                elif user_id and name:
                    data = db_connection.session.query(UsersModel).filter_by(id=user_id, name=name).one()

                if data:
                    # selects normally returns as list
                    query_data = [data]

                return query_data
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
