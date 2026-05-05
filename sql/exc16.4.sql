# how rich or poor men vs women
with num_males as ( select count(*) from studentinfo where gender = "M"),
num_females as (select count(*) from studentinfo where gender = "F"),
imd_g_m as (select imd_band, gender, round(count(*) / (select * from num_males) * 100, 2) as percentage
from studentinfo
group by imd_band, gender
having gender = "M"),
imd_g_f as (select imd_band, gender, round(count(*) / (select * from num_females) * 100, 2) as percentage
from studentinfo
group by imd_band, gender
having gender = "F")


select *
from imd_g_m
inner join imd_g_f using(imd_band)