with date_counts as (select date_unregistration, count(*) as date_count
from studentRegistration
where date_unregistration is not null
group by date_unregistration
order by date_count DESC)

select round((count(*) * sum(date_unregistration * date_count) - sum(date_unregistration) * sum(date_count)) / 
        (sqrt(count(*) * sum(date_unregistration * date_unregistration) - sum(date_unregistration) * sum(date_unregistration)) * sqrt(count(*) * sum(date_count * date_count) - sum(date_count) * sum(date_count))), 2) 
        AS coeff_credits_score
    from date_counts as d