from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


class Register:

    def step1(request):
        now = timezone.now()
        year = int(now.strftime("%Y")) - 12
        year_list = []
        count = 0
        for i in range(year):
            if count == 81:
                break
            year_list.append(year - count)
            count += 1

        return render(request, 'register-1.html', {'month': [i for i in range(1, 32)],
                                                'year': year_list})

    @csrf_exempt
    def step2(request):
        habbelix = {
            "gender": request.POST.get('gender'),
            "day": request.POST.get('day'),
            "month": request.POST.get('month'),
            "year": request.POST.get('year')
        }

        return render(request, 'register-2.html', {'data': habbelix})
    
    @csrf_exempt
    def step3(request):
        print(request.POST)

        habbelix = {
            "username": request.POST.get('username'),
            "email": request.POST.get('email'),
        }

        for userdata in request.POST['register-userdata']:
            habbelix.update = {
                "gender": userdata['gender'],
                "day": userdata['day'],
                "month": userdata['month'],
                "year": userdata['year'],
            }   
        print(habbelix)
        return render(request, 'register-3.html', {})