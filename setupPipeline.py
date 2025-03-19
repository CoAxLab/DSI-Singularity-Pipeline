import os

pipelineDirectory = os.getcwd()

def dsiPrint(text):
    print(f'\nDSI-PIPELINE: {text}\n')

# create directories
sifDirectory = os.path.join(pipelineDirectory, 'SingularitySIFs')
sourceDirectory = os.path.join(pipelineDirectory, 'bids')
outputDirectoryQSI = os.path.join(pipelineDirectory, 'qsiprep')
outputDirectorySRC = os.path.join(pipelineDirectory, 'src')
outputDirectoryFIB = os.path.join(pipelineDirectory, 'fib')
for path in [sourceDirectory, sifDirectory, outputDirectorySRC, outputDirectoryFIB, outputDirectoryQSI]:
    try:
        os.mkdir(path)
        dsiPrint(f'Created directory at: {path}!')
    except FileExistsError:
        dsiPrint(f'File path: {path} already exists!')

# pull SIF file for dsi studio
dsiPrint(f'Pulling latest SIF files to {sifDirectory}...')
os.chdir(sifDirectory)
os.system('docker pull dsistudio/dsistudio:latest')
os.system('docker pull pennlinc/qsiprep:latest')
os.chdir(pipelineDirectory)

dsiPrint(f'Set-Up complete!')
dsiPrint(f'Please move participant data directories to:\n\t\t{sourceDirectory}')