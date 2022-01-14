# DIS17 - Results of the Assignment

## Assignment I 

- 4 pts for wrong file names
- 4 pts for wrong query

## Results

| Student ID| A1 |
|----------|----|
| 11093999 | 20 |
| 11094995 | 20 |
| 11095449 | 0  |
| 11096202 | 20 |
| 11110703 | 20 |
| 11118344 | 20 |
| 11120099 | 20 |
| 11121154 | 20 |
| 11128330 | 20 |
| 11133327 | 20 |
| 11134199 | 20 |
| 11134202 | 20 |
| 11134303 | 20 |
| 11134718 | 20 |
| 11135533 | 20 |
| 11136112 | 20 |
| 11136561 | 20 |
| 11136865 | 20 |
| 11136973 | 20 |
| 11139754 | 20 |
| 11139919 | 20 |
| 11139926 | 16 |
| 11140076 | 20 |
| 11140334 | 16 |
| 11140537 | 20 |
| 11140538 | 20 |
| 11140540 | 20 |
| 11140576 | 20 |
| 11140578 | 16 |
| 11140591 | 20 |
| 11140612 | 20 |
| 11140624 | 16 |
| 11140625 | 20 |
| 11140903 | 20 |
| 11140904 | 20 |
| 11140931 | 16 |
| 11140939 | 16 |
| 11141179 | 20 |
| 11141352 | 20 |
| 11141379 | 20 |
| 11141419 | 20 |
| 11141762 | 20 |
| 11141763 | 20 |
| 11142356 | 20 |
| 11142385 | 20 |
| 11142933 | 20 |
| 11143182 | 20 |
| 11143471 | 20 |
| 11143680 | 20 |
| 11143789 | 20 |
| 11152050 | 20 |

## Assignment II

### General concerns

- Unspecific problem description: please address the properties of the CORD19 datasets and identify problems that might occur

- Unspecific goals: which of the outlined problems do you want to address?

- Missing details on the evaluation setup
    - What basline are you planning to use?
    - Which measures do you want to evaluate and why?
    - When you claim success? How do you measure improvements?
    - What kinds of tools (,e.g., trec_eval, qrels, etc.) are you planning to use?

- Unspecific oulines how the LTR approach will be implemented.
    - What kind of features do you want to consider? 
    - Where does the training data come from? 
    - Which classifier do you plan to use? 
    - Feature engineering requires a lot of work and careful reasoning, please pay attention that you do not waste too much time on this step

- Consider time: even though it is not a hard requirement, please think about how do you want to measure the project's progress. It will be helpful.

## Results

| Team name | A2 |
| --- | --- |
| First | 10 |
| Die Powerpuff Girls | 10 |
| TheGitGangTheory | 10 |
| def init(elynot,self,ish) | 7 |
| The Boolean Business | 7 |
| Shit happens | 9 |
| BugBustersReloaded | 10 |
| Gehacktes Misch | 8 |
| Die Drei von der Tankstelle | 10 |
| Information_Revival_Group | 10 |
| DuckDuckBros | 10 |
| The Internet Explorers | 10 |
| Searchbusters | 6 |

### First - 10 points 

+ Very good presentation style and well-structured document. The text is well written.
+ Reasonable approach and explicit goals. It will help to measure your progress over time.
+ A lot of resources are included in the footnotes in the reference section. Good "literature" research!
- Minor point: The section 2.4.1 about LTR is too unspecific. It is not entirely clear what will be done in this step. Still it is an interesting approach. Please be aware that good feature engineering might take some time.

### Die Powerpuff Girls - 10 points 

+ Very good presentation style and well-structured document. The text is well written.
+ Reasonable approach and explicit goals. 
+ Realistic goal: It is clearly outlined how the group wants to improve the recall and how it can be evaluated. The document contains detailed description regarding each (pre-)processing step.
+ The group includes relevant references in the footnotes in the reference section.

### TheGitGangTheory - 10 points

+ The concept is well written. I like the abstract.
+ Good motivation and problem identification wrt. synonyms.
+ Having read the concept, I got the impression that the group knows how to approach the problem. However, it would have been nice to include a brief outlook on the schedule until the final run submission.

### def init(elynot,self,ish) - 7 points

+ It seems like that the group wants focus on LTR approaches, which is of course an interesting approach wrt. the retrieval problem!
- However, having read the concept, it seems like that details on the LTR approach are too unspecific. What kind of features do you want to consider? Where does the training data come from (shown in the Figure on page 4)? Which classifier do you plan to use? Feature engineering requires a lot of work and careful reasoning, please pay attention that you do not waste too much time on this step
- Some questions remained open:
    - Missing details on evaluation setup. How do you plan to evaluate the experiments?
    - When do you claim your approach to be successful? Consider to mention a baseline 
    - Missing time schedule
- When you include screenshots from YouTube videos, please cite them accordingly. Likewise, make reproductions of figures more explicit.

### The Boolean Business - 7 points

