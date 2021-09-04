from models import db


class FamilyModel(db.Model):
    __tablename__ = 'families'

    household_id = db.Column(db.Integer, nullable=False)
    member_id = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint(household_id, member_id),
        db.ForeignKeyConstraint(
            ['household_id'],
            ['households.id']
        ),
        db.ForeignKeyConstraint(
            ['member_id'], ['members.id']
        )
    )

    def __init__(self, household_id, member_id):
        self.household_id = household_id
        self.member_id = member_id

    def __repr__(self):
        return f"{self.member_id} @ {self.household_id}"

    def serialize(self):
        return {
            "household_id": self.household_id,
            "member_id": self.member_id
        }
