select  day, 
        count(user_id) as dau 
from (select distinct toDate(timestamp) as day, user_id from default.churn_submits)
group by day