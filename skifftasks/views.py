import json

from django.contrib import auth
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django_browserid.auth import get_audience
from django_browserid.forms import BrowserIDForm


@require_POST
def browserid_verify(request):
    """
    Accept a posted BrowserID assertion and return user details if login succeeds.
    """
    assertion = request.raw_post_data
    user = auth.authenticate(assertion=assertion,
                             audience=get_audience(request))
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponse(json.dumps(
                    {
                    'user' : user.profile.as_dict(request_user=user),
                    'sessionid' : request.session.session_key
                    }
                ))
    return HttpResponse(json.dumps(
                {
                'error' : "Unauthorized",
                'status' : 401
                }
            ), status_code=401)

        
        
