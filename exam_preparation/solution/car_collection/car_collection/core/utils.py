from car_collection.auth_app.models import Profile


def get_first_profile():
    return Profile.objects.first()

