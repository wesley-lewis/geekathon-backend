import psycopg2

def get_cursor():
  conn = psycopg2.connect(
    host="localhost",
    database="users",
    user="postgres",
    password="gobank"
  )
  cur = conn.cursor();

  cur.execute("""CREATE table if not exists user_data(
            id serial PRIMARY KEY,
            username varchar(50) not null,
            password varchar(50) not null,
            email varchar(50) not null,
            created_at date DEFAULT CURRENT_TIMESTAMP 
            )""")

  print("DB Created succesfully")
  return cur, conn