# routers.py

class ExternalRouter:
    """
    يوجه العمليات على نموذج User (الموجود في قاعدة SQL Server) إلى قاعدة 'external'
    بينما يترك باقي التطبيقات تستخدم 'default'
    """
    route_app_labels = {'core','accounts', 'hotels', 'rooms','tours','attractions'}  # عدل هذا لاسم التطبيق الذي يحتوي على نموذج User

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'external'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'external'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'external'
        return db == 'default'
