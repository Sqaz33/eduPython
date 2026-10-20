select * 
from orders 
where amount > (
  select avg(amount) from orders
);

select * 
from users 
where id in (
  select user_id 
  from orders
  where status = 'cancelled'
);

select *
from users as u
where exists (
  select 1
  from orders as o
  where o.user_id = u.id 
    and o.satus = 'cancelled'
)