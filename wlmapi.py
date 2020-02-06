import requests as rq
from hashlib import md5


def get_md5(s):
    return md5(s.encode('utf-8')).hexdigest()


class WlmApi:
    def __init__(self, host, api_key, return_format):
        self.host = host if host[-1] == '/' else host + '/'
        self.api_key = api_key
        self.return_format = return_format  # php, xml or json
        self.session = rq.Session()
        self.session.headers.update({'User-Agent': 'WLMAPIClass'})  # dunno if it's useless but I did it

    def get_url(self, ressource_name=''):
        return self.host + "wlmapi/2.0/" + self.return_format + "/" + ressource_name

    def _auth(self):
        # TODO : gere le fail
        r_json = self.session.get(self.get_url('auth')).json()
        token = get_md5(r_json["lock"] + self.api_key)
        data = {
            "key": token,
            "support_emulation": 1,
        }
        r = self.session.post(self.get_url('auth'), data=data)

        return  # TODO : ok ou pas