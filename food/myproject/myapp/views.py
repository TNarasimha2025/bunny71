from django.shortcuts import render, get_object_or_404

from .models import bakerys
def bakerys_list(request):
    ob_lists = bakerys.objects.all()
    return render(request, 'bakerys_list.html', {'lists': ob_lists})

def bakerys_detail(request, pk):
    ob_lists = get_object_or_404(bakery, pk=pk)
    return render(request, 'list_detail.html', {'bakerys': ob_bakerys})

from .models import canteen
def canteen_list(request):
    ob_lists = canteen.objects.all()
    return render(request, 'canteen_list.html', {'lists': ob_lists})

def canteen_detail(request, pk):
    ob_lists = get_object_or_404(canteen, pk=pk)
    return render(request, 'list_detail.html', {'canteen': ob_canteen})

from .models import mess
def mess_list(request):
    ob_lists = mess.objects.all()
    return render(request, 'mess_list.html', {'lists': ob_lists})

def mess_detail(request, pk):
    ob_lists = get_object_or_404(canteen, pk=pk)
    return render(request, 'list_detail.html', {'mess': ob_mess})
# Create your views here.
