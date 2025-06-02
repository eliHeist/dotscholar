from ninja import ModelSchema, Schema

from .models import User, UserProfile



class UserProfileSchema(ModelSchema):
    class Meta:
        model = UserProfile
        fields = ["gender", "phone_1", "phone_2"]

class UserSchema(ModelSchema):
    profile: UserProfileSchema = None
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "username", "is_active", "is_teacher"]
    
    
    @staticmethod
    def resolve_profile(obj):
        return obj.profile or None




class UserInSchema(Schema):
    first_name: str
    last_name: str
    email: str
    is_teacher: bool
    gender: str
    phone_1: str
    phone_2: str
    