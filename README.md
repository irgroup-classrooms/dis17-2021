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
4. Upload the screenshot until 2021-11-19 to this Sciebo folder: https://th-koeln.sciebo.de/s/FHerELroqNlwDPC

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

### Links: 
- Solr tutorial: https://solr.apache.org/guide/8_10/solr-tutorial.html
- CORD-19 from 2020-07-16: https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases/cord-19_2020-07-16.tar.gz
- TREC-COVID: https://ir.nist.gov/covidSubmit/
- TREC-COVID topic set: https://ir.nist.gov/covidSubmit/data/topics-rnd5.xml
- Create a "catchall" Copy Field: https://solr.apache.org/guide/8_10/solr-tutorial.html#create-a-catchall-copy-field
- `trec_eval` sources: https://github.com/usnistgov/trec_eval
- `trec_eval` [pre-compiled for Windows](download/trec_eval_win32.zip)

