# use python3 xxx.py instead of it? #!/usr/bin/env python3

import sys
from nltk.tokenize import sent_tokenize
#nltk.data.path.append('CUSTOMPATH')
data = sys.stdin.read()
a_list = sent_tokenize(data.replace('\n', ' '))
for line in a_list:
    print(line)


# ref:
# https://github.com/lervag/vimtex/issues/544#issuecomment-299477241

