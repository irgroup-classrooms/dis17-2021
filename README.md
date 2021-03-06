# Search Engine Technologies 2021 (DIS17.1)

## Slides and online lecture archive

All lectures will be hosted on Zoom: https://th-koeln.zoom.us/j/86500487419. The password for Zoom is the ZIP code of TH Köln @ Claudiusstraße 1. Lectures will be recorded and archived for later referal.

The following slide sets and videos are available. The password for the videos is the same as for the Zoom room.

* **01 Introduction** [[pdf]](slides/DIS17-01-introduction.pdf) [[video]](https://th-koeln.sciebo.de/s/zkxwDLmIf3RnFsL)
* **02 IR in a Nutshell and TREC Evaluations** [[pdf]](slides/DIS17-02-IR-Nutshell.pdf) [[video]](https://th-koeln.sciebo.de/s/5UlwblJSHsaqzTM)
* **03 Solr** [[pdf]](slides/DIS17-03-Solr.pdf) [[video]](https://th-koeln.sciebo.de/s/LCdBeIX4P2uPicY)
* **04 Indexing** [[pdf]](slides/DIS17-04-Indexing.pdf) [[video]](https://th-koeln.sciebo.de/s/D8DZUZHCmVUMb7E)
* **05 Solr-Hands-on**  [[script]](https://github.com/irgroup-classrooms/dis17-2021/blob/main/src/simple-run.py) [[video]](https://th-koeln.sciebo.de/s/zl6thuzMSKB9cg2)
* **06 Queries** [[pdf]](slides/DIS17-06-Queries.pdf) [[video]](https://th-koeln.sciebo.de/s/dZ5HXn7LmCvXav1)
* **07 Ranking** [[pdf]](slides/DIS17-07-Ranking.pdf) [[video]](https://th-koeln.sciebo.de/s/NvDsWWKTeYeAQDP)
* **08 Mini-TREC I** [[video]](https://th-koeln.sciebo.de/s/qAegnQcJFSPncjr)
* **09 Mini-TREC II** [[video]](https://th-koeln.sciebo.de/s/XX41g12SN9hoJYd)
* **10 World Café** [[pdf]](slides/DIS17-10-WorldCafe.pdf) [[Indexing I]](https://docs.google.com/document/d/1-iVhHXrXKlVBO61EOzLC617JPOhsFDBC8E_j1BLRz0Q/edit?usp=sharing) [[Indexing II]](https://docs.google.com/document/d/1b66n1VdY7UDPqCUaIwqftDDQrjE0ViJmxb_aytCiDUs/edit?usp=sharing) [[Ranking I]](https://docs.google.com/document/d/1oHHcT499xeog4Lm0x2jbDjOchpU08oop-mk-QcgMvl0/edit?usp=sharing) [[Ranking II]](https://docs.google.com/document/d/1KSpD2pMuLohX18vzpi24Tq6lZfxAuhC6a10m1dSn8d0/edit?usp=sharing) [[Querying I]](https://docs.google.com/document/d/1a8eb0MfDa25ztph-ad13x7ryjqmffCNFa9jKonqU3To/edit?usp=sharing) [[Querying II]](https://docs.google.com/document/d/1FdhdX3q3WBYbeAZh0RidFwAg0yZaTS7VpLrIkDsqxhI/edit?usp=sharing)

## Assignments and Teams

> [Teams and members](https://github.com/irgroup-classrooms/dis17-2021/blob/main/teams.md)

### Assignment I - Run the Solr tutorial and index CORD-19 (20 points)

1. Please work on the official Solr tutorial and go through all the three exercises. In [Exercise 1 - Launch Solr in SolrCloud Mode](https://solr.apache.org/guide/8_10/solr-tutorial.html#launch-solr-in-solrcloud-mode), you will set up your Solr cloud and get it running. Some important concepts and features of Solr like **nodes**, **shards**, and **replicas** are included in this setup guide. Understanding all of these features may be a little bit overwhelming for newcomers and **they will not be picked up during the rest of the tutorial**. Feel free to simply follow the setup guide without diving deep into these topics (copy & paste the commands). For those who are interested, the [Solr Glossary](https://solr.apache.org/guide/8_10/solr-glossary.html) provides some more information. In our tutorial, we will focus on the later sections - indexing and searching data.
2. In addition to exercise 3 index the CORD-19 data set from from 2020-07-16 that will be used in the later assignments again. **Hint:** More specifically, you have to index `metadata.csv`. *Please remember:* If you create a new collection using the `_default` configset, you are using a managed schema that has to be modified by the API or the Admin web interface. Some of the entries may result in errors during indexing, e.g., the data format of `publish_time` is not always consistent. To avoid these index errors, you have to define fields and the corresponding data format beforehand. Alternatively, you may choose to skip certain fields. Likewise, you have to define a catchall copy field in order to retrieve results for queries without specifying an additional category to search for (see link below).
    
    Indexing example: 
    ```
    bin/post -c <collection-name> path/to/metadata.csv -params "skip=<field-to-be-skipped>,<field-to-be-skipped>&header=true"
    ```
3. Make a screenshot of the results of a simple query from the official TREC-COVID topic set. We assigned one [topic number randomly to each student](topic-student.md). Name the file accordingly: `DIS17-2021-assignment1-LASTNAME-FIRSTNAME`.

Upload the screenshot until 2021-11-19 to this Sciebo folder: https://th-koeln.sciebo.de/s/FHerELroqNlwDPC

### Assignment II - Concept Paper (10 points)

This is the __first group assignment__. Write a two page concept paper (approx. 1000 words) and describe you planned approach for the Mini Trec Campaign. Please make sure that the following key aspects are included in you concept paper:

- There is a rough project plan or a project outline, which describes the ideas, the procedure and the goals of the project. 
- The idea is based on a coherent analysis of a problem regaring CORD-19, the topics or the relevance assessments.
- The ideas should be based on concepts from the lectures DIS08, DIS12 or any other DIS-related lecture/project. Additionally you may refer to external literature.
- Hint: Pick up some of the following ideas...
  - Analysis of the topics and development of a strategy to extract query terms from the topics - machine or manual implementation of the queries is possible. Tip: It is common to just take the title terms, for example.... But this works better!
  - Use of multilingual information
  - Use of query expansion and strategy to generate the expansions
  - Experiments with different ranking methods and weighting factors
  - Extension or adaptation of the indexing pipeline for better processing of the data set
  - A proprietary approach to improve retrieval performance
  - Make up your mind and find something on your own!

Upload the concept papers as PDF files until 2021-12-10 to this Sciebo folder: https://th-koeln.sciebo.de/s/FHerELroqNlwDPC - Name the file accordingly: `DIS17-2021-assignment2-GROUPNAME`.

### Assignment III - Start your Engines (30 points)

Based on your project plan from assignment II your team has to build and evaluate a search engine on finding relevant documents on COVID-19 and to submit the results (run files). 

- Use the TREC-COVID Complete test collection as our common document, topic and qrel set: https://ir.nist.gov/covidSubmit/data.html. 
- We will evalute your run files using trec_eval, so please make sure to test these files before submitting them. We will not fix parsing errors. 
- Choose some "speaking" names for your runs, like `BM25-manual-queries`.
- Your run files may contain up to 1000 documents per topic, but fewer documents are fine.
- Prepare a short 2-page overview paper including a short description of 
  1. Your original overall idea to test in the Mini-TREC campaign
  2. The retrieval methods used and the technical implementation
  3. Your evaluation and outcomes
  4. Next steps and ideas
- We will use these descriptions as input for our World Café on 2022-01-14. 

Each run must be contained in a single text file. Each line in the file must be in the form
```
         topicid Q0 docid rank score run-tag
```
where 
  - `topicid` is the topic number (1..50)
  - `Q0` is the literal 'Q0' (currently unused, but trec_eval expects this column to be present)
  - `docid` is the cord_uid of the document retrieved in this position. It must be a valid cord_id in the July 16 release of CORD-19. If it has already been judged for this topic, it will be removed.
  - `rank` is the rank position of this document in the list
  - `score` is the similarity score computed by the system for this document. When your run is processed (to create judgment sets and to score it using trec_eval), the run will be sorted by decreasing score and the assigned ranks will be ignored. In particular, trec_eval will sort documents with tied scores in an arbitrary order. If you want the precise ranking you submit to be used, that ranking must be reflected in the assigned scores, not the ranks.
  - `run-tag`	is a name assigned to the run. Tags must be unique across both your own runs and all other participants' runs, so you may have to choose a new tag if the one you used is already taken. 
  
Upload your __two most successful runs__ in the correct TREC run files format and the 2-page paper until 2022-01-13 16:00 to this Sciebo folder: https://th-koeln.sciebo.de/s/FHerELroqNlwDPC - Name the files accordingly: `DIS17-2021-assignment3-GROUPNAME-RUNNAME` and `DIS17-2021-assignment3-GROUPNAME-overview`. Change GROUPNAME and RUNNAME as it fits.

### Assignment IV - Write it down (40 points)

Based on the previous assignments we would like you to compile a final report including the following topics:

  1. Your original overall idea to test in the Mini-TREC campaign
  2. The retrieval methods used and the technical implementation
  3. Your evaluation and outcomes
  4. Next steps and ideas

The paper should respect the following requirements:

- Clear style of writing and textual presentation (in German or English). This is your (maybe) first scientific report. Get some inspiration on how to write these reports by looking at papers from [TREC](https://trec.nist.gov/proceedings/proceedings.html) or [CLEF](http://ceur-ws.org/Vol-2936/). 
- Cite relevant literature about methods/techniques.
- Use the [CEUR-WS Proceedings template](http://ceur-ws.org/Vol-XXX/CEURART.zip) in 1-column style. An Overleaf page for LaTeX users is available at https://www.overleaf.com/read/gwhxnqcghhdt.
- __All team members have to contribute__ to the report. Include an overview who contributed what part of the report. 

Upload your overview paper in PDF until 2022-02-28 to this Sciebo folder: https://th-koeln.sciebo.de/s/FHerELroqNlwDPC - Name the files accordingly: `DIS17-2021-assignment4-GROUPNAME-report`.

### Links: 
- Solr tutorial: https://solr.apache.org/guide/8_10/solr-tutorial.html
- CORD-19 from 2020-07-16: https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases/cord-19_2020-07-16.tar.gz
- TREC-COVID: https://ir.nist.gov/covidSubmit/
- TREC-COVID topic set: https://ir.nist.gov/covidSubmit/data/topics-rnd5.xml
- Create a "catchall" Copy Field: https://solr.apache.org/guide/8_10/solr-tutorial.html#create-a-catchall-copy-field
- `trec_eval` sources: https://github.com/usnistgov/trec_eval
- `trec_eval` [pre-compiled for Windows](download/trec_eval_win32.zip)

