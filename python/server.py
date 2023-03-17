from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

engine = create_engine('sqlite:///calendar.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    start = Column(String)
    end = Column(String)
    title = Column(String)
    class_ = Column(String)

    def to_dict(self):
        return {'id': self.id, 'start': str(self.start), 'end': str(self.end), 'title': self.title, 'class': self.class_}

Base.metadata.create_all(engine)

@app.route('/calendarAPI/getAll')
def get_all_events():
    session = Session()
    events = session.query(Event).all()
    event_dicts = [event.to_dict() for event in events]
    session.close()
    return jsonify(event_dicts)

@app.route('/calendarAPI/addEvent', methods=['POST'])
def add_event():
    session = Session()
    print(request.json)
    start = request.json['start']
    end = request.json['end']
    title = request.json['title']
    try:
        class_ = request.json['class']
    except:
        class_ = "default"
        

    new_event = Event(start=start, end=end, title=title, class_=class_)
    session.add(new_event)
    session.commit()

    session.close()
    return "OK"
    # return None

if __name__ == '__main__':
    app.run(debug=True)
