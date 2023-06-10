#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    Type: MMv1     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_https_health_check
description:
- An HttpsHealthCheck resource. This resource defines a template for how individual
  VMs should be checked for health, via HTTPS.
short_description: Creates a GCP HttpsHealthCheck
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  check_interval_sec:
    description:
    - How often (in seconds) to send a health check. The default value is 5 seconds.
    required: false
    type: int
  description:
    description:
    - An optional description of this resource. Provide this property when you create
      the resource.
    required: false
    type: str
  healthy_threshold:
    description:
    - A so-far unhealthy instance will be marked healthy after this many consecutive
      successes. The default value is 2.
    required: false
    type: int
  host:
    description:
    - The value of the host header in the HTTPS health check request. If left empty
      (default value), the public IP on behalf of which this health check is performed
      will be used.
    required: false
    type: str
  name:
    description:
    - Name of the resource. Provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
    type: str
  port:
    description:
    - The TCP port number for the HTTPS health check request.
    - The default value is 443.
    required: false
    type: int
  request_path:
    description:
    - The request path of the HTTPS health check request.
    - The default value is /.
    required: false
    type: str
  timeout_sec:
    description:
    - How long (in seconds) to wait before claiming failure.
    - The default value is 5 seconds. It is invalid for timeoutSec to have greater
      value than checkIntervalSec.
    required: false
    type: int
    aliases:
    - timeout_seconds
  unhealthy_threshold:
    description:
    - A so-far healthy instance will be marked unhealthy after this many consecutive
      failures. The default value is 2.
    required: false
    type: int
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
    - accesstoken
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  access_token:
    description:
    - An OAuth2 access token if credential type is accesstoken.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
    elements: str
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/v1/httpsHealthChecks)'
- 'Adding Health Checks: U(https://cloud.google.com/compute/docs/load-balancing/health-checks#legacy_health_checks)'
- for authentication, you can set service_account_file using the C(GCP_SERVICE_ACCOUNT_FILE)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set access_token using the C(GCP_ACCESS_TOKEN)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a HTTPS health check
  google.cloud.gcp_compute_https_health_check:
    name: test_object
    healthy_threshold: 10
    port: 8080
    timeout_sec: 2
    unhealthy_threshold: 5
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
checkIntervalSec:
  description:
  - How often (in seconds) to send a health check. The default value is 5 seconds.
  returned: success
  type: int
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
description:
  description:
  - An optional description of this resource. Provide this property when you create
    the resource.
  returned: success
  type: str
healthyThreshold:
  description:
  - A so-far unhealthy instance will be marked healthy after this many consecutive
    successes. The default value is 2.
  returned: success
  type: int
host:
  description:
  - The value of the host header in the HTTPS health check request. If left empty
    (default value), the public IP on behalf of which this health check is performed
    will be used.
  returned: success
  type: str
id:
  description:
  - The unique identifier for the resource. This identifier is defined by the server.
  returned: success
  type: int
name:
  description:
  - Name of the resource. Provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
port:
  description:
  - The TCP port number for the HTTPS health check request.
  - The default value is 443.
  returned: success
  type: int
requestPath:
  description:
  - The request path of the HTTPS health check request.
  - The default value is /.
  returned: success
  type: str
timeoutSec:
  description:
  - How long (in seconds) to wait before claiming failure.
  - The default value is 5 seconds. It is invalid for timeoutSec to have greater value
    than checkIntervalSec.
  returned: success
  type: int
unhealthyThreshold:
  description:
  - A so-far healthy instance will be marked unhealthy after this many consecutive
    failures. The default value is 2.
  returned: success
  type: int
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            check_interval_sec=dict(type='int'),
            description=dict(type='str'),
            healthy_threshold=dict(type='int'),
            host=dict(type='str'),
            name=dict(required=True, type='str'),
            port=dict(type='int'),
            request_path=dict(type='str'),
            timeout_sec=dict(type='int', aliases=['timeout_seconds']),
            unhealthy_threshold=dict(type='int'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#httpsHealthCheck'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.put(link, resource_to_request(module)))


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#httpsHealthCheck',
        u'checkIntervalSec': module.params.get('check_interval_sec'),
        u'description': module.params.get('description'),
        u'healthyThreshold': module.params.get('healthy_threshold'),
        u'host': module.params.get('host'),
        u'name': module.params.get('name'),
        u'port': module.params.get('port'),
        u'requestPath': module.params.get('request_path'),
        u'timeoutSec': module.params.get('timeout_sec'),
        u'unhealthyThreshold': module.params.get('unhealthy_threshold'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/global/httpsHealthChecks/{name}".format(**module.params)


def collection(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/global/httpsHealthChecks".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'checkIntervalSec': response.get(u'checkIntervalSec'),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'healthyThreshold': response.get(u'healthyThreshold'),
        u'host': response.get(u'host'),
        u'id': response.get(u'id'),
        u'name': module.params.get('name'),
        u'port': response.get(u'port'),
        u'requestPath': response.get(u'requestPath'),
        u'timeoutSec': response.get(u'timeoutSec'),
        u'unhealthyThreshold': response.get(u'unhealthyThreshold'),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://compute.googleapis.com/compute/v1/projects/{project}/global/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#httpsHealthCheck')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


if __name__ == '__main__':
    main()
