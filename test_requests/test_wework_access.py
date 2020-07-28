import requests


class TestWeworkAccess:

    def test_get_token(self):
        params = {
            "corpid": "wwe653983e4c732493",
            "corpsecret": "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
        }
        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                           params=params)
        try:
            return res.json()['access_token']
        except Exception as e:
            raise ValueError("requests token error")

    def test_add(self):
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "13800000009",
            "department": [1]
        }
        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_get_token()}",
                            json=data
                            )
        print(res.json())

    def test_get(self):
        params = {
            "access_token": self.test_get_token(),
            "userid": "zhangsan"
        }
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",
                           params=params)
        print(res.json())

    def test_update(self):
        data = {
            "userid": "zhangsan",
            "name": "wangwu"
        }
        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.test_get_token()}",
                            json=data)
        print(res.json())

    def test_delete(self):
        params = {
            "access_token": self.test_get_token(),
            "userid": "zhangsan"
        }
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",
                           params=params)
        print(res.json())
