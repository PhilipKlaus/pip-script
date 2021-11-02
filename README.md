# pip-script

A Python package for executing pip (*Python Package Manager*) commands from within code more easily

**pip-script** provides a wrapper for pip commands and their arguments. Internally, pip-script make use of
the [subprocess](https://docs.python.org/3/library/subprocess.html) package to execute pip. The basic usage is as
follows:

    pip.command().arg1().arg2().argN().run()

## Example

``` python
import pipscript as pip

# simple call to pip list with the --include-editable argument
pip.list().include_editable().run()
```
