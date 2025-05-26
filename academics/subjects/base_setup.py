from academics.classes.models import LevelChoices

from .models import Subject, Category, Paper
from .setup_data import O_level_subjects, A_level_subjects


def setup_subject_group(group:dict, level:str):
    """
    Setup base subjects for.
    """
    for subject_code, subject_data in group.items():
        # create subject if it doesn't exist or update it if it does
        subject = Subject.objects.update_or_create(
            code=subject_code,
            defaults={
                "name": subject_data["subject"],
                "abbreviation": subject_data["abbreviation"],
                "category": Category.objects.get_or_create(name=subject_data["category"])[0],
                "level": level,
                "is_base": True,
            }
        )
        
        for paper_data in subject_data["papers"]:
            
            Paper.objects.update_or_create(
                subject=subject[0],
                number=paper_data["number"],
                defaults={
                    # use the subject name if it differs from the paper name, since the model will be able to generate the "Paper 2" name automatically
                    "name": paper_data["name"] if paper_data["name"] != subject_data["subject"] else None,
                }
            )
            

def setup_base_subjects():
    """
    Setup base subjects for O and A levels.
    """
    setup_subject_group(O_level_subjects, LevelChoices.ORDINARY)
    setup_subject_group(A_level_subjects, LevelChoices.ADVANCED)