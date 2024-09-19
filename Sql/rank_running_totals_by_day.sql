/* The data used for these scripts is found in 'sales.csv */

with running_totals as
(select product_id, sale_date, quantity,
sum(quantity) over(partition by product_id order by sale_date rows between unbounded preceding and current row)  as running_total
from sales)


select product_id, sale_date, quantity, running_total, rank() over(partition by sale_date order by running_total DESC) as Rank
from running_totals
order by sale_date, product_id

/*_____________________________________________________________________________________________________________________________*/

/* The query below is an extended version of the previous one that does not ignore products that didn't have sales on a given day */ 



with 
running_totals as
(select product_id, sale_date, quantity,
sum(quantity) over(partition by product_id order by sale_date rows between unbounded preceding and current row)  as running_total
from sales),

dates as (select distinct sale_date from sales),

prod_ids as (select distinct product_id from sales),

a as (select sale_date, product_id from dates cross join prod_ids),

b as
(select a.product_id, a.sale_date, isnull(quantity, 0) as quantity, 
case 
	when running_total is null then lag(running_total,1,0) over(partition by a.product_id order by a.sale_date)
	else running_total
end as running_total
from a left join running_totals r on a.sale_date = r.sale_date and a.product_id = r.product_id)

select product_id, sale_date, quantity, running_total, rank() over(partition by sale_date order by running_total DESC) as Rank
from b
order by sale_date, Rank