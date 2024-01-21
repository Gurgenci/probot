#
from ute import init_openai
(Client, LLM)=init_openai()
webfolder="general"
datafolder="data"+"/"+webfolder+"/"
DataFile=datafolder+"data"+".txt"
TextListFile=datafolder+webfolder+"_textlist.txt"
UploadListFile=datafolder+webfolder+"_uploadlist.txt"
UploadIDFile=datafolder+webfolder+"_uploadid.txt"
EmbeddingFile=datafolder+webfolder+"_embedding.npz"
#
TextSimilarity=None
topN=None
N=3
#
Thread=None
Run=None
Messages=[]
RunIDs=[]

# Define the md() function to display markdown text
from IPython.display import display, Markdown
def md(s):
    display(Markdown(s))

def showglobals():
    s="|Contents|File Name|\n|--|--|\n\
|Web folder name|"+webfolder+"|\n\
|Data folder name|"+datafolder+"|\n\
|Data file name|"+DataFile+"|\n\
|Text list file name|"+TextListFile+"|\n\
|Upload list file name|"+UploadListFile+"|\n\
|Upload ID file name|"+UploadIDFile+"|\n\
|Embedding file name|"+EmbeddingFile+"|\n\
|Client|"+str(Client)+"|\n\
|LLM|"+str(LLM)+"|\n\
\n\n\n\n"
   
    s+="|Variable name|Description|\n|--|--|\n\
|`webfolder`|Web folder name|\n\
|`datafolder`|Data folder name|\n\
|`DataFile`|Data file name|\n\
|`TextListFile`|Text list file name|\n\
|`UploadListFile`|Upload list file name|\n\
|`UploadIDFile`|Upload ID file name|\n\
|`EmbeddingFile`|Embedding file name|\n\
|`Client`|OpenAI client|\n\
|`LLM`|Language model|\n\
`UploadList`|List of file names to upload|\n\
`UploadID`|List of OpenAI file IDs (created when files are uploaded)|\n\
`TextList`|List of text files (as pairs of two lines, URL and title)|\n\
`Embedding`|Embedding matrix|\n\
`TextSimilarity`|Similarity vector|\n\
`topN`|`TextSimilarity` indices of the N best-matching pages|\n\
`N`|Number of best-matching pages to display|\n\
`Thread`|Current thread object|\n\
`Run`|Current run object|\n\
`Messages`|List of messages on the current thread|\n\
`RunIDs`|List of run IDs on the current thread|\n\
\n\n"
    return s