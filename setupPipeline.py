import os

pipelineDirectory = os.getcwd()

def dsiPrint(text):
    print(f'\nDSI-PIPELINE: {text}\n')

# create directories
sifDirectory = os.path.join(pipelineDirectory, 'SingularitySIFs')
sourceDirectory = os.path.join(pipelineDirectory, 'dicom')
outputDirectorySRC = os.path.join(pipelineDirectory, 'src')
outputDirectoryFIB = os.path.join(pipelineDirectory, 'fib')
for path in [sifDirectory, sourceDirectory, outputDirectorySRC, outputDirectoryFIB]:
    try:
        os.mkdir(path)
        dsiPrint(f'Created directory at: {path}!')
    except FileExistsError:
        dsiPrint(f'File path: {path} already exists!')

# pull SIF file for dsi studio
dsiPrint(f'Pulling latest SIF files to {sifDirectory}...')
os.chdir(sifDirectory)
os.system('singularity pull docker://dsistudio/dsistudio:latest')
os.system('singularity pull docker://nipreps/mriqc:latest')
os.chdir(pipelineDirectory)

dsiPrint(f'Set-Up complete!')
dsiPrint(f'Please move participant data directories to:\n\t\t{sourceDirectory}')