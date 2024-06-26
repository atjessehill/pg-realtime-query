import random
import factory.random
import sqlalchemy
from faker import Faker
from faker.providers import internet
from datetime import datetime

from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker

from models import Region, House, Faction, Warrior
from fantasy_examples import region_data, faction_data, house_data, warriors

fake = Faker(internet)
seed = '2024JUN24'

fake.seed_instance(seed=seed)
factory.random.reseed_random(seed)
random.seed(seed)

if __name__ == "__main__":
    connection_url = engine.URL.create(
        drivername='postgresql+psycopg',
        username='postgres',
        password='password',
        host='localhost',
        database='postgres'
    )

    db_engine = sqlalchemy.create_engine(connection_url)

    session_factory = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    session = session_factory()

    date_now = datetime.now()

    # insert regions

    house_ids = []
    for region, faction, house in zip(region_data, faction_data, house_data):
        r = Region(
            code=region[0],
            name=region[1],
            desc=region[2]
        )
        f = Faction(
            code=faction[0],
            name=faction[1],
            desc=faction[2]
        )
        session.add_all([r, f])
        session.flush()

        h = House(
            region_id=r.id,
            faction_id=f.id,
            code=house[0],
            name=house[1],
            desc=house[2]
        )
        session.add(h)
        session.flush()

        house_ids.append(h.id)

    for warrior in warriors:

        w = Warrior(
            **warrior
        )
        w.house_id = random.choice(house_ids)
        session.add(w)

    session.commit()
