#!/usr/bin/python3.10
"""
this module should open the Postman Collection json and parse it and return the cURL
"""
import json


def postman_parser():
    output = {}
    curls = []
    with open("data/IBS-NG Copy.postman_collection.json", "rb") as file:
        f = json.load(file)
        items = f.get("item")
        variables = f.get("variable")
        output['names'] = [item['name'] for item in items]
        output['request'] = [item['request'] for item in items]

        for out in output['request']:
            key = out['url']['raw'].split("/")[0]
            for variable in variables:
                if key[2:-2] == variable['key']:
                    url = out['url']['raw'].replace(key, variable['value'])
                    c = f"curl -X {out['method']} \"{url}\" "
                else:
                    c = f"curl -X {out['method']} \"{out['url']['raw']}\" "
            for header in out['header']:
                header_key = header.get('key')
                header_value = header.get('value')
                headers = f"-H \"{header_key}: {header_value}\" "
                c = c + headers

            if out['method'] != 'GET':
                body = out.get('body', "")
                raw = body.get('raw', '') if body else '{}'
                c = c + f"-d \"{raw}\" "
            curls.append(c)
            print(c)


if __name__ == "__main__":
    postman_parser()
