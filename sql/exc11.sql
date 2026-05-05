with weight_stats as (select weight, round(avg(score), 2) as avg_score
from assessments
inner join studentassessment
using (id_assessment)
group by weight
order by avg_score, weight)

select distinct round((count(*) * sum(w.weight * avg_score) - sum(w.weight) * sum(avg_score)) / 
        (sqrt(count(*) * sum(w.weight * w.weight) - sum(w.weight) * sum(w.weight)) * sqrt(count(*) * sum(avg_score * avg_score) - sum(avg_score) * sum(avg_score))), 2) 
        AS coeff_weight_score
    from weight_stats as w