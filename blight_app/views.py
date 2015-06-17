from django.shortcuts import render
from blight_app.forms import AbndSiteForm
from blight_app.models import AbndSite
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#TODO: permitir View solo si el usuario esta autenticado
@login_required
def add_abandoned(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = AbndSiteForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new property to the database.
            #form.save(commit=True)
            abn = form.save(commit=False)

            #TODO: verificar que se haya grabado el picture uploaded
            if 'picture' in request.FILES:
                abn.picture = request.FILES[abn.catastro]
            
            print abn
            abn.save()

            return render(request, 'mvp_app/home.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = AbndSiteForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'blight/add_abandoned.html', {'form': form})


def suggest(request, catastro):
    try:
        propiedad = AbndSite.objects.get(catastro=catastro)
        propiedad.shortname = propiedad.catastro.replace('-','')
        #TODO: si se crea, necesita la longitud y latitud
        #o utilizar get_object_or_404 from django.shortcuts 
        #propiedad = AbndSite.objects.get_or_create(catastro=catastro)
    except AbndSite.DoesNotExist:
        #TODO: redireccionar al home...no deberia ir a 404 si se utiliza get_or_create
        raise Http404
    return render(request, 'blight/detail.html', {'propiedad': propiedad})



def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'blight/login.html', {})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')