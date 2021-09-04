from models import db
from models.HouseholdModel import HouseholdModel
from models.FamilyModel import FamilyModel
from models.MemberModel import MemberModel


def add_family_member(household_id, member_id):
    new_family_member = FamilyModel(household_id, member_id)
    db.session.add(new_family_member)
    db.session.commit()

    return new_family_member.serialize()


def get_family(household_id):
    rows = db.session.query(FamilyModel, MemberModel, HouseholdModel).filter(
        FamilyModel.household_id == household_id).filter(
        FamilyModel.member_id == MemberModel.id).filter(
        FamilyModel.household_id == HouseholdModel.id).all()

    family_json = []
    for _, member, household in rows:
        family_member_json = {
            "household_type": household.housing_type,
            "member_id": member.id,
            "name": member.name,
            "gender": member.gender,
            "marital_status": member.marital_status,
            "occupation_type": member.occupation_type,
            "annual_income": member.annual_income,
            "dob": member.dob
        }
        family_json.append(family_member_json)

    return family_json


def remove_family_member(household_id, member_id):
    db.session.query(FamilyModel).filter(FamilyModel.household_id ==
                                         household_id and FamilyModel.member_id == member_id).delete()
    db.session.commit()
