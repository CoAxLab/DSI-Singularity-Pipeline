'''
This file runs bash commands to run the other python scripts in this repository sequentially. 
fixBIDS.py and setupPipeline.py must run separately as additional input is required between these steps.
'''

import os
def dsiPrint(text):
    print(f'\nDSI-PIPELINE: {text}\n')

dsiPrint(f'Running All Processes, starting with QSI Prep.')
qsiPrepCommand = f'python runQSIPrep.py'
dsiPrint(qsiPrepCommand)
os.system(qsiPrepCommand)

dsiPrint(f' QSI Prep complete...')
dsiPrint(f'Attempting to run reconstruction...')
recCommand = f'python runPipeline.py'
dsiPrint(recCommand)
os.system(recCommand)

dsiPrint(f'All Processes exited.')