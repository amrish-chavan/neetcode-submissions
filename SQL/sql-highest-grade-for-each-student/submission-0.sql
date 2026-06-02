Select Distinct on (student_id) 
    student_id, 
    exam_id,
    score
from exam_results
order by student_id, score Desc, exam_id;