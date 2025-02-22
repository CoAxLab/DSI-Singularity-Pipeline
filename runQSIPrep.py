'''
Note: os.system() uses C command: system()
    It runs a text string as a commandline instruction.
'''

import os

pipelineDirectory = os.getcwd()
sifDirectory = os.path.join(pipelineDirectory, 'SingularitySIFs')
sourceDirectory = os.path.join(pipelineDirectory, 'bids')
outputDirectoryQSI = os.path.join(pipelineDirectory, 'qsiprep')
fsLicense = os.path.join(pipelineDirectory, 'license.txt')
sifFile = os.path.join(sifDirectory, 'qsiprep_1.0.0.sif')

singularityCommandPart = f'singularity run {sifFile}'

def dsiPrint(text):
    print(f'\nDSI-PIPELINE: {text}\n')

## run src on BIDS folder for each subject
for subjID in os.listdir(sourceDirectory):
    if '.tsv' in subjID or '.json' in subjID: continue
    # source files:
    bidsPath = os.path.join(sourceDirectory, subjID)
    # output files:
    subjOutDir = os.path.join(outputDirectoryQSI, subjID)
    workDir = os.path.join(subjOutDir, 'work')
    try:
        os.mkdir(subjOutDir)
        os.mkdir(workDir)
    except FileExistsError:
        dsiPrint(f'QSIPrep already complete for subject: {subjID}! Attempting to continue pipeline...')
        continue
    options = f'--participant_label {subjID} --output-resolution 2 --unringing-method mrdegibbs --fs-license-file {fsLicense}'
    qsiCommandPart = f'{bidsPath} {subjOutDir} -w {workDir} {options}'

    fullCommandQSI = f'{singularityCommandPart} {qsiCommandPart}'
    dsiPrint(f'Running QSIPrep for subject: {subjID}.....')
    dsiPrint(fullCommandQSI)
    os.system(fullCommandQSI)
    dsiPrint(f'{subjID} QSIPrep  exited!')