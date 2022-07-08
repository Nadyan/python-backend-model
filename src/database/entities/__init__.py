from .pets import Pets
from .users import Users

"""
    Após a criação das entidades, ir no terminal python:

    $ python
    $ >>> from src.infra.config import *
    $ >>> from src.infra.entities import *
    $ >>> db_conn = DBConnectionHandler()
    $ >>> engine = db_conn.get_engine()
    $ >>> Base.metadata.create_all(engine)
    $ >>> exit()

    Será criado o arquivo storage.db
"""
