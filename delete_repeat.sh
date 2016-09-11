delete from douban_movie where id not in(select * from (select min(id) from douban_movie group by name) as tmp);-
