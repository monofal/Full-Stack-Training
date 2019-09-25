"""
Scrapper Module
"""
import re

import requests
from bs4 import BeautifulSoup

from web_scrapper.model.job import Job
from web_scrapper.utils.log_handler import LogHandler


class Scrapper(object):
    """
    Extract data from hacker news website
    """
    def __init__(self,
                 url):
        self.__url = url
        self.__soup = None

    def scrap_website(self):
        """
        Start extracting required information from website
        :return: list of job object
        """
        try:
            response = requests.get(self.__url)
            soup = BeautifulSoup(response.text, 'html.parser')

            jobs = []
            # Get by tag and class name
            for job_link in soup.findAll("a", class_="storylink"):
                job_text = job_link.findAll(text=True)[0]

                company_name = self.extract_company_name(job_text)
                position = self.extract_job_position(job_text)
                location = self.extract_location(job_text)

                jobs.append(Job(company_name,
                                position,
                                location,
                                '{}_{}_{}'.format(company_name, position, location)))
        except:
            LogHandler.log('exception', 'Exception Occurred')

        return jobs

    @staticmethod
    def extract_company_name(text):
        """
        Extract company name from text
        :param text: description from hacker news
        :return: string , company name
        """
        # Split text by hiring,is hiring , is looking for , looking for
        company_name = re.split("hiring|looking for|is hiring|is looking for",
                                text, flags=re.IGNORECASE)
        # if match found return everything on left side otherwise return empty string
        return company_name[0] if len(company_name) > 1 else ''

    @staticmethod
    def extract_location(text):
        """
        Extract location from text
        :param text: description from hacker news
        :return: string , company location
        """
        location = re.split(" in ", text, flags=re.IGNORECASE)
        # if match found return everything on right side otherwise return empty string
        return location[1] if len(location) > 1 else ''

    @staticmethod
    def extract_job_position(text):
        """
        Extract job position from text
        :param text: description from hacker news
        :return: string , job position
        """
        #
        split_text = re.split("hiring|hiring a|hiring an",
                              text, flags=re.IGNORECASE)
        # if match found split again
        position = re.split(" in ", split_text[1] if len(split_text) > 1 else '', flags=re.IGNORECASE)
        # if match found, return string on the left side
        return position[0]
