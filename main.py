import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale

DNS = "postgresql://postgres:postgres@localhost:5432/postgres"
engine = sqlalchemy.create_engine(DNS)

create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()

pub1 = Publisher(name='Publisher1')
pub2 = Publisher(name='Publisher2')
book1 = Book(title='Book1', publisher=pub1)
shop1 = Shop(name='Shop1')
stock1 = Stock(book=book1, shop=shop1, count=3)
sale1 = Sale(price=123.45, date_sale='20200101', stock=stock1, count=2)

session.add_all([pub1, pub2, book1, shop1, stock1, sale1])
session.commit()
r = input('Введите имя или идентификатор издателя:')
if r.isdigit():
    for b in session.query(Publisher).filter(Publisher.id==int(r)):
        print(b)
else:
    for b in session.query(Publisher).filter(Publisher.name.like(f'%{r}%')):
        print(b)


session.close()