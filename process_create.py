#!python

import cgi

form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value
description = description.replace('<','&lt')
description = description.replace('>','&gt')

opened_file = open('data/'+title, 'w')
opened_file.write(description)

print("Location: index.py?id="+title)
print()
