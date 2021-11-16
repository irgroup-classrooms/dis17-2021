# Search Engine Technologies 2021 (DIS17.1)

## Slides and online lecture archive

All lectures will be hosted on Zoom: https://th-koeln.zoom.us/j/86500487419. The password for Zoom is the ZIP code of TH Köln @ Claudiusstraße 1. Lectures will be recorded and archived for later referal.

The following slide sets and videos are available. The password for the videos is the same as for the Zoom room.

* **01 Introduction** [[pdf]](slides/DIS17-01-introduction.pdf) [[video]](https://th-koeln.sciebo.de/s/zkxwDLmIf3RnFsL)
* **02 IR in a Nutshell and TREC Evaluations** [[pdf]](slides/DIS17-02-IR-Nutshell.pdf) [[video]](https://th-koeln.sciebo.de/s/5UlwblJSHsaqzTM)
* **03 Solr** [[pdf]](slides/DIS17-03-Solr.pdf) [[video]](https://th-koeln.sciebo.de/s/LCdBeIX4P2uPicY)
* **04 Indexing** [[pdf]](slides/DIS17-04-Indexing.pdf) [[video]](https://th-koeln.sciebo.de/s/D8DZUZHCmVUMb7E)
* **05 Solr-Hands-on** [[video]](https://th-koeln.sciebo.de/s/zl6thuzMSKB9cg2)

## Assignments and Teams

Please register your teams: https://forms.gle/fXXdQG8qr7YVXWXLA 

### Assignment I - Run the Solr tutorial and index CORD-19

1. Please work on the official Solr tutorial and go through all the three exercises. In [Exercise 1 - Launch Solr in SolrCloud Mode](https://solr.apache.org/guide/8_10/solr-tutorial.html#launch-solr-in-solrcloud-mode), you will set up your Solr cloud and get it running. Some important concepts and features of Solr like **nodes**, **shards**, and **replicas** are included in this setup guide. Understanding all of these features may be a little bit overwhelming for newcomers and **they will not be picked up during the rest of the tutorial**. Feel free to simply follow the setup guide without diving deep into these topics (copy & paste the commands). For those who are interested, the [Solr Glossary](https://solr.apache.org/guide/8_10/solr-glossary.html) provides some more information. In our tutorial, we will focus on the later sections - indexing and searching data.
2. In addition to exercise 3 index the CORD-19 data set from from 2020-07-16 that will be used in the later assignments again. **Hint:** More specifically, you have to index `metadata.csv`. *Please remember:* If you create a new collection using the `_default` configset, you are using a managed schema that has to be modified by the API or the Admin web interface. Some of the entries may result in errors during indexing, e.g., the data format of `publish_time` is not always consistent. To avoid these index errors, you have to define fields and the corresponding data format beforehand. Alternatively, you may choose to skip certain fields. Likewise, you have to define a catchall copy field in order to retrieve results for queries without specifying an additional category to search for (see link below).
    
    Indexing example: 
    ```
    bin/post -c <collection-name> path/to/metadata.csv -params "skip=<field-to-be-skipped>,<field-to-be-skipped>&header=true"
    ```
3. Make a screenshot of the results of a simple query from the official TREC-COVID topic set. We assigned one [topic number randomly to each student](topic-student.md). Name the file accordingly: `DIS17-2021-assignment1-LASTNAME-FIRSTNAME`.
4. Upload the screenshot until 2021-11-19 to this Sciebo folder: https://th-koeln.sciebo.de/s/FHerELroqNlwDPC

Links: 
- Solr tutorial: https://solr.apache.org/guide/8_10/solr-tutorial.html
- CORD-19 from 2020-07-16: https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases/cord-19_2020-07-16.tar.gz
- TREC-COVID: https://ir.nist.gov/covidSubmit/
- TREC-COVID topic set: https://ir.nist.gov/covidSubmit/data/topics-rnd5.xml
- Create a "catchall" Copy Field: https://solr.apache.org/guide/8_10/solr-tutorial.html#create-a-catchall-copy-field





## Syllabus

The following syllabus is an overview on the topics I plan to cover in this semester. Stay tuned!

![syllabus](syllabus.png)
