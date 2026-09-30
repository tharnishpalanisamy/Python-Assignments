from abc import abstractmethod , ABC 

class BaseRepository(ABC) : 

    @abstractmethod
    def get_all(self) :
        pass 

    @abstractmethod
    def find(self , id : int ) :
        pass




