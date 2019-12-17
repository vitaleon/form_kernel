import os
import os.path

from traitlets.config import Config
from nbconvert.exporters.templateexporter import TemplateExporter

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------

class FormExporter(TemplateExporter):
    """
    Form exporter
    """

    # If this custom exporter should add an entry to the
    # "File -> Download as" menu in the notebook, give it a name here in the
    # `export_from_notebook` class member
    export_from_notebook = "FORM"

    def _file_extension_default(self):
        """
        The new file extension is `.frm`
        """
        return '.frm'

    @property
    def template_path(self):
        """
        We want to inherit from script template, and have template under
        `./templates/` so append it to the search path. (see next section)
        """
        return super().template_path+[os.path.join(os.path.dirname(__file__), "templates")]

    def _template_file_default(self):
        """
        We want to use the new template we ship with our library.
        """
        return 'FORM'
