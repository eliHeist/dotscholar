from ninja import Schema
from accounts.schemas import UserSchema
from schools.schools.schemas import SchoolSchema


# Define the schema for creating a new User and School
class CreateUserAndSchoolSchema(Schema):
    user: UserSchema
    school: SchoolSchema