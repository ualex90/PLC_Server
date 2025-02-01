from sqlalchemy.orm import Mapped

from core.models import Base


class Сooler(Base):
    """Модель "Охладитель"""

    name: Mapped[str]
    state: Mapped[str]
    ctrl_word: Mapped[int]
    StateWord: Mapped[int]
    FaultWord: Mapped[int]
    MPState: Mapped[bool]
    TemperCubeOn_Value: Mapped[float]
    TimeStopAuto_Value: Mapped[float]
