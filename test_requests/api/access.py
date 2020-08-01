from test_requests.api.base_api import BaseApi


class Access(BaseApi):
    def test_add(self, userid, name, mobile, token, department=None):
        if department is None:
            department = [1]
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department
            }
        }

        res = self.send_api(data)
        return res

    def test_get(self, userid, token):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "access_token": token,
                "userid": userid
            }

        }

        res = self.send_api(data)
        return res

    def test_update(self, userid, name, token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
            "json": {
                "userid": userid,
                "name": name
            }
        }

        res = self.send_api(data)
        return res

    def test_delete(self, userid, token):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": token,
                "userid": userid
            }
        }
        res = self.send_api(data)
        return res
