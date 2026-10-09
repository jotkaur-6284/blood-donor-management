from django.shortcuts import render
from .models import Donor, RegisterP,Donor

# Create your views here.
def IndexPage(request):
    return render(request, 'index.html')

def AboutPage(request):
    return render(request, 'about.html')

def BecameDonorPage(request):
    if request.method=="POST":
        name = request.POST.get('full_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        mail = request.POST.get('email')
        phone = request.POST.get('phone')
        blood_group = request.POST.get('blood_type')
        location=request.POST.get('loc')

        # Create a new Donor object and save it to the database
        Donor.objects.create(
            name=name,
            age=age,
            gender=gender,
            mail=mail,
            phone=phone,
            blood_group=blood_group,
            location=location
        )
    return render(request, 'became_donor.html')



def find_donor(request):
    donors = Donor.objects.none()
    searched = False

    if request.method == "POST":
        location = request.POST.get("loc", "").strip()
        blood_group = request.POST.get("blood_type", "").strip()

        searched = True

        donors = Donor.objects.filter(
            location__icontains=location,
            blood_group__iexact=blood_group
        )

    return render(request, "find_donor.html", {
        "donors": donors,
        "searched": searched,
    })
    
def RegisterPage(request):
    if request.method=="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            # Handle password mismatch
            return render(request, "register.html", {'error': 'Passwords do not match.'})
            

        RegisterP.objects.create(
            firstname=firstname, 
            lastname=lastname, 
            address=address, 
            email=email, 
            password=password,)
    return render(request, "register.html", {'message': 'Registration successful.'})

def LoginPage(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=RegisterP.objects.filter(
            email=email,
            password=password
        ).first()
        if user:
            return render(request, 'index.html', {'message': 'Login successful.'})
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password.'})
        
    return render(request, 'login.html')