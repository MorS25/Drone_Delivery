import model
import csv

def load_ducks(postgres_session):
    with open("seed_data/u.duck") as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            id, name, pic, price, bio = row
            id = int(id)
            u = model.Duck(id=id,
                            name=name,
                            pic=pic,
                            price=price,
                            bio=bio)
            postgres_session.add(u)
            postgres_session.commit()

def main(postgres_session):
    # You'll call the load_* functions with the session as an argument
    load_ducks(postgres_session)

if __name__ == "__main__":
    s = model.postgres_session
    main(s)