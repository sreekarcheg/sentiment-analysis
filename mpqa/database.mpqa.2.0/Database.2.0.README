===========================================================

   Documentation for MPQA Opinion Corpus version 2.0

===========================================================

Contents:

  1. Introduction

  2. Overview of Changes

     2.1 Additional data
     2.2 Addition of attitude and target annotations
     2.3 Removal of exploratory attributes
     2.4 Addition of OpQA answer annotations
     2.5 Refinement of some annotations

  3. Data 

     3.1 MPQA original subset
     3.2 OpQA subset
     3.3 XBank subset
     3.4 ULA subset
     3.5 ULA-LU subset

  4. MPQA Annotation Scheme

     4.1 agent
     4.2 expressive-subjectivity
     4.3 direct-subjective
     4.4 objective-speech-event
     4.5 attitude
     4.6 target
     4.7 inside

  5. Subjective Sentences

  6. OpQA Answer Annotations

  7. Database Structure

     7.1 database/docs
     7.2 database/meta_anns
     7.3 database/man_anns

  8. MPQA Annotation Format

  9. Acknowledgements

 10. Contact Information

 11. References

-----------------------------------------------------------

1. Introduction  

This corpus contains news articles and other text documents
manually annotated for opinions and other private states
(i.e., beliefs, emotions, sentiments, speculations, etc.).  

The main changes in this version of the MPQA Corpus are the
addition of new attitude and target annotations, the inclusion
of answer annotations for the OpQA subset of the corpus, and
the addition of new annotated documents, growing the size of 
the corpus to 692 documents.  These changes are described in
more detail in the following section.

The previous version of the MPQA Corpus was released with
two different versions of the terminology used to describe
the MPQA annotation scheme.  For this version of the corpus,
only the newer terminology (LRE) from (Wiebe, Wilson, and Cardie, 
2005) is used. 

-----------------------------------------------------------

2. Overview of Changes

2.1 Additional data

