#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
            html = response.read()
            print('Body response:')
            print('\t- type: {}'.format(type(html)))
            print('\t- content: {}'.format(html))
            print('\t- utf8 content: {}'.format(html.decode("utf-8")))
    except urllib.error.URLError as e:
        print('Error: {}'.format(e))
