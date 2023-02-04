from import_export.admin import ExportMixin


class CeleryExportMixin(ExportMixin):

    def has_export_permission(self, request):
        """Removing export permission through django import export"""
        return False
