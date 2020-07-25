import json
from pprint import pprint

from mitmproxy import http

def response(flow: http.HTTPFlow):
    # redirect to different host
    if "quote.json" in flow.request.url and "x=" in flow.request.url:
        ## 先接收到返回信息
        data = json.loads(flow.response.content)
        ## 对数据进行批量修改
        new_data = json_travel(data , num=100, text=1)
        ## 这步是为了方便打印
        data_mess = json.dumps(new_data, indent=2, ensure_ascii=False)
        print("=====================修改后的信息=======================================")
        print(data_mess)
        ## 改变返回信息
        flow.response.text = data_mess


def json_travel(data, array=None, text=1, num=1):
    """
    {
        "data":
        {"name":{
        "nickname": "xxxxx"
        }

        }
    }
    """
    # 如果是字典，则对字典进行遍历
    if isinstance(data, dict):
        data_new = dict()
        for k, v in data.items():
            data_new[k] = json_travel(v, array, text, num)
            if k == "name":
                data_new[k] = json_travel(v, array, text=2, num=1)

    # 如果是列表，那么对列表的每一项进行遍历
    elif isinstance(data, list):
        data_new = list()
        for item in data:
            item_new = json_travel(item, array, text, num)
            if array is None:
                data_new.append(item_new)
            else:
                pass
    # 如果是字符串，则和传入的text参数相乘、实现对字符串的修改
    elif isinstance(data, str):
        data_new = data*text
    # 如果是int或float 的数字类型，那么会对数字做一个乘积
    elif isinstance(data, int) or isinstance(data, float):
        data_new = data*num
    # 传入什么返回什么
    else:
        data_new = data
    return data_new
