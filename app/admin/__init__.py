from flask_admin import Admin, BaseView,expose


admin=Admin()
def config_admin(app):

    admin.init_app(app)
    app.admin=admin


class AdminView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin.html')
