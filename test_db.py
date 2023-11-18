import psycopg2

def select():
  conn = psycopg2.connect(
    host="localhost",
    database="users",
    user="postgres",
    password="gobank"
  )

  cur = conn.cursor()

  cur.execute("select * from user_data")
  
  users = cur.fetchall()
  print(users)

select()
def insert():
  conn = psycopg2.connect(
    host="localhost",
    database="users",
    user="postgres",
    password="gobank"
  )

  cur = conn.cursor()

  cur.execute("insert into user_data values(%s, %s, %s, %s)", (2, "hrushi", "hrushi", "hrushi@gmail.com"))
  
  conn.commit()

insert()
select()