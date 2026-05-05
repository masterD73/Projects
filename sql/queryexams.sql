select id_assessment, id_student, weight * score / 100
from studentassessment
inner join assessments using(id_assessment);


