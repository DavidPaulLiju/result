from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        employee_id = request.POST.get("Employee_ID")  # Update variable name to match form field
        api_url = f'http://127.0.0.1:8000/details/{employee_id}/'  # Update API endpoint URL
        response = requests.get(api_url)
        employee_data = response.json()  # Update variable name to reflect employee data
        if response.status_code == 200:
            return render(request, 'results.html', {'employee_data': employee_data})  # Update variable name in template context
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch employee details. Check Again!'})  # Update error message
    
    return render(request, 'index.html')
