# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import functools
import json

from django.http import HttpResponse
from django.views import generic

from openstack_dashboard.api.rest import utils as rest_utils
from openstack_dashboard.api.rest.utils import JSONResponse

import horizon_web_ui.freezer_ui.api.api as freezer_api


# https://github.com/tornadoweb/tornado/issues/1009
# http://haacked.com/archive/2008/11/20/anatomy-of-a-subtle-json-vulnerability.aspx/
def prevent_json_hijacking(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        response = function(*args, **kwargs)
        if isinstance(response, JSONResponse) and response.content:
            response.content = ")]}',\n" + response.content
        return response

    return wrapper


class Clients(generic.View):
    """API for nova limits."""

    @prevent_json_hijacking
    @rest_utils.ajax()
    def get(self, request):
        """Get all registered freezer clients"""

        # we don't have a "get all clients" api (probably for good reason) so
        # we need to resort to getting a very high number.
        clients = freezer_api.client_list_json(request)
        clients = json.dumps(clients)
        return HttpResponse(clients,
                            content_type="application/json")


class Actions(generic.View):
    """API for clients"""

    @prevent_json_hijacking
    @rest_utils.ajax()
    def get(self, request):
        """Get all registered freezer actions"""
        actions = freezer_api.action_list_json(request)
        actions = json.dumps(actions)
        return HttpResponse(actions,
                            content_type="application/json")


class ActionsInJob(generic.View):
    """API for actions in a job"""

    @prevent_json_hijacking
    @rest_utils.ajax()
    def get(self, request, job_id=None):
        """Get all registered freezer actions"""
        actions = freezer_api.actions_in_job_json(request, job_id)
        actions = json.dumps(actions)
        return HttpResponse(actions,
                            content_type="application/json")
