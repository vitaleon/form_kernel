from metakernel import MetaKernel
import form, sys

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
                self.form.write(".sort")
                res = self.form.read(code[5:])
                return res
        except form.FormError as e:
            self.Error(str(e))
            self.do_shutdown(True)
        except form.IOError as e:
            self.Error(str(e))
            self.do_shutdown(True)
        except:
            self.Error('Unexpected error:', sys.exc_info()[0], '\n')
            self.do_shutdown(True)

    def do_shutdown(self, restart):
        self.form.close()
        return super().do_shutdown(restart)

    def restart_kernel(self):
        self.form.close()
        self.__start_form()

    def get_usage(self):
        return "This is the FORM kernel."

    def post_execute(self, retval, code, silent):
        """Post-execution actions
        Handle special kernel variables and display response if not silent.
        """
        # Handle in's
        self.set_variable("_iii", self._iii)
        self.set_variable("_ii", self._ii)
        self.set_variable("_i", code)
        self.set_variable("_i" + str(self.execution_count), code)
        self._iii = self._ii
        self._ii = code
        if (retval is not None):
            # --------------------------------------
            # Handle out's (only when non-null)
            self.set_variable("___", self.___)
            self.set_variable("__", self.__)
            self.set_variable("_", retval)
            self.set_variable("_" + str(self.execution_count), retval)
            self.___ = self.__
            self.__ = retval
            self.log.debug(retval)
            content = {
                'execution_count': self.execution_count,
                'data': {'text/plain':str(retval)},
                'metadata':  {}
            }
            if not silent:
                self.send_response(self.iopub_socket, 'execute_result', content)


if __name__ == '__main__':
    FormKernel.run_as_main()
