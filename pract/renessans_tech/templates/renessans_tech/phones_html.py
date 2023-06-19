import json

with open('/Users/margaritausova/Documents/pract/phones_data.json') as f:
    templates = json.load(f)

with open('phones.html', 'a') as f:

    for i in templates:
        f.write("""    <h1>{link}</h1>
        """.format(link=templates[i]['item_name']))
    f.write("""</body>
    </html>""")




