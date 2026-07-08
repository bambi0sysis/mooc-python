class Recording:
    def __init__(self, length: int):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("The length should not be below zero")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length_changed: int):
        if length_changed >= 0:
            self.__length = length_changed
        else:
            raise ValueError("The length should not be below zero")
