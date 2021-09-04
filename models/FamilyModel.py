from models import db


class FamilyModel(db.Model):
    __tablename__ = 'families'

    postal_code = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.Integer, nullable=False)
    member_id = db.Column(db.String(), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint(postal_code, level, unit, member_id),
        db.ForeignKeyConstraint(
            ['postal_code', 'level', 'unit'],
            ['households.postal_code', 'households.level', 'households.unit']
        ),
        db.ForeignKeyConstraint(
            ['member_id'], ['members.id']
        )
    )

    def __init__(self, postal_code, level, unit, member_id):
        self.postal_code = postal_code
        self.level = level
        self.unit = unit
        self.member_id = member_id

    def __repr__(self):
        return "{member_id} #{level}-{unit} S{postal_code}".format(member_id=self.member_id, level=self.level, unit=self.unit, postal_code=self.postal_code)
