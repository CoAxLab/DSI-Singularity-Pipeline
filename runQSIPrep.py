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
sifFile = os.path.join(sifDirectory, 'qsiprep_latest.sif')

singularityCommandPart = f'docker run -it --rm -v "{sourceDirectory}":/bids -v "{outputDirectoryQSI}":/output pennlinc/qsiprep:latest'

def dsiPrint(text):
    print(f'\nDSI-PIPELINE: {text}\n')

## run src on BIDS folder for each subject
for subjID in os.listdir(sourceDirectory):
    if '.tsv' in subjID or '.json' in subjID: continue
    # output files:
    subjOutDir = os.path.join(outputDirectoryQSI, subjID)
    workDir = os.path.join(subjOutDir, 'work')
    try:
        os.mkdir(subjOutDir)
        os.mkdir(workDir)
    except FileExistsError:
        dsiPrint(f'QSIPrep already complete for subject: {subjID}! Attempting to continue pipeline...')
        #continue
    options = f'--participant-label {subjID} --output-resolution 2 --unringing-method mrdegibbs --omp-nthreads 8 --nthreads 8 --mem-mb 16000 --fs-license-file "{fsLicense}"'
    qsiCommandPart = f'/bids /output  participant --output-resolution 2 -w /output/work --skip-bids-validation {options}'

    fullCommandQSI = f'{singularityCommandPart} {qsiCommandPart}'
    dsiPrint(f'Running QSIPrep for subject: {subjID}.....')
    dsiPrint(fullCommandQSI)
    os.system(fullCommandQSI)
    dsiPrint(f'{subjID} QSIPrep  exited!')