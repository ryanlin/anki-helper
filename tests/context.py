import os
import sys

# project root path
project_root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__),'..')
    )
sys.path.insert(0, project_root_path)

# Add project src path
project_src_path = os.path.abspath(
    os.path.join(project_root_path, 'src')
    )
sys.path.insert(0, project_src_path)

import anki.ankiconnect as ankiconnect
import anki
import ankigpt.llm as llm
import ankigpt.ankigpt as ankigpt
import create