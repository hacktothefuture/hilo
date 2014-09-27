import web

web.config.debug = False

urls = (
    '/', 'index',

    # GETs
    '/products/(\d+)/gettoppros', 'gettoppros',
    '/products/(\d+)/gettoppros', 'gettopcons'
    '/products/(\d+)/getpros', 'getpros'
    '/products/(\d+)/getcons', 'getcons'

    # POSTs
    '/products/(\d+)/addpro_message=(\w+)', 'addpro',
    '/products/(\d+)/addcon_message=(\w+)', 'addcon',
    '/products/(\d+)/voteup_proconid=(\d+)', 'voteup'
    '/products/(\d+)/votedown_proconid=(\d+)', 'votedown'

class index:
    def GET(self):
        render = web.template.render('./')    
        return render.what(id)

# GETs

class gettoppros:
    def GET(self, id):
        return getTopPros(id)

class gettopcons:
    def GET(self, id):
        return getTopCons(id)

class getpros:
    def GET(self, id):
        return getPros(id)

class getcons:
    def GET(self, id):
        return getCons(id)

# POSTs

class addpro:
    def POST(self, id, message):
        addPro(id, message)
class addcon:
    def POST(self, id, message):
        addCon(id, message)

class voteup:
    def POST(self, id, message):
        voteUp(id, message)

class votedown:
    def POST(self, id, message):
        voteDown(id, message)


if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()