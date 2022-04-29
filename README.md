# pip-script
A Python package for executing pip (*Python Package Manager*) commands from within code.

Supported pip verion: **>=22.0.4**

**pip-script** provides a wrapper for pip commands and their arguments. Internally, pip-script make use of the [subprocess](https://docs.python.org/3/library/subprocess.html) package to execute pip.
The basic usage is as follows:
``` python
    pip.command().arg1().arg2().argN().run()
```

## Example

``` python
import pipscript as pip

# simple call to pip 'list' with the '--include-editable' argument
pip.list().include_editable().run()
```

## Documentation
Please refer to the official [pip documentation](https://pip.pypa.io/en/stable/). 

## Current status
Currently, the following pip commands are wrapped:
- *list*
- *show*
- *install*
