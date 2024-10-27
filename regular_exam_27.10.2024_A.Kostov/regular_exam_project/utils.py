from regular_exam_project.author.models import Author


def get_user_obj():
    return Author.objects.first()
