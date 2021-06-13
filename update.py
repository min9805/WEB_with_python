#!python
print("Content-Type: text/html")
print()
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else :
    pageId = 'Welcome'
    description = 'Hello Web'
print('''
<!doctype html>
<html>
<head>
  <title>WEB1 - html</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href = "create.py">create</a>
  <form action="process_update.py" method="post">
      <p><input type="hidden" name="pageId" value="{form_default_title}"></p>
      <p><input type="text" name="title" value="{form_default_title}"></p>
      <p><textarea rows="4" name="description">{form_default_description}</textarea></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(
listStr=view.getList(),
form_default_title=pageId,
form_default_description=description))
