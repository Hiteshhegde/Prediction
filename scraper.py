import glassdoor as glass
import pandas as pd

raw_data = glass.get_jobs("data scientist",20,False,15)
