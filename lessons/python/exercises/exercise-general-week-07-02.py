## THIS CODE IS NOT BEST PRACTICE - ITS JUST FOR TEACHING AND LEARNING


from enum import Enum
import secrets
import hashlib

##---------------------------------------------------------------------------##
class Permissions(Enum):
    INSERT_COMMENT = "IC"
    SELECT_COMMENT = "SC"
    UPDATE_COMMENT = "UC"
    DELETE_COMMENT = "DC"


class Type(Enum):
    ADMIN = "A"
    CLIENT = "C"
    GUEST = "G"
    UNSET = "U"


class Auth:
    token = None
    is_logged_in = False
    permissions: list[Permissions] = []

    def generate_token(self):
        self.token = secrets.token_hex(16)


class User:
    user = None
    password = None
    user_type = Type.UNSET

    def __init__(self, user, password) -> None:
        self.user = user
        self.hash(password)

    def hash(self, password: str):
        # IMPORTANT: Seed, Pepper, Salt ???
        hash_object = hashlib.md5(password.encode())
        self.password = hash_object.digest().hex()

    def __str__(self) -> str:
        # IMPORTANT: THIS IS BAD PRACTICE - ITS JUST FOR TEACHING AND LEARNING
        return f"{self.user} - {self.user_type} - {self.password}"

    def __repr__(self) -> str:
        return self.__str__()


class GuestUser(User, Auth):
    permissions = [Permissions.SELECT_COMMENT]
    user_type = Type.GUEST


class ClientUser(User, Auth):
    permissions = [Permissions.SELECT_COMMENT, Permissions.INSERT_COMMENT]
    user_type = Type.CLIENT


class AdminUser(User, Auth):
    permissions = [
        Permissions.SELECT_COMMENT,
        Permissions.INSERT_COMMENT,
        Permissions.UPDATE_COMMENT,
        Permissions.DELETE_COMMENT,
    ]
    user_type = Type.ADMIN


##---------------------------------------------------------------------------##
users = []

users.append(AdminUser("Admin1", "password1"))
users.append(AdminUser("Admin2", "password2"))
users.append(ClientUser("Client1", "password1"))
users.append(ClientUser("Client2", "password2"))
users.append(GuestUser("Guest1", "password1"))
users.append(GuestUser("Guest2", "password2"))

users[0].generate_token()
print(f"{users[0].is_logged_in} - {users[0].token}")

print(users)
