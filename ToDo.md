# SoMeSci
- [ ] 1. SoMeSci: Annotate all contexts of Softcite anchors for implicit mentions. 
- [ ] 2. (SoMeSci: identify further implicit mentions through heuristics based on Softcite contexts, quality issues)
- [ ] 3. component/plugin type : compare mentions string-based in a table and look at the confusion; discuss mismatches
- [ ] 4. merge Application and Operating System as "Software"
- [ ] 5. Programming language type : drop "allusions", this ensures conformance with the Softcite definition, where programming language are considered as formal languages, and only annotated if used.
- [ ] 6. Programming language type : re-annotate Prog other cases connecting them to the software.
- [ ] 7. Drop SoMeSci co-reference type
- [ ] 8. extension : add extension to the software name to match Softcite annotation; Regex matching
- [ ] 9. version : SoMeSci: merge version and release
- [ ] 10. Citation : drop SoMeSci
- [ ] 11. Publisher : Remove the final dot
- [ ] 12. Add identifier as a label to extend it to RRID, swMATH, and other identifiers.


# Softcite
- [ ] 13. remove implicit mentions without an anchor (language/environment)
- [ ] 14. Softcite: examine anchors for implicit mentions
- [ ] 15. component/plugin type : compare mentions string-based in a table and look at the confusion; discuss mismatches
- [ ] 16. Softcite: recode cases where an Operating System is mentioned as a version, e.g., "SPSS for Windows"; Regex Matching
- [ ] 17. merge Environment and Software as "Software"
- [ ] 18. Review Softcite mention context cases that are difficult, e.g., shared, but not created/used
- [ ] 19. In software-name, separate name and abbreviation based on regexp. The abbreviation is supposed to be in brackets.
- [ ] 20. use regex on software name to find the version (ex SPSS16)
- [ ] 21. Add identifier as a label to extend it to RRID, swMATH, and other identifiers.

# Extension
- [] 22. Match RRID to PMC OA and extract sections mentioning the RRID software
- [] 23. Setup Inter Annotator Agreement assessment for application of new data scheme 
- [] 24. Annotate RRID artcile paragraphs based on merged scheme 
- [] 25. Add further RRID paragraphs based on PDFs publications 