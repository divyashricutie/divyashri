
import os, sys
import pandas as pd
import numpy as np
from visa.constant import *
from visa.logger import logging
from visa.exception import CustomException
from visa.pipeline.pipeline import Pipeline 
import os, sys

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()


    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()