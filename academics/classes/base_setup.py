from . models import Class, LevelChoices

def setup_classes():
    for num in range(1, 7):
        level = LevelChoices.ORDINARY if num < 5 else LevelChoices.ADVANCED
        
        Class.objects.update_or_create(
            level=level,
            number=str(num),
            defaults={'level': level, 'number': str(num)}
        )