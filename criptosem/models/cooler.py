from sqlalchemy.orm import Mapped

from core.models import Base


class cooler(Base):
    __tablename__ = 'products'  # Можно явно указать, если в базовом классе не использован declared_attr для именования таблиц

    name: Mapped[str]           
    description: Mapped[str]
    price: Mapped[int]