
from app.services.template_service import TemplateService
from app.services.zip_service import ZipService

class GeneratorService:
    def generate(self,payload):
        project_dir = TemplateService().render_project(
            payload.project_name,
            payload.db_type,
            payload.auth_type
        )
        archive = ZipService().build(project_dir)
        return {'archive': archive}
