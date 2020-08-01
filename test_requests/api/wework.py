from test_requests.api.base_api import BaseApi


class WeWork(BaseApi):
    def test_get_token(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "wwe653983e4c732493",
                "corpsecret": "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
            }
        }
        res = self.send_api(data)
        try:
            return res['access_token']
        except Exception as e:
            raise ValueError("requests token error")
