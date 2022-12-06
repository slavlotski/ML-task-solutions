select brand, 
       count(sku_type) as count_sku 
from sku_dict_another_one
where brand is not null
group by brand
order by count(sku_type) desc
limit 10