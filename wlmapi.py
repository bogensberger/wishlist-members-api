import requests as rq
from hashlib import md5


def get_md5(s):
    return md5(s.encode('utf-8')).hexdigest()


class WlmApi:
    def __init__(self, host, api_key):
        self.host = host if host[-1] == '/' else host + '/'
        self.api_key = api_key
        self.return_format = "json"  # only json handled atm
        self.session = rq.Session()
        self.session.headers.update({'User-Agent': 'WLMAPIClass'})  # dunno if it's useless but I did it
        self.authenticated = False
        self.__auth()

    def __get_url(self, ressource_name=''):
        ressource_name = ressource_name[1:] if ressource_name[0] == "/" else ressource_name
        return self.host + "wlmapi/2.0/" + self.return_format + "/" + ressource_name

    def __auth(self):
        """
        Authentificate with api key
        :return: boolean, true if everything is ok, false then
        """
        try:
            r_json = self.session.get(self.__get_url('auth')).json()
            if r_json.get("success") == 1:
                token = get_md5(r_json["lock"] + self.api_key)
                data = {
                    "key": token,
                    "support_emulation": 1,
                }
            else:
                print(r_json.get("ERROR"))
                return False
            r_json = self.session.post(self.__get_url('auth'), data=data).json()
            if r_json.get("success") == 1:
                self.authenticated = True
                return True
            else:
                print(r_json.get("ERROR"))
                return False
        except Exception as e:
            print(e)
            return False

    def post(self, resource, data):
        try:
            return self.session.post(self.__get_url(resource), data).json()
        except Exception as e:
            print(e)
            return False

    def get(self, resource, data=''):
        try:
            return self.session.get(self.__get_url(resource), params=data).json()
        except Exception as e:
            print(e)
            return False

    def put(self, resource, data=''):
        try:
            return self.session.put(self.__get_url(resource), data).json()
        except Exception as e:
            print(e)
            return False

    def delete(self, resource):
        try:
            return self.session.delete(self.__get_url(resource)).json()
        except Exception as e:
            print(e)
            return False

