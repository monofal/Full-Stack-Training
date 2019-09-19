"""
Job model
"""


class Job(object):

    def __init__(self,
                 company_name,
                 position,
                 location):
        self.__company_name = company_name
        self.__position = position
        self.__location = location

    @property
    def company_name(self):
        """
        Get company name
        :return: string , company name
        """
        return self.__company_name

    @property
    def position(self):
        """
        Get __position
        :return: string , position
        """
        return self.__position

    @property
    def location(self):
        """
        Get location
        :return: string , location
        """
        return self.__location
