## A Jupyter kernel for [FORM](https://www.nikhef.nl/~form/)

This requires **Jupyter Notebook** <http://jupyter.readthedocs.org/en/latest/install.html> 
and [python-form](https://pypi.org/project/python-form/) installed.

To install:

```bash
python -m form_kernel.install --user
```

To use it, run one of:

```bash
jupyter notebook
# In the notebook interface, select FORM from the 'New' menu
jupyter qtconsole --kernel form
jupyter console --kernel form
```

For details of how this works, see the Jupyter docs on [wrapper kernels](https://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html).
