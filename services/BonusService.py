from collections import defaultdict
from datetime import date

from models import db
from models.HouseholdModel import HouseholdModel
from models.FamilyModel import FamilyModel
from models.MemberModel import MemberModel


def get_all_rows():
    rows = db.session.query(FamilyModel, MemberModel, HouseholdModel).filter(
        FamilyModel.member_id == MemberModel.id).filter(
        FamilyModel.household_id == HouseholdModel.id).all()

    return rows


def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def get_household_with_children(rows, children_age: int) -> list:
    household_with_children = []
    for _, member, household in rows:
        age = calculate_age(member.dob)
        if age < children_age:
            household_with_children.append(household.id)

    return household_with_children


def get_household_with_elder(rows, elder_age: int) -> list:
    household_with_elder = []
    for _, member, household in rows:
        age = calculate_age(member.dob)
        if age > elder_age:
            household_with_elder.append(household.id)

    return household_with_elder


def get_household_below_income(rows, max_income: int) -> list:
    household_income = defaultdict(int)
    for _, member, household in rows:
        household_income[household.id] += member.annual_income

    household_below_income = []
    for household_id, income in household_income.items():
        if income < max_income:
            household_below_income.append(household_id)

    return household_below_income


def get_household_husband_wife(rows) -> list:
    household_husband = defaultdict(int)
    household_wife = defaultdict(int)
    for _, member, household in rows:
        if member.marital_status == "married":
            if member.gender == "male":
                household_husband[household.id] += 1
            elif member.gender == "female":
                household_wife[household.id] += 1

    pairs = list(household_husband.keys() & household_wife.keys())
    return pairs


def get_family_from_household_ids(household_ids):
    filtered_rows = db.session.query(FamilyModel, MemberModel, HouseholdModel).filter(
        FamilyModel.household_id.in_(household_ids)).filter(
        FamilyModel.household_id == HouseholdModel.id).filter(
        FamilyModel.member_id == MemberModel.id).all()

    family_json = defaultdict(list)
    for _, member, household in filtered_rows:
        family_member_json = {
            "household_id": household.id,
            "household_type": household.housing_type,
            "member_id": member.id,
            "name": member.name,
            "gender": member.gender,
            "marital_status": member.marital_status,
            "occupation_type": member.occupation_type,
            "annual_income": member.annual_income,
            "dob": member.dob
        }
        family_json[household.id].append(family_member_json)

    return family_json


def get_student_encouragement_bonus(children_age=16, max_income=150000):
    rows = get_all_rows()

    household_with_children = get_household_with_children(rows, children_age)
    household_below_income = get_household_below_income(rows, max_income)

    household_ids = list(set(household_with_children)
                         & set(household_below_income))

    filtered_rows = db.session.query(FamilyModel, MemberModel, HouseholdModel).filter(
        FamilyModel.household_id.in_(household_ids)).filter(
        FamilyModel.household_id == HouseholdModel.id).filter(
        FamilyModel.member_id == MemberModel.id).all()

    family_json = get_family_from_household_ids(household_ids)

    return family_json


def get_family_togetherness_scheme(children_age=18):
    rows = get_all_rows()

    household_husband_wife = get_household_husband_wife(rows)
    household_with_children = get_household_with_children(rows, children_age)

    household_ids = list(set(household_with_children)
                         & set(household_husband_wife))

    family_json = get_family_from_household_ids(household_ids)

    return family_json


def get_elder_bonus(elder_age=50):
    rows = get_all_rows()
    household_with_elder = get_household_with_elder(rows, elder_age)

    family_json = get_family_from_household_ids(household_with_elder)

    return family_json


def get_baby_sunshine_grant(children_age=5):
    rows = get_all_rows()

    household_with_children = get_household_with_children(rows, children_age)
    family_json = get_family_from_household_ids(household_with_children)

    return family_json


def get_yolo_gst_grant(max_income=100000):
    rows = get_all_rows()

    household_below_income = get_household_below_income(rows, max_income)
    family_json = get_family_from_household_ids(household_below_income)

    return family_json
