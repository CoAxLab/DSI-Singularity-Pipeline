import os
def dsiPrint(text):
    print(f'\nDSI-PIPELINE: {text}\n')

pipelineDirectory = os.getcwd()
bidsDir = os.path.join(pipelineDirectory, 'bids')

def cleanSession(sessionPath):
    ### sessionPath should be full file path, ses is session dir name
    for subDir in os.listdir(sessionPath):
        currDir = os.path.join(sessionPath, subDir)
        for file in os.listdir(currDir):
            currFilePath = os.path.join(currDir, file)
            if 's2_' in file:
                newFile = file.replace('s2_', '_ses-2_')
            elif 's1_' in file:
                newFile = file.replace('s1_', '_ses-1_')
            else:
                dsiPrint(f'did not detect changes for \n\t{sessionPath}\n')
                continue
            newFilePath = os.path.join(currDir, newFile)
            #dsiPrint(f'mv {currFilePath} {newFilePath}')
            os.system(f'mv "{currFilePath}" "{newFilePath}"')

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
        
        ### clean session contents
        cleanSession(sessionDir)

        if newName != ses:
            newSessionDir = os.path.join(subjectDir, newName)
            #dsiPrint(f'mv {sessionDir} {newSessionDir}')
            os.system(f'mv "{sessionDir}" "{newSessionDir}"')
        else:
            dsiPrint(f'rename not needed for subject {subject}, session {ses}')