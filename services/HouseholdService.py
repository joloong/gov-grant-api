from models import db
from models.HouseholdModel import HouseholdModel


def get_households(page_size=20, page_num=0):
    households = HouseholdModel.query.limit(
        page_size).offset(page_num * page_size).all()

    households_json = []

    for household in households:
        households_json.append(household.serialize())

    return households_json


def create_household(postal_code, level, unit, housing_type):
    new_household = HouseholdModel(postal_code, level, unit, housing_type)
    db.session.add(new_household)
    db.session.commit()

    return new_household.serialize()
