select code_module, code_presentation, module_presentation_length
from courses
where module_presentation_length = (select min(module_presentation_length) from courses)
