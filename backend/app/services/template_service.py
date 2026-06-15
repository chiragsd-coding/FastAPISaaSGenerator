
from pathlib import Path
from jinja2 import Template

class TemplateService:
    def render_project(self,name,db,auth):
        out = Path('generated')/name
        out.mkdir(parents=True,exist_ok=True)

        content = Template(
            'PROJECT={{name}}\nDB={{db}}\nAUTH={{auth}}'
        ).render(name=name,db=db,auth=auth)

        (out/'README.md').write_text(content)
        return out
