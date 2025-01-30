'''
Note: os.system() uses C command: system()
    It runs a text string as a commandline instruction.
'''

import os
import time

pipelineDirectory = os.getcwd()
sifDirectory = os.path.join(pipelineDirectory, 'SingularitySIFs')
sourceDirectory = os.path.join(pipelineDirectory, 'bids')
outputDirectoryQSI = os.path.join(pipelineDirectory, 'qsiprep')
sifFile = os.path.join(sifDirectory, 'qsiprep_latest.sif')

singularityCommandPart = f'singularity exec {sifFile}'

def dsiPrint(text):
    print(f'\nDSI-PIPELINE: {text}\n')

## run src on BIDS folder for each subject
for subjID in os.listdir(sourceDirectory):
    # source files:
    bidsPath = os.path.join(sourceDirectory, subjID)
    # output files:
    subjOutDir = os.path.join(outputDirectoryQSI, subjID)
    try:
        os.mkdir(subjOutDir)
    except FileExistsError:
        dsiPrint(f'QSIPrep already complete for subject: {subjID}! Attempting to continue pipeline...')
        continue
    qsiCommandPart = None #f'dsi_studio --action=src --source={bidsPath} --output={srcFiles}'

    fullCommandQSI = f'{singularityCommandPart} {qsiCommandPart}'
    dsiPrint(f'Running QSIPrep for subject: {subjID}.....')
    dsiPrint(fullCommandQSI)
    os.system(fullCommandQSI)
    dsiPrint(f'{subjID} QSIPrep  exited!')