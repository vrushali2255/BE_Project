import os, os.path
import cherrypy
import json
class Welcomepage(object):
    @cherrypy.expose
    def index(self):
        return '''<html>
<head>
<style>
body {
  background-color:pink;
}
</style>
</head>
<body>
<h1>
<p style="color:red">MOVIE RECCOMENDATION</p>
</h1>
            <form action="Recsys" method="GET">
            Enter viewer_id:
            <input type="text" name="viewer_id" /><br>
            <input type="submit" />
            </form>
            </htm>'''
        
    @cherrypy.expose
    def Recsys(self, viewer_id):  
        if viewer_id:
            rec = recommend(viewer_id, data_sparse, user_vecs, item_vecs, item_lookup)
            return json.dumps(rec)
         
        else:
            if viewer_id is None:
                # No name was specified
                return 'Please enter name <a href="./">here</a>.'
            else:
                return 'enter user name first <a href="./">here</a>.'

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(Welcomepage(), '/', conf)
