import json
import restswag
import wsmeswag
import inspect
from oslo_utils import importutils
import sys

# arg1: path to root controller e.g. test_project.root.RootController
# arg2: name of project e.g. testproject
# arg3: version of project e.g. 2.1.1

# for debugging purposes
_c = []


path_to_controller = str(sys.argv[1])
rootcontroller = importutils.import_class(path_to_controller)

def collect_swagger(title, version):
    swagger = {}
    swagger['swagger'] = '2.0'
    swagger['info'] = {    'title': title,
                            "description": str(inspect.getcomments(rootcontroller)),
                            'version': version,
                            "license": {
                                "name": "Apache 2.0",
                                "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
                            }
    }
    swagger['host'] = '/'
    swagger['schemes'] = ['http']
    swagger['basePath'] = '/'
    swagger['produces'] = ['application/json']

    controllers = restswag.collect_controllers(rootcontroller)
    _c.append(controllers)
    methods = restswag.collect_methods(controllers)

    paths = wsmeswag.getpaths(methods)
    swagger['paths'] = paths

    definitions = wsmeswag._definitions
    swagger['definitions'] = definitions

    print json.dumps(swagger, indent=2)

# run the method below with your project name and version and scooop up your swagger spec from terminal output

# collect_swagger(project_name, project_version)

project_name = str(sys.argv[2])
project_version = str(sys.argv[3])

collect_swagger(project_name, project_version)
