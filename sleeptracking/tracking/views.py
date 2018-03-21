from django.shortcuts import render
from tracking.models import Sleep

def index(request):
	return render(request, 'index.html')

def tracking_data(request):
	data = []
	night_sleep1 = Sleep(1, 2.5, 5.5, 40, 60, '2018-03-16')
	night_sleep2 = Sleep(2, 4.5, 8.5, 57, 43, '2018-03-17')
	night_sleep3 = Sleep(3, 5, 9.2, 67, 33, '2018-03-18')
	night_sleep4 = Sleep(4, 3.75, 6.6, 50, 50, '2018-03-19')
	data.append(night_sleep1)
	data.append(night_sleep2)
	data.append(night_sleep3)
	data.append(night_sleep4)

	return render(request, 'data.html', {"sleeps" : data})


def tracking_details(request, id):
	night_sleep = Sleep()

	if(id == 1):
		night_sleep = Sleep(id, 3.75, 7.5, 57, 43, '2018-03-21')

	return render(request, 'tracking.html', {"sleep" : night_sleep})