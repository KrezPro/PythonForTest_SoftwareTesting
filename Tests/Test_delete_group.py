




def test_untitled_test_case(app):
    app.Open_home_directory()
    app.session.Enter_Login(Login="admin", Password="secret")
    app.group.Delete_first_group()