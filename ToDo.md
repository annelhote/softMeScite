SoMeSci categories are in _italics_
SoftCite categories are in **bold**
Merged Categories are in _**both**_

# Merges and Drops

| SoMeSci                                  | Merged Label        | SoftCite                             |
| ---                                      | ---                 | ---                                  |
| _Application_ and _Operating System_     | _**Software**_      | **Environment** and **Software**     |
| _PlugIn_                                 | _**subComponent**_  | **Component**                        |
|   _co-reference_                         | ø                   | ø                                    |
| Programming Langauge                     | ??                  | language                             |
| Abbreviation / Alternative name          |                     |                                      |
| Version                                  |                     |                                      |
| release                                  |                     |                                      |
| extension                                |                     |                                      |
| Developer                                | ??                  | Publisher                            |
| URL                                      | URL                 | URL                                  |
| Citation                                 | ø                   | ø                                    |
| License                                  | ø                   | ø                                    |
| _MentionType_ = _allusions_              | notUsedCreatedShared | (implicitly exists)                 |
| _MentionType_ = _usage_                  | Used               | MentionContextAttribute = used       |
| _MentionType_ = _Creation_               | Created            | MentionContextAttribute = created    |
| _MentionType_ = _Deposition_             | MadePublic         | MentionContextAttribute = shared     |

# SoMeSci
- [ ] 1. Annotate all contexts of Softcite anchors for **implicit** mentions.
- [ ] 2. (SoMeSci: identify further implicit mentions through heuristics based on Softcite contexts, quality issues)
- [ ] 3. **component**/_plugin_ type : compare mentions string-based in a table and look at the confusion; discuss mismatches
- [ ] 4. merge _Application_ and _Operating System_ as _**Software**_
- [ ] 6. _Programming language_ : re-annotate Prog other cases connecting them to the software.
- [ ] 7. _Programming language_ : drop (_MentionType_ = _allusions_)

  This ensures conformance with the Softcite definition, where programming **language** are considered as formal languages, and only annotated if used.
- [ ] 8. _co-reference_ : Drop _co-reference_ type

_co-reference_ is not coded in Softcite, and it was not considered useful to code it for the combined dataset
  
- [ ] 9. _extension_ : add extension to the software name to match Softcite annotation (*version*)

 Use regex matching. i.e., add _extension_ to _Application_, _PlugIn_, _Operating System_, or _Programming Lang_ (software type _co-reference_ is dropped)

- [ ] 10. _version_ : SoMeSci: merge _version_ and _release_ in single category _*version*_
- [ ] 11. _Citation_ : drop _Citation_
      
  _Citation_ is only captured in SoMeSci and not at all in SoftCite. For this reason, it is dropped in the merged version

- [ ] 12. _Publisher_ : Remove the final dot

Many publishers have a dot in the name. e.g., "IBM llc.". SoftCite doesn't capture the full stop/period, so to normalise, this will not be part of the annotation.

- [ ] 13. Add identifier as a label to extend it to RRID, swMATH, and other identifiers.

Inline citations of identifiers for software are not captured by either dataset. Inline citation identifiers are usually domain specific identifier schemes like RRID, but there may be others that are not being captured at all. Note also that in some domains, this detail may be captured in supplmentary materials, e.g., as a "Resources" or "Software Resources" table.   


# Softcite
- [ ] 14. remove **implicit** mentions without an anchor (language/environment)

i.e., remove "the [code] is available on request"

- [ ] 15. Softcite: examine anchors for implicit mentions

i.e., look for things like "the \[analysis\](**implicit**) was done using the \[R\](**language**) language, and retain in the merged set if a corresponding action in SoMeSci occurs to label the combined _**implicit**_ label
 
- [ ] 16. **component**/_plugin_ type : compare mentions string-based in a table and look at the confusion; discuss mismatches
- [ ] 17. recode cases where an _Operating System_ is mentioned as a **version**, e.g., "SPSS for Windows"; Regex Matching
- [ ] 18. merge **Environment** and **Software** as new merged category _**Software**_
- [ ] 19. Review Softcite **mention** context cases that are difficult, e.g., shared, but not created/used
- [ ] 20. Extract a new category for SoftCite: _**abbrevation**_

  In **software-name**, separate **name** from _**abbreviation**_ based on regexp. The abbreviation is supposed to be in brackets. e.g., "...we used \[Statistical Package for the Social Sciences (SPSS)\](**software-name**) to analyse..." should be split into \[Statistical Package for the Social Sciences\] (\[SPSS\](_**abbreviation**_)

- [ ] 21. use regex on software name to find the _**version**_ within the name token (ex SPSS16)

SoMeSci separates this out and labels is separately, while Softcite doesn't. For consistency, this must be extracted in the SoftCite dataset.

- [ ] 22. Add identifier as a label to extend it to RRID, swMATH, and other identifiers.

Identifiers is not coded in either dataset. (see item 12)

# Extension
- [ ] 23. Match RRID to PMC OA and extract sections mentioning the RRID software
- [ ] 24. Setup Inter Annotator Agreement assessment for application of new data scheme 
- [ ] 25. Annotate RRID artcile paragraphs based on merged scheme 
- [ ] 26. Add further RRID paragraphs based on PDFs publications
