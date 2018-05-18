from common import constant
import json


class CommonResponse:
    def __init__(self, data, code = constant.CODE_SUCCESS, msg = constant.MSG_SUCCESS):
        self.code = code
        self.msg = msg
        self.data = data

    def __str__(self):
        return self.code

    def toDict(self):
        return {
            "data": self.data,
            "msg": self.msg,
            "code": self.code
        }