from unipath import Path
import nltk

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR.child("data")
HTML_DIR = DATA_DIR.child("html")
CORPUS_DIR = DATA_DIR.child("corpus")

nltk.data.path.append(CORPUS_DIR)
nltk.download(['punkt',
               'stopwords'
               ], download_dir=CORPUS_DIR, quiet=True)
