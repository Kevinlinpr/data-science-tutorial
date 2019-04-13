import psycopg2

connection=psycopg2.connect(dbname="jcqppqbl",
                            user="jcqppqbl",
                            password="GW9HA7mPWfS7pANmpqmhnFhsJhIpuA18",
                            host="isilo.db.elephantsql.com",
                            port=5432)

create_qry = """CREATE TABLE IF NOT EXISTS users (
                  id integer NOT NULL,
                  username varchar NOT NULL,
                  role varchar NOT NULL,
                  PRIMARY KEY (id)
                );"""

# Get a cursor
cursor = connection.cursor()

# Create the table
cursor.execute(create_qry)