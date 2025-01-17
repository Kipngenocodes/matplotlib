import matplotlib.pyplot as plt
import numpy as np

'''
When data is symmetrical around a center (e.g., positive and negative anomalies around 0), the colors.
CenteredNorm() class can be used. It automatically maps the center to 0.5, 
and the point with the largest deviation from the center to 1.0 or 0.0, depending on its value.
'''