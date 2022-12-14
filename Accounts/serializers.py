from .models import User,Student

def get_student_list(_class,section):
    if type(_class) is int:
        data = {}
        chunk = Student.objects.filter(_class=_class,section=section)
        for s in chunk:
            user = s.user
            data[user.username] = f"{user.first_name} {user.last_name}"
        return data
    raise ValueError("Class must be a number")