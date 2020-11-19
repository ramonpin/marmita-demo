## Marmita SDK Demo
Just a demo of Scala -> Python integration.

### Tooling

To work in this package is recomended to use `tox` python automation tool. You can install `tox` in your environment with:

```bash
$> python3 -m venv $HOME/.tox
$> $HOME/.tox/bin/pip install tox==3.20.1
$> ln -s $HOME/.tox/bin/tox $HOME/bin/tox
```

Where you can replace `$HOME/bin` for any directory where you install your user tools (and is in your path).

Now you can check it works with:

```bash
$> tox --version
3.20.1 imported from /home/user/.tox/lib/python3.8/site-packages/tox/__init__.py
```

##### Development

To install the project in a virtualenv for development use:

```bash
$> tox --devenv <venv_dir> -e py<xx>
```

Where `venv_dir` is the directory where you want to create the virtual environment and `xx` can be `36`, `37` or `38` 
depending on your preference of python3 version.

A `marmita-demo` script should be created and available in the path, pointing to the local project files.
The local installation only needs to be done again if the main method or the `setup.py` script changes.

You can run all tests and pass the linter check on all the available python3 versions at once with:

```bash
$> tox
```

Or you can just try one with:

```bash
$> tox -e py<xx>
```

##### Run demo script

Just to try that the installation process works and that integration works properly you can try:

```bash
$> tox -qe run
```

##### Release as python wheel

To package for distribution, execute the following:

```bash
$> tox -e package
```

The above command creates a `marmitasdk-<version>-py3-none-any.whl` executable at `dist` directory. This 
file can be distributed.
