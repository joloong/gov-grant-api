from models import db
from models.MemberModel import MemberModel


def get_members(page_size=20, page_num=0):
    members = MemberModel.query.limit(
        page_size).offset(page_num * page_size).all()

    members_json = []

    for member in members:
        members_json.append(member.serialize())

    return members_json


def create_member(name, gender, marital_status, occupation_type, annual_income, dob):
    new_member = MemberModel(name, gender, marital_status,
                             occupation_type, annual_income, dob)
    db.session.add(new_member)
    db.session.commit()

    return new_member.serialize()
