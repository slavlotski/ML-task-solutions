select sku_type, 
       count(distinct vendor) as count_vendor 
from sku_dict_another_one
group by sku_type
order by count(distinct vendor) desc
limit 10