import setuptools, json, pathlib, os

"""
[USAGE]:
# First
    * python3.7 -m pip install --upgrade pip setuptools wheel

# Source Distribution - Recompile on any platform
    * python3.7 setup.py sdist

# Built Distribution - Archive to a specific platform (Ex: linux-x86_64)
    * python3.7 setup.py bdist_wheel
"""


PROJECT = pathlib.Path(__file__).resolve().parents[0]
GET_DATA_FILES = lambda folder: "\n".join( [ f"""include { x[0].replace(f'{ str(PROJECT) }/','') }/*""" for x in os.walk( f"{ PROJECT }/{ folder }" ) ] )

MANIFEST_TEXT = f"""
include README.md
include LICENSE.txt
include CONFIG.json
{ GET_DATA_FILES('docs') }
{ GET_DATA_FILES('static') }
{ GET_DATA_FILES('views') }
""".strip()

with open("CONFIG.json", "r") as f:
    CONFIG = json.load(f)

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open("MANIFEST.in", "w") as f:
    f.write( MANIFEST_TEXT )
    f.close()

def form(**kwargs) : pass #print(kwargs)

#setuptools.setup
form(
    packages                        = setuptools.find_packages(exclude=(".git",)),
    url                             = f"""https://github.com/{ CONFIG['org'] }/{ PROJECT.name }""" if not CONFIG['url'] else CONFIG['url'],
    package_dir                     = {'.': 'core'},
    python_requires                 = CONFIG['python_requires'],
    name                            = PROJECT.name,
    version                         = CONFIG['version'],
    author                          = CONFIG['org'],
    author_email                    = CONFIG['email'],
    description                     = CONFIG['description'],
    long_description                = LONG_DESCRIPTION,
    long_description_content_type   = "text/markdown",
    classifiers                     = CONFIG['classifiers'],
    project_urls                    = CONFIG['project_urls'],
)
