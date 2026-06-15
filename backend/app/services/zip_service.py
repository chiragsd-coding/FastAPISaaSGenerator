
import zipfile

class ZipService:
    def build(self,project_dir):
        archive=f'{project_dir.name}.zip'
        with zipfile.ZipFile(archive,'w') as z:
            for f in project_dir.rglob('*'):
                if f.is_file():
                    z.write(f,f.relative_to(project_dir))
        return archive
