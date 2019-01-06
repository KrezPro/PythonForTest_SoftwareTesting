# -*- coding: utf-8 -*-
from application import Application
from Group import Group
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
        app.Open_home_directory()
        app.Enter_Login(Login="admin", Password="secret")
        app.Create_Group(Group(name="rty", header="recfghh", footer="dffgdfgdg"))
        app.See_result()

def test_untitled_test_case2(app):
        app.Open_home_directory()
        app.Enter_Login(Login="admin", Password="secret")
        app.Create_Group(Group(name="", header="", footer=""))
        app.See_result()


