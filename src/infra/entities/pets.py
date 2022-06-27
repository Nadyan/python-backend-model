import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """
        Definição de tipos de animais
    """

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    """
        Tabela Pets
    """

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, owner={self.user_id}]"
