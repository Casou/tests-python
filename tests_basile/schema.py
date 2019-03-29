from tests_basile import ma


class TokenSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "room_name", "expirationDate")

    # # Smart hyperlinking
    # _links = ma.Hyperlinks(
    #     {"self": ma.URLFor("user_detail", id="<id>"), "collection": ma.URLFor("users")}
    # )


token_schema = TokenSchema()
tokens_schema = TokenSchema(many=True)


class ParameterSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "key", "description", "value")


parameter_schema = ParameterSchema()
parameters_schema = ParameterSchema(many=True)


class PeopleInterestSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name")


people_interest_schema = PeopleInterestSchema()
people_interests_schema = PeopleInterestSchema(many=True)


class PeopleSchema(ma.Schema):
    interests = ma.Nested(PeopleInterestSchema, many=True)

    class Meta:
        # Fields to expose
        fields = ("id", "name", "surname", "sex", "birth_date", "arrival_date", "email", "phone", "city",
                  "picture_index", "work_place", "job", "interests")


people_schema = PeopleSchema()
peoples_schema = PeopleSchema(many=True)
