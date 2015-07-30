# Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.


def create_dict_action(**kwargs):
    """Create a dict only with values that exists so we avoid send keys with
    None values
    """
    return {k: v for k, v in kwargs.items() if v}


class SessionJob(object):
    """Create a session object """
    def __init__(self, job_id, session_id, client_id, status):
        self.job_id = job_id
        self.session_id = session_id
        self.client_id = client_id
        self.status = status
