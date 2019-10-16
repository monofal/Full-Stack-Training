"""
Job model
"""


class Job(object):
    """
    Hold job information
    """

    def __init__(self,
                 company_name,
                 position,
                 location,
                 unique_id,
                 job_id=None):
        self.__job_id = job_id
        self.__company_name = company_name
        self.__position = position
        self.__location = location
        self.__unique_id = unique_id

    @property
    def job_id(self):
        """
        Get id
        :return: integer , id
        """
        return self.__job_id

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

    @property
    def unique_id(self):
        """
        Get unique id
        :return: string , unique id
        """
        return self.__unique_id
