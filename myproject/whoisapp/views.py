# whoisapp/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .whoisproject import get_whois_info
import csv

def index(request):
    return render(request, 'whoisapp/index.html')

def whois_lookup(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            reader = csv.reader(file.read().decode('utf-8').splitlines())
            ips = [row[0] for row in reader]
            results = {}
            for ip in ips:
                ip, whois_info = get_whois_info(ip)
                results[ip] = whois_info
            return JsonResponse(results)
        else:
            return JsonResponse({'error': 'No file uploaded'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
