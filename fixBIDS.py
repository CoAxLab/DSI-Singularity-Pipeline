import os
def dsiPrint(text):
    print(f'\nDSI-PIPELINE: {text}\n')

pipelineDirectory = os.getcwd()
bidsDir = os.path.join(pipelineDirectory, 'bids')

for subject in os.listdir(bidsDir):
    if 'sub-' not in subject:
        continue
    subjectDir = os.path.join(bidsDir, subject)
    for ses in os.listdir(subjectDir):
        sessionDir = os.path.join(subjectDir, ses)
        if 's1' in ses or '-1' in ses:
            newName = 'ses-1'
        elif 's2' in ses or '-2' in ses:
            newName = 'ses-2'
        # insert func to change inner files
        if newName == None:
            raise Exception(f'ERROR: newName is not found')
        newSessionDir = os.path.join(subjectDir, newName)
        os.system(f'mv {sessionDir} {newSessionDir}')
