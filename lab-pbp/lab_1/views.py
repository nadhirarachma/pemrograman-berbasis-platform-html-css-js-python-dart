from lab_1.models import Friend
from django.shortcuts import render
from datetime import datetime, date

mhs_name = 'Nadhira Rachma Salsabila Anandra'  # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(2002, 8, 8)  # TODO Implement this, format (Year, Month, Date)
npm = 2006484974  # TODO Implement this


def index(request):
    response = {'name': mhs_name,
                'age': calculate_age(birth_date.year),
                'npm': npm}
    return render(request, 'index_lab1.html', response)


def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0


def friend_list(request):
    friends = Friend.objects.all()  # TODO Implement this
    response = {'friends': friends}
    return render(request, 'friend_list_lab1.html', response)
