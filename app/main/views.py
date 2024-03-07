from django.shortcuts import render
from authentication.decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request=request,
                  template_name="main/dashboard.html",
                  context={
                  })