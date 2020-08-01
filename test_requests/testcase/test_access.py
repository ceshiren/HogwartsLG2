import re
import pytest
from requests import Session

from test_requests.api.access import Access
from test_requests.api.wework import WeWork


class TestAccess:
    @pytest.fixture(scope="session")
    def token(self):
        yield WeWork().test_get_token()

    def setup(self):
        self.access = Access()

    def create_muti_data(self):
        data = [("wu12345wu" + str(x), "zhangsan1", "138%08d" % x) for x in range(20)]
        return data

    def test_get(self, token):
        print(self.access.test_get("zhangsanss1", token))

    def test_add(self, token):
        print(self.access.test_add("wu12345wu123", "zhangsan123", "13800000000", token))

    @pytest.mark.parametrize("userid, name, mobile", create_muti_data("xx"))
    def test_all(self, userid, name, mobile, token):
        try:
            # 创建一个成员, 对结果断言
            assert "created" == self.access.test_add(userid, name, mobile, token)['errmsg']
        except AssertionError as e:
            if "userid existed" in e.__str__():
                self.access.test_delete(userid, token)
            if "mobile existed" in e.__str__():
                delete_userid = re.findall(":(.*)'$", e.__str__())
                self.access.test_delete(delete_userid, token)
            assert "created" == self.access.test_add(userid, name, mobile, token)['errmsg']
        # 查询成员信息，对结果断言
        assert name == self.access.test_get(userid, token)['name']
        # 更新一个成员
        assert "updated" == self.access.test_update(userid, "wnangwu", token)['errmsg']
        assert "wnangwu" == self.access.test_get(userid, token)['name']
        # 删除
        assert "deleted" == self.access.test_delete(userid, token)['errmsg']
        assert 60111 == self.access.test_get(userid, token)['errcode']

    def test_session(self, token):
        s = Session()
        s.params = {"access_token": token}
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "userid": "zhangsanss1"
            }

        }
        print(s.request(**data).json())