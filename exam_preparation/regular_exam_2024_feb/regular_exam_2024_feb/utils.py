from regular_exam_2024_feb.car.models import Car
from regular_exam_2024_feb.profile_car.models import Profile


def get_user_obj():
    return Profile.objects.first()


def get_car_obj():
    return Car.objects.all()
