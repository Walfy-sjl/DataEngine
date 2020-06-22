import numpy as np
import pandas as pd
import seaborn as sns

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

titanic = sns.load_dataset('titanic')

print(titanic)