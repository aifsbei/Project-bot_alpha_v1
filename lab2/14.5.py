import re

match = re.findall(r'=\w+&?', input())
key = input()
if key == 'text':
    print(str(match[0]).lstrip('=').rstrip('&')) if match else 'Not Found'
elif key == 'source':
    print(str(match[1]).lstrip('=').rstrip('&')) if match else 'Not Found'