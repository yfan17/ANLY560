import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

db_cnx = db.cursor()

db_cnx.execute(
    """
        SELECT DISTINCT f.title, f.description, a.first_name, a.last_name
        FROM sakila.film f left join sakila.film_actor fa on f.film_id=fa.film_id
        LEFT JOIN sakila.actor a on fa.actor_id=a.actor_id
        WHERE f.title like 'ZO%' 
        ORDER BY fa.actor_id asc;
    """
)

results = db_cnx.fetchall()

for row in results:
  print(row)
