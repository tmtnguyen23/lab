class Television:
    """
    Class to work on the current status of a TV
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to set the default values for the TV status, channel, volume
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__is_on: bool = False

    def power(self) -> None:
        """
        Function to turn on or turn off the TV
        """
        if self.__is_on:
            self.__is_on = False
        else:
            self.__is_on = True

    def channel_up(self) -> None:
        """
        Function to move up the TV's current channel
        """
        if self.__is_on:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Function to move down the TV's current channel
        """
        if self.__is_on:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Function to increase the TV volume
        """
        if self.__is_on:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Function to turn down the TV volume
        """
        if self.__is_on and self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to return the TV current status
        :return: TV status including on/off, channel and volume
        """
        return (f'TV status: Is on = {self.__is_on}, Channel = {self.__channel}, Volume = {self.__volume}')

