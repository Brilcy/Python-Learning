import base64
import requests
import json

requests.packages.urllib3.disable_warnings()


def kibana_check(tenant):
    url = 'https://github.paypal.com/api/v3/repos/SearchPlatform-R/scripts/contents/config/Monitoring/qa.json'
    d = requests.get(url, auth=('brilp', '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'))
    res_json = d.json()
    file_content = base64.b64decode(res_json['content']).decode()
    file_json = json.loads(file_content)
    kibana_endpoint = file_json["kibana"][tenant]["endpoints"]
    endpoints = kibana_endpoint.split(',')
    print(endpoints)

    for host in endpoints:
        status_url = f"https://{host}/api/status"
        # print(status_url)

        try:
            get_status = requests.get(status_url, verify=False)
            status_json = get_status.json()
            kibana_status = status_json["status"]["overall"]["state"]
            print(status_url, ":", kibana_status)
        except:
            print(status_url, ": Red")


kibana_check("test-results-qa")
