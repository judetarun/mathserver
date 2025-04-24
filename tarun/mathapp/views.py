
from django.shortcuts import render
def power(request):
    context={}
    context['power']="0"
    context['intensity_value']="0"
    context['resistance_value']="0"
    if request.method == 'POST':
        intensity_value = int(request.POST.get('intensity-input'))
        resistance_value = int(request.POST.get('resistance-input'))
        print('request=',request)
        print('intesity=',intensity_value)
        print('resistance=',resistance_value)
        power = (intensity_value ** 2)*resistance_value
        context['power']=power
        context['intensity_value']=intensity_value
        context['resistance_value']=resistance_value
        print('output=',power)
        return render (request, 'mathapp/math.html', {'output':power})
    return render(request,'mathapp/math.html',context)