# how many m/f succeeded in their studies relative to their population
create or replace view genderbender as (with w as (select gender, round(sum(final_result in ("Withdrawn")) / count(*) * 100, 2) as withdrawn
from studentinfo
group by gender) ,
f as (select gender, round(sum(final_result in ("Fail")) / count(*) * 100, 2) as failed
from studentinfo
group by gender),

p as (select gender, round(sum(final_result in ("Pass")) / count(*) * 100, 2) as passed
from studentinfo
group by gender),


d as (select gender, round(sum(final_result in ("Distinction")) / count(*) * 100, 2) as distinction
from studentinfo
group by gender),

a as (select gender, count(*) as num_students
from studentinfo
group by gender)

select w.gender, withdrawn, failed, passed, distinction, num_students, round(num_students * (passed) / 100) as num_passed,
round(num_students * distinction / 100) as num_distinct,
round(num_students * failed / 100) as num_failed, round(num_students * withdrawn / 100) as num_withdrawn
from w
inner join (f, p, d, a) on w.gender = f.gender and w.gender = p.gender and w.gender = d.gender and w.gender = a.gender);

select *
from genderbender
s