create table users(id integer primary key, name text not null, age integer);

insert into users (name, age) values ('Anna1', 21), ('Anna2', 22);

create table orders(
  id integer primary key, 
  user_id integer not null, 
  amount integer not null,
  status text not null,
  foreign key (user_id) references users(id)
);

insert into orders (user_id, amount, status)
values 
  (1, 200, 'paid'), 
  (1, 100, 'pending'), 
  (2, 100, 'paid');

-- только совпавшие пары
select u.name, o.id as order_id, o.amount
from users as u
inner join orders as o on u.id = o.user_id
order by u.id, o.id;

SELECT u.name, o.id AS order_id, o.amount
FROM users AS u
LEFT JOIN orders AS o ON u.id = o.user_id
ORDER BY u.id, o.id;

-- и значения из левой таблицы без пары
SELECT u.id, u.name 
FROM users AS u
LEFT JOIN orders AS o ON u.id = o.user_id
WHERE o.user_id is NULL
ORDER BY u.id desc;

select 
  u.id, 
  u.name,
  count(*) as cancelled_orders  
from orders as o 
inner join users as u on o.user_id = u.id
where o.status = 'cancelled'
group by u.id;

-- | JOIN | Что сохраняет |
-- |---|---|
-- | `INNER` | Совпавшие пары |
-- | `LEFT` | Совпавшие пары + несовпавшие строки слева |
-- | `RIGHT` | Совпавшие пары + несовпавшие строки справа |
-- | `FULL OUTER` | Совпавшие пары + несовпавшие строки с обеих сторон |