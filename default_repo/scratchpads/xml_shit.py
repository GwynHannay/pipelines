"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""

import xmlschema
from xmlschema.extras import codegen
import pandas as pd

schema = xmlschema.XMLSchema('/filedrop/PHOLSchema-V3.1.xsd', base_url='/filedrop/', converter=xmlschema.UnorderedConverter)
# xml_doc = xmlschema.XmlDocument()
json_data = xmlschema.to_dict('/filedrop/combined-sample.xml', schema=schema, path='/Products/*')
print(json_data[3])
# df = pd.json_normalize(json_data)

# generator = codegen.PythonGenerator(schema)

# print(generator.get_template())
