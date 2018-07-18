import pycountry

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from ui.backend.forms import SignupForm, ProfileForm
from ui.utils import render_to_json


def get_states_info(country_code):
    """
    Gets subdivisions concerned information based on a chosen country.

    :param country_code string: pycountry alpha2 code for given country.
    :returns list of tuples: [(state_name, state_code), ...]
    """
    try:
        states = [
            (state.name, state.code) for state in pycountry.subdivisions.get(
                country_code=country_code
            )
        ]
    except KeyError:
        # Some states doesn't have any subdivisions
        states = []

    return states


def signup(request):
    """ Simple signup form. Creates new user and logs her into system. """

    if request.method == 'POST':
        form = SignupForm(request, data=request.POST)
        if form.is_valid():
            # Save a new user
            form.save_new_user()

            # Log her into the app.
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user and not user.is_anonymous():
                login(request, user)

            # Redirect to extended signup form
            return redirect('create_profile')
    else:
        form = SignupForm(request)

    return render(request, 'auth/signup.html', {'form': form})


@login_required
def create_profile(request):
    form = ProfileForm(instance=request.user.account)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.account)
        if form.is_valid():
            form.save()
            # All required fields filled -> setup complete for user.
            user = request.user
            user.is_signup_complete = True
            user.save()
            return redirect('charge_account')
        else:
            # Do not activate user but save all fields he filled.
            form.save_validated_fields()

    TOP_COUNTRIES = [
        ('United States', 'US'), ('Canada', 'CA'), ('United Kingdom', 'GB')
    ]
    OTHER_COUNTRIES = [
        (country.name, country.alpha2) for country in pycountry.countries
        if country.name not in TOP_COUNTRIES
    ]
    DEFAULT_STATES = get_states_info(form['country'].value() or 'US')

    context = {
        'countries': TOP_COUNTRIES + OTHER_COUNTRIES,
        'default_states': DEFAULT_STATES,
        'step': 'create_profile',
        'form': form,
    }

    return render(request, 'signup/create_profile.html', context)


@login_required
def charge_account(request):
    context = {'step': 'charge_account'}
    return render(request, 'signup/charge_account.html', context)


@login_required
def processing_payment(request):
    context = {'step': 'charge_account'}
    return render(request, 'signup/processing_payment.html', context)


@login_required
def setup_complete(request):
    context = {'step': 'setup_complete'}
    return render(request, 'signup/setup_complete.html', context)


@require_POST
@render_to_json()
def fetch_states(request):
    """
    :returns: json with states for country code given in POST request.
    """
    return {
        'states': get_states_info(
            request.POST.get('code')
        )
    }
