from models import db


class MemberModel(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    marital_status = db.Column(db.String(), nullable=False)
    occupation_type = db.Column(db.String(), nullable=False)
    annual_income = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.Date, nullable=False)

    __table_args__ = (
        db.CheckConstraint(
            "gender in ('male', 'female')"
        ),
        db.CheckConstraint(
            "marital_status in ('single', 'married', 'divorced')"
        ),
        db.CheckConstraint(
            "occupation_type in ('employed', 'unemployed', 'student')"
        ),
        db.CheckConstraint(
            "annual_income >= 0"
        ),
    )

    def __init__(self, id, name, gender, marital_status, occupation_type, annual_income, dob):
        self.id = id
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation_type = occupation_type
        self.annual_income = annual_income
        self.dob = dob

    def __repr__(self):
        return "{id} {name}".format(id=self.id, name=self.name)
