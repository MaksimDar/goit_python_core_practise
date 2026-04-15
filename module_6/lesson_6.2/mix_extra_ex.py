from enum import Enum
from collections import UserList
from dataclasses import dataclass

class UserRole(Enum):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

class UnauthorizedAccessError(Exception):
    pass

@dataclass
class Country:
    name: str
    code: str

@dataclass
class User:
    username: str
    email: str
    role: UserRole
    country: Country

class RestrictedUserList(UserList):
    def __init__(self, *args,allowed_roles=None,**kwargs):
        self.allowed_roles = allowed_roles or [UserRole.ADMIN]
        super().__init__(*args,**kwargs)

    def append(self,user) -> None:
        if user.role not in self.allowed_roles:
            raise UnauthorizedAccessError('You do not have permission to add user')
        super().append(user)

    def extend(self,users) -> None:
        for user in users:
            self.append(user)

    def remove(self,user) -> None:
        if user not in self.allowed_roles:
            raise UnauthorizedAccessError('You do not have permission to remove user')
        super().remove(user)

if __name__ == '__main__':
    USA = Country(name='United States', code='us')
    UK = Country(name='United Kingdom', code='uk')

    admin = User(username='Admin', email='adminname@admin.com', role=UserRole.ADMIN, country=USA)
    moderator = User(username='Moderator', email='moderatorname@moderator.com', role=UserRole.MODERATOR, country=UK)
    user = User(username='User', email='username@admin.com', role=UserRole.USER, country=USA)

    restricted_users = RestrictedUserList(allowed_roles=[UserRole.ADMIN, UserRole.MODERATOR])
    restricted_users.extend([admin, moderator])

    try:
        restricted_users.append(user)
    except UnauthorizedAccessError as e:
        print(e)

    