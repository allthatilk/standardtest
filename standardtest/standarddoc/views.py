from django.shortcuts import render

def iati_activities(request):
    """Render the iati_activities page."""
    return render(request, 'iati-activities.html', {})
