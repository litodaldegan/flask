#!flask/bin/python
from microblog import app
app.run(debug=True, use_reloader=True)