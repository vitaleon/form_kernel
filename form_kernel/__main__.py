from ipykernel.kernelapp import IPKernelApp
from .kernel import FormKernel

IPKernelApp.launch_instance(kernel_class=FormKernel)