This release contains an additional 157 annotated documents.
The new documents come from Xbank (85 Wall Street Journal texts), 
the ULA (48 texts from the American National Corpus), and the
ULA-LU (24 texts from the ULA language understanding subcorpus.

These additional documents are annotated with the full MPQA
annotation scheme, including attitudes and targets.

2.2 Addition of attitude and target annotations

The MPQA annotation scheme has been extended to include two
new types of annotations: attitude annotations and target
annotations - The new annotations are described in 
Theresa Wilson's Dissertation (Wilson, 2008). The related 
chapter can be found in the release: TAWilsonDissertationCh7Attitudes.pdf.


As an overview, the attitude annotations aim to capture the attitudes, e.g., 
positive sentiments, negative sentiments, agreements, negative 
arguings, etc., being expressed overall by the private states 
represented by the direct subjective annotations.  To capture
the relationship between attitudes and direct subjective 
annotations, a new attribute has been added to the direct 
subjective annotations: the attitude-link attribute.  The 
attitude-link indicates which attitude is associated with 
which direct subjective annotation. 

The target annotations aim to capture what each attitude
is about, e.g., what the sentiment is about, what is being
argued about, etc.  Just as the attitude annotations are
linked to the direct subjective annotations using the
attitude-link attribute, the target annotations are linked
to the attitude annotations using the target-link attribute.

The 157 new documents and 349 documents from the original 
MPQA Corpus have the new attitude and target annotations.

2.3 Removal of exploratory attributes

In the original MPQA annotation scheme, some exploratory
attributes were included to capture some attitude and target 
information.  These attributes were:

  - agent annotation -> nested-target attribute
  - direct subjective annotation -> attitude-type attribute
  - direct subjective annotation -> attitude-toward attribute

The new attitude and target annotations replace these 
earlier, exploratory annotations, so for this release,
these attributes have been removed.

2.4 OpQA Corpus subset

The OpQA Corpus is a 98 document subset of the original MPQA 
Corpus.  In work by Stoyanov, Cardie, and Wiebe (2005), these
documents were annotated for answers to a small set of fact
and opinion questions.  These answer annotations are included
in this release.

2.5 Refinement of some annotations

As part of annotating attitudes and targets, refinements
were made to some of the existing annotations.  These 
refinements include changing the annotation span boundaries, 
changing intensity and polarity attributes, and in a few cases, 
removing annotations, adding new annotations, or changing a
direct subjective annotation to an objective speech annotation
(or vice versa).  

-----------------------------------------------------------

3. Data

This release of the corpus contains 692 documents, a total of 
15802 sentences.  

There are 5 different sets of documents:

1. MPQA original subset
2. OpQA (Opinion Question Answering) subset
3. XBank
4. ULA (Unified Linguistic Annotation)
5. ULA-LU (Language Understanding subcorpus)

The Xbank, ULA, and ULA-LU data as well as some documents of 
the original 535-document release carry attitude and target
annotations following the scheme described below in section 4. 
This set of documents is listed in the file doclist.attitudeSubset.

For the documents of the original MPQA corpus (see section 3.1), 
an assignment to topic categories is available but not for any 
of the other data sets.

3.1 MPQA original subset

The documents in the MPQA original subset are listed in the 
file: doclist.mpqaOriginalSubset.

These articles are from 187 different foreign and U.S. news 
sources.  They date from June 2001 to May 2002.  They were 
identified by human searches and by an information retrieval 
system.  The majority of the articles are on 10 different topics, 
but a number of additional articles were randomly selected 
(more or less) from a larger corpus of 270,000 documents.  
This last set of articles has topic: misc.

The 10 topics are:

   argentina: economic collapse in Argentina
   axisofevil: reaction to President Bush's 2002 State of the Union Address
   guantanamo: U.S. holding prisoners in Guantanamo Bay
   humanrights: reaction to U.S. State Department report on human rights
   kyoto: ratification of Kyoto Protocol
   mugabe: 2002 presidential election in Zimbabwe
   settlements: Israeli settlements in Gaza and West Bank
   spacestation: space missions of various countries
   taiwan: relations between Taiwan and China
   venezuela: presidential coup in Venezuela

The file, doclist.mpqaOriginalByTopic, gives the topic for
each document.

3.2 OpQA subset

The documents in the OpQA subset are listed in the 
file: doclist.opqaSubset.

This section of the corpus consists of a set of 98 documents 
from the original 535-document MPQA Corpus.  These documents
were annotated for the research on Opinion Question Answering 
presented in Stoyanov, Cardie, and Wiebe (2005).  Text segments
that contributed answers to each of 30 question, 1/2 fact-based
and 1/2 opinion-based, are annotated.

3.3 XBank

The documents in the Xbank subset are listed in the
file: doclist.xbankSubset.

The Xbank subset contains 85 Wall Street Journal texts from the
Penn TreeBank.  They were annotated for inclusion in the Xbank, 
which is a simple tree-based merger of PropBank, NomBank, 
the Discourse TreeBank, and TimeBank annotations.

For more information on XBank and the additional annotations
available on this data, please visit:
http://www.cs.brandeis.edu/~marc/ula/xbank-browser/.

3.4 ULA

The documents in the ULA subset are listed in the 
file: doclist.ulaSubset.

The ULA-OANC-1 corpus is a 40K-word subcorpus of the
American National Corpus (ANC).  The documents in the
subcorpus were chosen to be representative of the open 
portion of the ANC.  

There are 48 documents in this set, falling into 6 categories:

travel guides
transcriptions of spoken conversation
fundraising letters
a chapter of the 9/11 report
a chapter from a linguistics textbook
articles from Slate magazine

All documents in ULA-OANC-1 corpus have been annotated 
by participants of the Unified Linguistic Annotation project. 
In additional to the MPQA annotations, the following annotations
are available on this data: PropBank, NomBank, PennTreebank, 
TimeBank, Penn Discourse Treebank, WordNet senses and 
FrameNet frames.

For more information on the ULA-OANC corpus and the additional
annotations available on this data, please visit:
http://nlp.cs.nyu.edu/wiki/corpuswg/ULA-OANC-1.

3.5 The ULA language understanding subcorpus (ULA-LU)

The documents in the ULA-LU subset are listed in the
file: doclist.ula-luSubset.

There are 24 documents in this set, falling into these main categories:

emails related to the enron case
spoken language transcripts
newswire text
wall street journal texts (from Penn TreeBank)
translations of Arabic source texts

-----------------------------------------------------------

4. MPQA Annotation Scheme

This section contains an overview of the types of annotations 
that you will see marked in the documents of this corpus.  
For more details on the MPQA annotations see the instructions
available here: 
http://www.cs.pitt.edu/~wiebe/pubs/pub1.html (original MPQA scheme) 
and http://homepages.inf.ed.ac.uk/twilson/attitude-instructions.pdf

4.1 agent annotation 

    Marks phrases that refer to sources of private states
    and speech events, or phrases that refer to agents who 
    are targets of an attitude.

    Possible attributes:
        id - Unique identifier assigned by the annotator to
             the first meaningful and descriptive reference
             to an agent.

             There are two agent annotations with a 0,0
             byte span in every document.  These two
             annotations are to give an id for the writer
             of the document ('w') and for an implicit
             agent ('implicit').  Private states and
             speech events are sometimes attributed to
             implicit agents.

        nested-source - Used when the agent reference is 
             the source of a private state/speech event. 
             The nested-source is a list of agent ids 
             beginning with the writer and ending with 
             the id for the immediate agent being referenced.

             Example:  w, Foreign Ministry, US State Dept

        agent-uncertain - Used when the annotator is 
             uncertain whether the agent is the correct
             source of a private state/speech event

             Possible values: somewhat-uncertain, very-uncertain

4.2 expressive-subjectivity annotation

    Marks expressive-subjective elements, words and phrases 
    that indirectly express a private state.  For example, 
    'fraud' and 'daylight robbery' in the following sentence 
    are expressive-subjective elements.

    "We foresaw electoral fraud but not daylight robbery,"
    Tsvangirai said.

    Possible attributes:
        nested-source - List of agent ids beginning with
             the writer and ending with the id for the 
             immediate agent that is the source of the 
             private state being expressed by the
             expressive-subjective element.

        nested-source-uncertain - Used when an annotator
             is uncertain as to whether the agent is
             the correct nested source.

             Possible values: somewhat-uncertain, very-uncertain

        intensity - Indicates the intensity of private state being
             expressed by the expressive-subjective element.

             Possible values: low, medium, high, extreme

        polarity - Indicates the contextual polarity of the
             private state.

             Possible values: positive, negative, both, neutral,
                uncertain-positive, uncertain-negative, uncertain-both,
                uncertain-neutral

4.3 direct-subjective annotation

    Marks direct mentions of private states and speech
    events (spoken or written) expressing private states.

    Possible attributes:
        nested-source - List of agent ids, beginning with
             the writer and ending with the id for the
             immediate agent that is the source of the
             private state or speech event.

        annotation-uncertain - Used when an annotator is uncertain
             as to whether the expression marked is indeed
             a direct private state or a speech event.

             Possible values: somewhat-uncertain, very-uncertain

        implicit - The presence of this attribute indicates
             that the speech event is implicit.  This attribute
             is used when there is not a private state or speech
             event phrase on which to actually make an annotation.
             For example, there is no phrase "I write" for the
             writer of the sentence.

        subjective-uncertain - Used when an annotator is
             uncertain as to whether a private state is
             being expressed.

             Possible values: somewhat-uncertain, very-uncertain

        intensity - Indicates the overall intensity of the private 
             state being expressed, considering the 'direct-subjective' 
             phrase and everything inside its scope.

             Possible values: low, medium, high, extreme

        expression-intensity - Indicates the intensity of the 
             speech event or private state expression itself. 
 
             Possible values: neutral, low, medium, high, extreme

        polarity - Indicates the contextual polarity of the
             private state.  Only included when expression-intensity
             is not neutral.

             Possible values: positive, negative, both, neutral,
                uncertain-positive, uncertain-negative, uncertain-both,
                uncertain-neutral

        attitude-link - Id of attitude annotation(s) that are linked
             to this direct-subjective annotation.  If there is more
             than one linked attitude, this is represented as a comma-
             separated list of attitude ids.

        insubstantial - Used when the private state or
             speech event is not substantial in the discourse

             Possible values are combination of: c1, c2, c3

             These possible values correspond to criteria 
             necessary for a private state or speech event to 
             be substantial.  Please see the annotation
             instructions for a complete description of these
             criteria.  The criteria listed for this attribute
             are the criteria that the private state or speech
             speech event fails to meet.

4.4 objective-speech-event annotation

    Marks speech events that do not express private states.

    Possible attributes:
        nested-source - List of agent ids, beginning with
             the writer and ending with the id for the
             immediate agent that is the source of the
             private state or speech event.

        annotation-uncertain - Used when an annotator is uncertain
             as to whether the expression marked is indeed
             a speech event.

             Possible values: somewhat-uncertain, very-uncertain

        implicit - The presence of this attribute indicates
             that the speech event is implicit.  This attribute
             is used when there is not a speech event phrase 
             on which to actually make an annotation.
             For example, there is no phrase "I write" for the
             writer of the sentence.

        objective-uncertain - Used when an annotator is
             uncertain as to whether the speech event is objective.

             Possible values: somewhat-uncertain, very-uncertain

        insubstantial - Used when the speech event is not
             substantial in the discourse

             Possible values are combination of: c1, c2, c3

             These possible values correspond to criteria 
             necessary for a private state or speech event to 
             be substantial.  Please see the annotation 
             instructions for a complete description of these 
	     criteria.  The criteria listed for this attribute 
             are the criteria that the private state or speech 
             event fails to meet.

4.5 attitude annotation

    Marks the attitudes that compose the expressed private states.

    Possible attributes:
        id - Identifier assigned to the attitude annotation, 
             typically beginning with an 'a' followed by a number.

        attitude-type - Type of attitude

             Possible values:
		positive sentiment	negative sentiment
		positive arguing	negative arguing
		positive agreement	negative agreement (disagreement)
                positive intention	negative intention
		speculation
		other-attitude

        attitude-uncertain - Used when an annotator is uncertain
             about the type of attitude, or whether the attitude
             should be marked.

             Possible values: somewhat-uncertain, very-uncertain

        target-link - Id of target annotation(s) that are linked
             to this attitude annotation.  If there is more than
             than one linked target, this is represented as a comma-
             separated list of target ids.  If the attitude does
             not have a target (or the target is unmarkable), this
             attribute has the value 'none'.

        inferred - Used when a fairly prominent attitude can be
             inferred.  For example, in the sentence below, the
             most prominent attitude is a positive sentiment being 
             expressed by the people toward the fall of Chavez.  
             However, there is also clearly a negative attitude
             negative attitude toward Chavez that can be inferred.

             Example: People are happy because Chavez has fallen.

4.6 target annotation

    Marks the targets of the attitudes, i.e., what the attitudes
    are about or what the attitudes are directed toward. 

    Possible attributes:
        id - Identifier assigned to the target annotation, 
             typically beginning with an 't' followed by a number.

        target-uncertain - Used when an annotator is uncertain
             about whether this is the correct target for the
             attitude.

             Possible values: somewhat-uncertain, very-uncertain

4.7 inside annotation

    The term 'inside' refers to the words inside the scope 
    of a direct private state or speech event phrase ('on').  
    The annotators did not mark 'inside' annotations.  
    However, 'inside' annotations were created automatically 
    for each writer 'on' annotation.  Each writer 'inside' 
    corresponds to a GATE sentence.

-----------------------------------------------------------

5. Subjective Sentences

The annotations described in section 4 are expression-
level annotations, performed below the level of the 
sentence.  We ask annotators to identify all subjective
expressions in a sentence, which gives us very 
fine-grained, detailed annotations.  Although the
annotators sometimes differ over which particular 
expressions are subjective, and how many subjective
expressions are in a sentence, they have very good
agreement as to whether there is subjectivity in a
sentence (see (Wiebe, Wilson, Cardie (2005)).

For the work using this data that appeared in CoNLL03
(Riloff et al., 2003) and EMNLP03 (Riloff & Wiebe, 2003)
the following definition of a subjective sentence was
used.  The definition is in terms of the annotations.

A sentence was considered subjective if 1 OR 2:
  1. the sentence contains a "GATE_direct-subjective" 
     annotation WITH attribute intensity NOT IN ['low', 'neutral'] 
     AND NOT WITH attribute insubstantial.

  2. the sentence contains a "GATE_expressive-subjectivity"
     annotation WITH attribute intensity NOT IN ['low']

Otherwise, a sentence was considered objective.

The file, test_setCoNLL03, contains the list of files
used for evaluation in (Riloff et al, 2003).

NOTE: Since the experiments performed in (Riloff et al., 
2003) and (Riloff & Wiebe, 2003), some annotation errors 
and errors in the sentence splits have been corrected,
and some annotations have been refined. 

-----------------------------------------------------------

6. OpQA Answer Annotations

This section contains an overview of the answer annotations
marked in the OpQA subset.  For more details on the OpQA
answer annotations see the instructions available here:
http://www.cs.cornell.edu/~ves/Publications/MPQA_annot_instr.pdf

Each answer annotation marks a text segment that contributes
(or partially contributes) an answer to one of 30 different fact 
or opinion questions.  These questions can be found in the 
file: opqa-questions.

The answer annotations have the following attributes:

a. annotator - the annotator who provided the given annotation

b. topic - topic of the question being answered (see opqa-questions)

c. questionnumber - within the topic, the number of the question 
                    being answered (see opqa-questions)

d. confidence - value ranging from 1 to 5 expressing the annotator's
                confidence that the segment answers the question

e. confidencecomment - optional comment given by annotator

f. partial - true or false, used to indicate whether the segment
             is only a partial answer to the question

-----------------------------------------------------------

7. Database Structure

The database/ contains three subdirectories: docs, meta_anns, man_anns.
Each subdirectory has the following structure:
	
		        subdir
		       /      \
		  parent  ..  parent
		 /     \          
	  docleaf  ...  docleaf

Within each subdirectory, each document is uniquely identified 
by its parent/docleaf.  For example, 20010927/23.18.15-25073, 
identifies one document.  20010927 is the parent; 23.18.15-25073 
is the docleaf.

7.1 database/docs

    The docs subdirectory contains the document collection.  
    In this subdirectory, each docleaf (e.g., 23.18.15-25073) 
    is a text file containing one document.

7.2 database/meta_anns

    Each docleaf (e.g., 23.18.15-25073) in the meta_anns 
    subdirectory contains information about the document 
    (e.g., source, date).  The meta_anns files are in MPQA 
    format, which is described in section 8. All the documents
    in the MPQA original subset have corresponding meta_anns 
    files except the following five documents: 20020516/22.23.24-9583, 
    20020517/22.08.22-24562, 20020521/22.21.24-5526, 
    20020522/22.34.49-13286, and 20020523/22.37.46-10374.
    
7.3 database/man_anns

    This subdirectory contains the manual annotations for 
    the documents.  In this subdirectory, each docleaf 
    (23.18.15-25073) is a directory that contains two or 
    three files: gateman.mpqa.lre.2.0, gatesentences.mpqa.2.0,
    and for those documents that are part of the OpQA corpus
    subset, answer.mpqa.2.0.

    The file gateman.mpqa.lre.2.0 contains the human opinion 
    annotations, including the new attitude and target annotations
    (Wilson, 2008) for those documents that have been annotated
    for attitudes and targets.  The file gatesentences.mpqa.2.0 
    contains spans for sentence, minus junk sentences that
    contain meta data or other spurious information that was
    not part of the article.  These junk sentences were 
    removed by hand.

    All of these files, gateman.mpqa.lre.2.0, gatesentences.mpqa.2.0,
    and answer.mpqa.2.0, are in MPQA format, described in section 8.

-----------------------------------------------------------

8. MPQA Annotation Format

The MPQA format is a type of general stand-off annotation.  
Every line in an annotation file is either a comment line 
(beginning with a '#") or an annotation line (one annotation 
per line).  

An MPQA annotation line consists of text fields separated by a
single TAB.  The fields used are listed below, with an example 
annotation underneath.

id	span	data_type	ann_type	attributes
58      730,740 string  	GATE_agent      nested-source="w,chinarep"

Every annotation has a identifier, id.  This id is unique ONLY 
within a given MPQA annotation file. 

The span is the starting and ending byte of the annotation in 
the document.  For example, the annotation listed above is from 
the document, temp_fbis/20.20.10-3414.  The span of this annotation 
is 730,740.  This means that the start of this annotation is 
byte 730 in the file docs/temp_fbis/20.20.10-3414, and byte 740 
is the character after the last character of the annotation.

     blah, blah, blah, example annotation, blah, blah, blah
                       |                 |
                  start byte          end byte

The data_type of all annotations should be 'string'.

The types of annotations in the gateman.mpqa files are 
GATE_agent, GATE_expressive-subjectivity, GATE_direct-subjective, 
GATE_objective-speech-event, GATE_attitude, GATE_target, GATE_inside, 
and GATE_split.  With the exception of GATE_split, these annotation 
types correspond to the annotation types described in section 4.  

Sentence annotations in the gatesentence.mpqa.2.0 files have 
type GATE_sentence.

The annotations in the answer.mpqa.2.0 files all are of
type 'answer'.

Each attribute is an attribute_name="attribute_value" pair.  
An annotation may have any number of attributes, including 
0 attributes.  Multiple attributes for an annotation are 
separated by single spaces, and they may be listed in any 
order.  The attributes that an annotation may have depends 
on the type of annotation.  The set of possible attributes 
for each MPQA annotation type is listed in section 4.  The
set of possible attributes for the OpQA answer annotations
are listed in section 6.

-----------------------------------------------------------

9. Acknowledgements

The development of the MPQA Opinion Corpus version 1.0 
was performed in support of the Northeast Regional Research 
Center (NRRC) which is sponsored by the Advanced Research 
and Development Activity (ARDA), a U.S. Government entity 
which sponsors and promotes research of import to the 
Intelligence Community which includes but is not limited 
to the CIA, DIA, NSA, NIMA, and NRO.

The development of version 1.2 was supported in part by the 
NSF under grant IIS-0208798 and by the Advanced Research 
and Development Activity (ARDA).

The development of version 2.0 was supported in part by an
Andrew Mellow Pre-doctoral Fellowship, Department of Homeland Security
Grant N0014-07-1-0152, and National Science Foundation grant
CNS-0551615. 

-----------------------------------------------------------

10. Contact Information

Please direct any questions that you have about this corpus or
the annotation scheme to Janyce Wiebe at the University of
Pittsburgh.

Theresa Wilson  email: twilson@inf.ed.ac.uk
Janyce Wiebe 	email: wiebe@cs.pitt.edu


-----------------------------------------------------------

11. References

Janyce Wiebe, Eric Breck, Chris Buckley, Claire Cardie, 
  Paul Davis, Bruce Fraser, Diane Litman, David Pierce, 
  Ellen Riloff, Theresa Wilson, David Day, Mark Maybury 
  (2003). REcognizing and Organizing Opinions Expressed in 
  the World Press. 2003 AAAI Spring Symposium on New 
  Directions in Question Answering.

Theresa Wilson and Janyce Wiebe (2003). Annotating Opinions 
  in the World Press. 4th SIGdial Workshop on Discourse and 
  Dialogue (SIG0dial-03). ACL SIGdial.

Ellen Riloff, Janyce Wiebe, and Theresa Wilson (2003). 
  Learning Subjective Nouns Using Extraction Pattern 
  Bootstrapping. Seventh Conference on Natural Language
  Learning (CoNLL-03). ACL SIGNLL.

Ellen Riloff and Janyce Wiebe (2003). Learning Extraction
  Patterns for Subjective Expressions. Conference on 
  Empirical Methods in Natural Language Processing (EMNLP-03).
  ACL SIGDAT.

Veselin Stoyanov, Claire Cardie, and Janyce Wiebe (2005). 
Multi-Perspective Question Answering Using the OpQA Corpus.
  Human Language Technologies Conference/Conference on
  Empirical Methods in Natural Language Processing.

Janyce Wiebe, Theresa Wilson, and Claire Cardie (2005).
  Annotating expressions of opinions and emotions in language. 
  Language Resources and Evaluation (formerly Computers and 
  the Humanities) 1(2).

Theresa Wilson, Janyce Wiebe, and Paul Hoffman (2005).
  Recognizing Contextual Polarity in Phrase-Level Sentiment 
  Analysis. Proceedings of HLT/EMNLP 2005, Vancouver, Canada.

Theresa Wilson (2008). Fine-grained Subjectivity and Sentiment
  Analysis: Recognizing the intensity, polarity, and attitudes
  of private states, Chapter 7, "Representing Attitudes and
  Targets".  Ph.D. Dissertation, University of Pittsburgh.

-----------------------------------------------------------

Theresa Wilson
Josef Ruppenhofer
Janyce Wiebe

version 2.0  
last modified 12/10/08
