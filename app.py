from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date

from config import Config
from models import db, HouseholdModel, MemberModel, FamilyModel
from services import HouseholdService, MemberService, FamilyService
from exceptions.MissingKeyError import MissingKeyError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)
migrate = Migrate(app, db)


def get_page_size_and_num(request):
    page_size = int(request.args.get("page_size", 20))
    if page_size <= 1:
        page_size = 1

    page_num = int(request.args.get("page_num", 0))
    if page_num <= 0:
        page_num = 0

    return page_size, page_num


def custom_dict_get(data, key, default=None, exception=True):
    value = data.get(key, default)
    if not value and exception:
        raise MissingKeyError(key)
    else:
        return value


@app.route("/")
def hello():
    return "Welcome to API!"


@app.route("/household", methods=["GET", "POST", "DELETE"])
def household_handler():
    # Task 1, 3, 6
    if request.method == "GET":
        page_size, page_num = get_page_size_and_num(request)

        households = HouseholdService.get_households(page_size, page_num)
        return {
            "households": households
        }
    elif request.method == "POST":
        data = request.get_json()
        postal_code = custom_dict_get(data, "postal_code")
        level = custom_dict_get(data, "level")
        unit = custom_dict_get(data, "unit")
        housing_type = custom_dict_get(data, "housing_type")

        household = HouseholdService.create_household(
            postal_code, level, unit, housing_type
        )

        return {
            "household": household
        }
    elif request.method == "DELETE":  # TODO
        return "DELETE not implemented yet."


@app.route("/household/<household_id>", methods=["GET"])
def family_handler(household_id):
    # Task 4
    family = FamilyService.get_family(household_id)
    return {
        "family": family
    }


@app.route("/household/<household_id>/member", methods=["POST"])
def family_member_handler(household_id):
    # Task 2
    data = request.get_json()
    name = custom_dict_get(data, "name")
    gender = custom_dict_get(data, "gender")
    marital_status = custom_dict_get(data, "marital_status")
    occupation_type = custom_dict_get(data, "occupation_type")
    annual_income = int(custom_dict_get(data, "annual_income"))
    dob = date(1997, 11, 19)  # TODO
    member = MemberService.create_member(
        name, gender, marital_status, occupation_type, annual_income, dob)

    family = FamilyService.add_family_member(household_id, member.get("id"))
    return {
        "family": family
    }


@app.route("/household/<household_id>/member/<member_id>", methods=["DELETE"])
def single_family_member_handler(household_id, member_id):
    # Task 7
    FamilyService.remove_family_member(household_id, member_id)
    return {"status": "success"}


if __name__ == '__main__':
    app.run()
