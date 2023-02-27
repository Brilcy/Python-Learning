import base64
import requests
import json
import sys


def kibana_check(tenant):
    url = 'https://github.paypal.com/api/v3/repos/SearchPlatform-R/scripts/contents/config/Monitoring/slc.json'
    res = requests.get(url, auth=('brilp', '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'))
    res_json = res.json()
    file_content = base64.b64decode(res_json['content']).decode()
    file_json = json.loads(file_content)
    kibana_endpoint = file_json["kibana"][tenant]["endpoints"]
    secured = file_json["kibana"][tenant]
    is_secured = secured.get("secure", "not_found")
    endpoints = kibana_endpoint.split(',')
#    print(endpoints)

    for host in endpoints:
        if is_secured == True:

            status = f"https://searchservadmin:searchservadmin@{host}/api/status"
#            status_url = status.format(host)
        else:
            status = f"http://{host}/api/status"
#            status_url = status.format(host)

        try:
            response = requests.get(status_url, verify=False)
            response_json = response.json()
            kibana_status = response_json["status"]["overall"]["state"]
            print(status_url, ":", kibana_status)
        except:
            print(status_url, ": Red")
 #       print(response_json)

#       print(status_url)


tenant = sys.argv[1]
kibana_check(tenant)
