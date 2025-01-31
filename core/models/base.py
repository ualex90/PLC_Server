from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive                # Указываем имена таблиц такие как названия классов во множественном числе
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'

    # Mapped — это современный способ аннотировать типы данных для колонок в моделях SQLAlchemy. 
    #Он позволяет более четко указать, что переменная представляет собой колонку таблицы в базе данных, 
    #делая код более читаемым и понятным.
    #mapped_column — это функция, которая используется для создания колонок в моделях SQLAlchemy. 
    # Она принимает в качестве аргументов тип данных колонки и дополнительные параметры, 
    # такие как primary_key, nullable, default и так далее
    id: Mapped[int] = mapped_column(primary_key=True)   