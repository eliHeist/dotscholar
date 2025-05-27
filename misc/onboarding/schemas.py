from ninja import Schema


class UserSchema(Schema):
    email: str
    password: str
    password_confirm: str
    first_name: str
    last_name: str

class SchoolSchema(Schema):
    name: str
    short_name: str


class CreateUserAndSchoolSchema(Schema):
    user: UserSchema
    school: SchoolSchema