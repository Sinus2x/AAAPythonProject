from typing import Literal
import abc


class Pizza(abc.ABC):
    """
    Хотел сделать абстрактный класс, но, кажется,
    здесь достаточно обычного базового.
    """

    """
    Вообще поле emoji необязательно определять, т.к. оно 
    всё равно будет перезаписано в наследниках (код не сократится). 
    Но для того, чтобы обозначить все аттрибуты пиццы, я всё-таки определил emoji в базовом классе. 
    """

    def __init__(self, size: Literal['L', 'XL'] = 'L'):
        """
        Буду исходить из того, что после инстанса размер нельзя изменить, будто пицца уже заказана.
        И сделаю size приватным
        """
        assert size.upper() in ['L', 'XL'], "The size doesn't exist"
        self.__size = size.upper()

    @property
    def size(self):
        return self.__size

    @classmethod
    @property
    @abc.abstractmethod
    def emoji(cls):
        pass

    @classmethod
    @property
    @abc.abstractmethod
    def components(cls):
        """
        Чтобы можно было обратиться за компонентами как к классу, так и к объекту.
        Ведь от объекта к объекту меняется только размер пиццы.
        """
        return ['tomato_sauce', 'mozzarella']

    @classmethod
    def __dict__(cls):
        return {cls.__name__: ', '.join(cls.components)}

