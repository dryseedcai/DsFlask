"""
Python中两种方式发送请求
# urllib
# requests
"""

# from urllib import request
import requests


class HTTP:

    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code == 200:
            return r.json() if return_json else r.text
        else:
            return {} if return_json else ''
