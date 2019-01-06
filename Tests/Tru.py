# -*- coding: utf-8 -*-
from fixture.application import Application
from model.Group import Group
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
        app.Open_home_directory()
        app.session.Enter_Login(Login="admin", Password="secret")
        app.group.Create(Group(name="rty", header="recfghh", footer="dffgdfgdg"))


def test_untitled_test_case2(app):
        app.Open_home_directory()
        app.session.Enter_Login(Login="admin", Password="secret")
        app.group.Create(Group(name="", header="", footer=""))



