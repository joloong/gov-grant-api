from models import db


class MemberModel(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
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

    def __init__(self, name, gender, marital_status, occupation_type, annual_income, dob):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation_type = occupation_type
        self.annual_income = annual_income
        self.dob = dob

    def __repr__(self):
        return f"{self.id} {self.name}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "marital_status": self.marital_status,
            "occupation_type": self.occupation_type,
            "annual_income": self.annual_income,
            "dob": self.dob
        }
