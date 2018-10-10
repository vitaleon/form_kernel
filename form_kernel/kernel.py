from ipykernel.kernelbase import Kernel
import form

__version__ = '0.1.0'

class FormKernel(Kernel):
    implementation = 'form_kernel'
    implementation_version = __version__
    language = 'FORM'
    language_version = '4.2'
    banner = 'FORM kernel started'
    language_info = {'name': 'FORM',
                     'codemirror_mode': 'form',
                     'mimetype': 'text/plain',
                     'file_extension': '.frm'}

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.__start_form()
        
    def __start_form(self):
        self.form = form.open()
    
    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        if not code.startswith("read"):
            self.form.write(code)
            silent = True
        else:
            res = self.form.read(code[5:])
        if not silent:
            stream_content = {'name': 'stdout', 'text': res}
            self.send_response(self.iopub_socket, 'stream', stream_content)
  
        return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}

    def do_shutdown(self, restart):
        self.form.close()
        return {'status': 'ok', 'restart': restart}