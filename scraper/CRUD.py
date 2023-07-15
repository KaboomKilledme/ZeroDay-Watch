from datetime import datetime
from sqlalchemy import  Table, MetaData
from Database import session, engine, Source

created_at = datetime.now()
updated_at = datetime.now()

metadata = MetaData()
metadata.reflect(bind=engine, views=True)


def addSource(source):
    foundSource = findSource(source['title'])
    if foundSource is None:
        newSource = Source(title=source['title'], type=source['type'], content=source['content'],
        link=source['link'], created_at=created_at, updated_at=updated_at)

        session.add(newSource)
        session.commit()
    else:
        raise RuntimeError('Record Already Exists')

def getAllSources():
    allAllSources = Table('sources', metadata, autoload=True)
    results = session.query(allAllSources).all()
    return results

def findSource(SourceTitle):
    foundSource = session.query(Source).filter(Source.title == SourceTitle).first()
    return foundSource

def getSources(type):
    results = session.query(Source).filter(Source.type == type).all()
    return results