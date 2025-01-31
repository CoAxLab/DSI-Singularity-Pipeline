'''Note: os.system() uses C command: system() to run a text string as a commandline instruction'''

import os
import time

pipelineDirectory = os.getcwd()
sifDirectory = os.path.join(pipelineDirectory, 'SingularitySIFs')
sourceDirectory = os.path.join(pipelineDirectory, 'bids')
outputDirectorySRC = os.path.join(pipelineDirectory, 'src')
sifFile = os.path.join(sifDirectory, 'dsistudio_latest.sif')

singularityCommandPart = f'singularity exec {sifFile}'

def dsiPrint(text):
    print(f'\nDSI-PIPELINE: {text}\n')

## run src on BIDS folder for each subject
for subjID in os.listdir(sourceDirectory):
    # source files:
    bidsPath = os.path.join(sourceDirectory, subjID)
    # output files:
    srcFiles = os.path.join(outputDirectorySRC, subjID)
    try:
        os.mkdir(os.path.join(outputDirectorySRC, subjID))
    except FileExistsError:
        dsiPrint(f'src action already complete for subject: {subjID}! Attempting to continue pipeline...')
        continue
    srcCommandPart = f'dsi_studio --action=src --source={bidsPath} --output={srcFiles}'

    fullCommandSrc = f'{singularityCommandPart} {srcCommandPart}'
    dsiPrint(f'Running DSI Studio src action for subject: {subjID}.....')
    dsiPrint(fullCommandSrc)
    os.system(fullCommandSrc)
    dsiPrint(f'{subjID} src action exited!')

reconOutputDirectory = os.path.join(pipelineDirectory, 'fib')
for subjID in os.listdir(outputDirectorySRC):
    start = time.time()
    # src files for input
    subjectSrcDirectory = os.path.join(outputDirectorySRC, subjID)
    srcFilesForRecon = os.path.join(subjectSrcDirectory, '*.src.gz')
    # fib output file
    subjRecOutDirectory = os.path.join(reconOutputDirectory, subjID)
    try:
        os.mkdir(subjRecOutDirectory)
    except FileExistsError:
        dsiPrint(f'recon output directory already exists for subject: {subjID}.....')
        continue

    # Optionally add settings to reconCommandPart to use settings described in the string
    settings = '--method=7 --param0=1.25 --nthreads=1 --other_output=all'
    reconCommandPart = f'dsi_studio --action=rec --source={srcFilesForRecon} --output={subjRecOutDirectory} {settings}'

    fullRecCommand = f'{singularityCommandPart} {reconCommandPart}'
    dsiPrint(f'Running DSI Studio recon action for subject: {subjID}.....')
    dsiPrint(f'cd src/{subjID}')
    dsiPrint(fullRecCommand)
    os.chdir(os.path.join(outputDirectorySRC, subjID))
    os.system(fullRecCommand)
    end = time.time()
    dsiPrint(f'{subjID} recon exited in {end - start} seconds!')