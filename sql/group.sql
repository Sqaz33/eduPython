select 
  user_id,
  sum(amount) as total_amount -- без групировки сумма всех строк
from orders
where status = 'paid'
group by user_id
having sum(amount) >= 100
order by total_amount desc;

select 
  u.id as user_id,
  u.name as name,
  count(o.id) as orders_count,
  coalesce(sum(o.amount), 0) as total_amount
from users as u
left join orders as o on u.id = o.user_id
group by u.id, u.name
order by total_amount desc, user_id asc;


select 
  u.name as name, 
  count(o.id) as orders_count,
  coalesce(sum(o.amount), 0) as total_amount
from users as u
left join orders as o on u.id = o.user_id
group by u.id
order by total_amount desc, orders_count asc;







