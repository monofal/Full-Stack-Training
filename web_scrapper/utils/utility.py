"""
Utility module
"""


class Utility(object):

    @staticmethod
    def get_params(jobs):
        params = []
        for job in jobs:
            params.append((
                jobs.company_name,
                jobs.position,
                jobs.location
            ))
        return params
