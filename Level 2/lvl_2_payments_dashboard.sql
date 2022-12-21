select b.date as time, 
       b.mode as mode, 
       coalesce((a.confirmed_by_month * 100.0 /b.total_by_month),0)  as percents 
from 
        (select date_trunc('month',date)::date as date, mode, count(*) as confirmed_by_month
        from new_payments
        where status = 'Confirmed' and mode <> 'Не определено'
        group by date_trunc('month',date), mode) a 
right join
        (select date_trunc('month',date)::date as date, mode, count(*) as total_by_month
        from new_payments
        where mode <> 'Не определено'
        group by  date_trunc('month',date), mode) b on 
a.date = b.date and a.mode = b.mode
order by b.date, b.mode