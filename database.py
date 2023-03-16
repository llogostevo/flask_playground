from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DBCONNECTIONSTRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * FROM topic"))
  result_all = result.all()
  print(result_all)

  column_names = result.keys()

  topic = []
  for row in result.all():
    topic.append(dict(zip(column_names, row)))

  print(topic[0])
