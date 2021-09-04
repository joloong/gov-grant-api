from models import db


class HouseholdModel(db.Model):
    __tablename__ = 'households'

    postal_code = db.Column(db.Integer)
    level = db.Column(db.Integer)
    unit = db.Column(db.Integer)
    housing_type = db.Column(db.String(), unique=True)

    __table_args__ = (
        db.PrimaryKeyConstraint(postal_code, level, unit),
        db.CheckConstraint(
            "level >= 0 and level <= 999999"
        ),
        db.CheckConstraint(
            "housing_type in ('HDB', 'Condominium', 'Landed')"
        ),
    )

    def __init__(self, postal_code, level, unit, housing_type):
        self.postal_code = postal_code
        self.level = level
        self.unit = unit
        self.housing_type = housing_type

    def __repr__(self):
        return "{housing_type} #{level}-{unit} S{postal_code}".format(
            housing_type=self.housing_type, level=self.level, unit=self.unit, postal_code=self.postal_code)
