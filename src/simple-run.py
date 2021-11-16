from requests import get    
from bs4 import BeautifulSoup 

BASE_URL = "http://localhost:8983/solr/cord19/select?q="
FIELDS = "&fl=cord_uid,score"
ROWS = "&rows="
rows = 2000
RUN_FILE = 'data/bm25.k1.12.b.075.txt'
TAG = 'solr-bm25'

with open('data/topics-rnd5.xml', 'r') as f:
    data = f.read() 

bs_data = BeautifulSoup(data, 'xml') 

topics = bs_data.find_all('topic')

with open(RUN_FILE, 'w') as f_out:
    for topic in topics:
        num = topic.get('number')
        q = topic.query.text.replace(' ', '%20')
        
        url = ''.join([BASE_URL, q, FIELDS, ROWS, str(rows)])
        r = get(url)
        json = r.json()
        
        rank = 1
        
        docs = set()
        
        for doc in json.get('response').get('docs'):
            docid = doc.get('cord_uid')[0]
            if docid not in docs and len(docs) < 1000:
                docs.add(docid)
                score = doc.get('score')
                out_str = '\t'.join([num, 'Q0', docid, str(rank), str(score), TAG])
                f_out.write(out_str + '\n')
                rank += 1
