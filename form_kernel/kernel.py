from metakernel import MetaKernel
import form

__version__ = '0.2.0'

class FormKernel(MetaKernel):
    implementation = 'form_kernel'
    implementation_version = __version__
    language = 'FORM'
    language_version = '4.2'
    banner = 'FORM kernel started'
    language_info = {'name': 'FORM',
#                      'codemirror_mode': {
#                          "version": 2,
#                          "name": 'form'
#                      },
                     'nbconvert_exporter': 'form_kernel.exporter.FormExporter',
                     'mimetype': 'text/x-form',
                     'file_extension': '.frm'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__start_form()
        
    def __start_form(self):
        self.form = form.open()
    
    def do_execute_direct(self, code):
        try:
            if not code.startswith("read"):
                self.form.write(code)
            else:
                res = self.form.read(code[5:])
                return res
        except form.FormError as e:
            res = str(e) + '\nRestarting FORM'
            self.Error(res)
            self.__start_form()

    def do_shutdown(self, restart):
        self.form.close()
        return {'status': 'ok', 'restart': restart}

    def get_usage(self):
        return "This is the FORM kernel."

    def repr(self, data):
        return repr(data)


if __name__ == '__main__':
    FormKernel.run_as_main()
