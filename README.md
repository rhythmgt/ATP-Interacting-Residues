# ATP Interacting Residues

Given a protein sequence, identify which residues interact with ATP (adenosine triphosphate).

**Input format**\
Input is in the form of 2 columns: ID and label. For each ID , we have a label which denotes a residue in a given protein sequence. If the label is capitalized, the residue interacts with ATP, if not capitalized, then it does not interact.\
\
**Output format**\
Output file contains 2 columns, one is the sequence's ID and the other is the label. For each ID, label =1 indicates that the residue of given ID has interactions with ATP, if label =-1, it does not interact with ATP.
