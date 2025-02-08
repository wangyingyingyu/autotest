from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str = '12'


def x() -> int:
    return 1


user1 = User(username='admin', password='123')

print(user1.model_dump())
print(user1.model_dump_json(indent=2))

user1 = User.model_validate_json('{"username": "admin", "password": "123"}')
print(user1)
