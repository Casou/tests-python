from tests_basile.model import Parameter, ParameterEnum, PeopleInterest, People


def init_default_data(db):
    # Init mandatory parameters
    parameters = Parameter.query.all()
    for default_param in list(ParameterEnum):
        found_param = filter(lambda p: p.key == default_param.key, parameters)
        if len(list(found_param)) == 0:
            parameter = Parameter(key=default_param.key, description=default_param.description,
                                  value=default_param.default_value)
            db.session.add(parameter)

    # interest = PeopleInterest(name="Basket")
    # people = People(name="Basile", surname="Parent", sex=1, birth_date=None, arrival_date=None,
    #                 email="basile.parent@proxiad.com", phone="06.06.06.06.06", city="Lille",
    #                 picture_index=25, work_place="Lille", job="Développeur.se", interets=[interest])
    #
    # db.session.add(people)
    db.session.commit()
