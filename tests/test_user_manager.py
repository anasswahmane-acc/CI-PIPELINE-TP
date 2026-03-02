from app.user_manager import UserManager


def test_add_user():
    manager = UserManager()
    manager.add_user("Anas")
    assert manager.count_users() == 1


def test_remove_user():
    manager = UserManager()
    manager.add_user("Anas")
    manager.remove_user("Anas")
    assert manager.count_users() == 0