- Overall, the group wants to achieve a MAP score above 0.2. I appreciate that you mention a specicifc goal, but why do want to achieve this sepcific goal? Please provide some more background.
- The report includes a idea collection, but it is not made explicit what kinds of ideas (or problems) will be adressed. It seems like that the group wants to address all of them, but that might be (1) too much and (2) too unspecific for some problems, i.e., you mention LTR but do not provdide any ideas on this.
- There is a "Goals" section, but it is not explained how the experiments are evaluated, please consider to mention tools like trec_eval or qrels. Have you made up you mind about a adequate baseline?

### Shit happens - 9 points

+ The group outlines some concrete modification of a default Solr configuration, that might lead improved retrieval effectiveness.
- When you include references, please put citation makers in the text. Otherwise, we do not know to what they refer.
- The Evaluation section is very short and unspecific. Do you want to use a baseline? How do measure improvements?
- It is unclear how the group wants to improve the ranking with LTR.

### BugBustersReloaded - 10 points 

+ I really appreciate Figure 1! Sometimes a good illustration explains more than text ever can! :) It does not only include a technical pipeline but also milestones that will help you to measure progress.
+ I have the impression that the group has a very good understanding how to approach this challenge.
- It is not clear how you want to include transformer language models. I appreciate your intentions that are in line with state-of-the-art solutions, but please be aware that these might be time-consuming, especially if you do not a very concrete idea how to implement it.

### Gehacktes Misch - 8 points

+ Overall, realistic plans, but unfortunately very unspecific.
+ Although the concept mentions some good ideas for modifications, it is not entirely clear what will be addressed.
- The concept does not address properties of the CORD19 data. It seems a little bit arbitrary.
- Please mention the author names.

### Die Drei von der Tankstelle - 10 points

+ The concept is well written.
+ It includes specific modifications regarding the normalization, query expansion, ranking methods, and the evaluation. If everything is compared and evaluated properly, I am looking forward to some interesting insights.
- Minor point: The concept does not address many properties of the CORD19 data.

### Information_Revival_Group  - 10 points

+ Good illustration of the workflow.
+ The concept mentions some details addressing some of the data-specific problems (e.g. SciSpaCy and medSpaCy or the consideration of using already existing LTR feature data).
- The evaluations could be better explained.

### DuckDuckBros - 10 points

+ The concept is straight to the point.
+ It mentions speicific details wrt. problems, approach, and how they will be evaluated. Overall, it looks promising.
- The 12 goals could have been accompanied with a rough estimation of required effort (time)

### The Internet Explorers - 10 points

+ The concept is well written and it is understandable what the group wants to do.
+ Very good timetable. Overall, the entire approach looks promising and will likely be successful
- The description of the LTR approach is rather unspecific when compared to the other workflow steps.

### Searchbusters - 6 points

+ The group includes a time schedule.
- This concept paper does not mention the CORD19 dataset or TREC Covid even once. The text is very arbitrary and the outlined problems do not address any of the obstacles that might occur when using the CORD19 datasets. Did the group look a the data?
- Some formulations are hard to understand.
- Missing details wrt. the evaluations. When do you claim success? Do you want to use a baseline? How do you measure improvements?


## Assignment III

As part of the Assignment III, every group submitted valid run files and a corresponding paper with at least two pages. All group members, who also took part in the World Café on 2022-01-14, get 30 points. Those who did not take part in the World Café and the discussions get 5 points less.


| Student ID | A3 | 
| --- | --- | 
| 11093999 | 30 | 
| 11094995 | 30 | 
| 11095449 | 25 | 
| 11096202 | 25 | 
| 11110703 | 25 | 
| 11118344 | 30 | 
| 11120099 | 25 | 
| 11121154 | 25 | 
| 11128330 | 30 | 
| 11133327 | 30 | 
| 11134199 | 30 | 
| 11134202 | 30 | 
| 11134303 | 30 | 
| 11134718 | 30 | 
| 11135533 | 30 | 
| 11136112 | 30 | 
| 11136561 | 30 | 
| 11136865 | 30 | 
| 11136973 | 30 | 
| 11139754 | 30 | 
| 11139919 | 25 | 
| 11139926 | 30 | 
| 11140076 | 25 | 
| 11140334 | 25 | 
| 11140537 | 30 | 
| 11140538 | 30 | 
| 11140540 | 30 | 
| 11140576 | 30 | 
| 11140578 | 30 | 
| 11140591 | 30 | 
| 11140612 | 30 | 
| 11140624 | 30 | 
| 11140625 | 25 | 
| 11140903 | 30 | 
| 11140904 | 25 | 
| 11140931 | 30 | 
| 11140939 | 30 | 
| 11141179 | 25 | 
| 11141352 | 30 | 
| 11141379 | 30 | 
| 11141419 | 30 | 
| 11141762 | 30 | 
| 11141763 | 25 |
| 11142356 | 30 | 
| 11142385 | 30 |
| 11142933 | 30 | 
| 11143182 | 25 | 
| 11143471 | 30 | 
| 11143680 | 30 |   
| 11143789 | 30 | 
| 11152050 | 30 | 
