import requests
import json

from django.conf import settings
from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView
from .models import Vendor
from rest_framework import serializers

from .serializers import VendorSerializer


class VendorList(ListView):
    """Fetch the Data from Database and Show it in the FrontEnd"""
    model = Vendor


def Index(request):
    """Call the `VendorFetch` and return to Vendor List"""
    VendorFetch()
    return redirect(reverse("vendorlist"))

"""
Note 
1> I have not configured the Django to auto renew the access token an dits just a configurable
as the assignment was just to fetch and display.
2> There is Exception handled generically and in production quality code we can handle in details
3> Logging not added as it was a demo code
4> security and other performance stuff can be added but just its a throwaway code hence not yet added
"""
def VendorFetch():
    """Fetch the data from the API Source , Validate it and store in the Database"""
    try:
        data = {"grant_type": settings.GRANT_TYPE}
        response = requests.post(settings.OAUTH_TOKEN_URL, data=data, verify=False, allow_redirects=False,
                                 auth=(settings.OAUTH_CLIENT_ID, settings.OAUTH_CLIENT_SECRET))

        tokens = json.loads(response.text)
        api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
        api_call_response = requests.get(settings.OAUTH_VENDOR_LIST_URL, headers=api_call_headers, verify=False)
        json_fields = json.loads(api_call_response.text)
        vendor_data_serialize = VendorSerializer(data=json_fields, many=True)
        if (vendor_data_serialize.is_valid()):  # Validate
            vendor_data_serialize.save()
        else:
            raise serializers.ValidationError(vendor_data_serialize.errors)
    except Exception as e:
        # Either Log or print the message and continue dont break
        print("Canoot Import Data Exception Raised => {}".format(e))

