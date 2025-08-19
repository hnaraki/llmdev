import pytest
from authenticator import Authenticator


@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth


# 各メソッドのテスト
def test_register(authenticator):
    # ユーザーを登録し、正しく登録されているかを確認
    authenticator.register("testuser", "password123")
    #   ユーザー登録されているか
    assert "testuser" in authenticator.users
    #   パスワードが正しく保存されているかを確認
    assert authenticator.users["testuser"] == "password123"
    # 同じユーザーを登録し、例外が発生することを確認
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authenticator.register("testuser", "password123")


def test_login(authenticator):
    # 正しいユーザー名とパスワードでログインできるかを確認
    authenticator.register("testuser", "password123")
    assert authenticator.login("testuser", "password123") == "ログイン成功"
    # 誤ったパスワードでログインし、例外が発生することを確認
    with pytest.raises(
        ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"
    ):
        authenticator.login("testuser", "wrongpassword")
