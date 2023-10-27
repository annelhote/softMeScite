# SoMeSci
- [ ] SoMeSci: Annotate all contexts of Softcite anchors for implicit mentions. 
- [ ] (SoMeSci: identify further implicit mentions through heuristics based on Softcite contexts, quality issues)
- [ ] component/plugin type : compare mentions string-based in a table and look at the confusion; discuss mismatches
- [ ] merge Application and Operating System as "Software"
- [ ] Programming language type : drop "allusions", this ensures conformance with the Softcite definition, where programming language are considered as formal languages, and only annotated if used.
- [ ] Programming language type : re-annotate Prog other cases connecting them to the software.
- [ ] Drop SoMeSci co-reference type
- [ ] extension : add extension to the software name to match Softcite annotation; Regex matching
- [ ] version : SoMeSci: merge version and release
- [ ] Citation : drop SoMeSci
- [ ] Publisher : Remove the final dot
- [ ] Add identifier as a label to extend it to RRID, swMATH, and other identifiers.


# Softcite
- [ ] remove implicit mentions without an anchor (language/environment)
- [ ] Softcite: examine anchors for implicit mentions
- [ ] component/plugin type : compare mentions string-based in a table and look at the confusion; discuss mismatches
- [ ] Softcite: recode cases where an Operating System is mentioned as a version, e.g., "SPSS for Windows"; Regex Matching
- [ ] merge Environment and Software as "Software"
- [ ] Review Softcite mention context cases that are difficult, e.g., shared, but not created/used
- [ ] In software-name, separate name and abbreviation based on regexp. The abbreviation is supposed to be in brackets.
- [ ] use regex on software name to find the version (ex SPSS16)
- [ ] Add identifier as a label to extend it to RRID, swMATH, and other identifiers.