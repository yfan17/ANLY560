SELECT DISTINCT f.title, f.description, a.first_name, a.last_name
FROM sakila.film f left join sakila.film_actor fa on f.film_id=fa.film_id
left join sakila.actor a on fa.actor_id=a.actor_id
where f.title like 'ZO%' 
ORDER BY fa.actor_id asc;

