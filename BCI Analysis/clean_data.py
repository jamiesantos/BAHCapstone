import pandas as pd
import numpy as np
with open("data\Jamie_Cup1.csv") as input_file:
    reader = csv.reader(input_file)
    desired_rows = [row for row_number, row in enumerate(reader)
                    if row_number in DESIRED_ROWS]

                    
