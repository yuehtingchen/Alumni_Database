from models import User, School, db
db.create_all()
s = School(longitude=24.5, latitude=26.5, name="Columbia", city="New York", country="USA")
u = User(name="alice", degree="BA in CS", grad_year=2024, email="emample@example.com", linkedIn="", school_name="Columbia")

db.session.add(s)
db.session.add(u)
db.session.commit()


