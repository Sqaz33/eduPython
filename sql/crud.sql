create table users(id integer primary key, name text not null, age integer);

insert into users (name, age) values ('Anna1', 21), ('Anna2', 22);

-- select
select name, age from users where age > 20 order by age desc, id asc limit 2;
select distinct age from users; --убрать повторы в результате
select * from users where age between 18 and 25; --убрать повторы в результате
select * from users where age in (18, 25); --убрать повторы в результате
select * from users where (age >= 18 and age <= 25) or name != 'Anton'; --убрать повторы в результате
select * from users where age is not NULL;

--update, delete
update users set age = 10 where age = 9; 
update users set age = 10; -- обновить все строки 
update users set age = 10, name = 'Anna1'; 
update users set age = age + 1; -- на основе текущих значений
update users set age = null; -- на основе текущих значений

delete from users where id = 2;
delete from users; -- удалить все из таблицы