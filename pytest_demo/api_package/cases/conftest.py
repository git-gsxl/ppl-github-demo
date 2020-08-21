import pytest
import re
from api_package.api.api_login import Login_api


@pytest.fixture(scope="session")
def get_token():
    res = Login_api().login()
    token = re.findall('"datas":"(.+?)",', res)
    return token[0]


# 需要cookies传入下一个接口
@pytest.fixture(scope="session")
def get_cookie():
    cookie = Login_api().login().cookies
    return cookie


