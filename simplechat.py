# I set my OPENAI_API_KEY in a .env file.  You can also set it in your environment variables.
# The following two lines read the .env file and set the environment variable.
import dotenv
dotenv.load_dotenv()
import os
print("Current Working Directory:", os.getcwd())
import math
import numpy as np
from ute import embedweb

embedweb()

