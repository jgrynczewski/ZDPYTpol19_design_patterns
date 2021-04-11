import abc

from house import House


class IHouseBuilder(abc.ABC):
    def get_house(self):
        return self._house

    def new_house(self):
        self._house = House()

    @abc.abstractmethod
    def build_wall(self):
        pass

    @abc.abstractmethod
    def install_door(self):
        pass

    @abc.abstractmethod
    def install_window(self):
        pass

    @abc.abstractmethod
    def lay_floor(self):
        pass

    @abc.abstractmethod
    def plant_garden(self):
        pass

    @abc.abstractmethod
    def install_garage(self):
        pass

    @abc.abstractmethod
    def excavate_pool(self):
        pass
