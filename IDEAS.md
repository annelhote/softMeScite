# By sementical elements

Softcite guidelines for annotations can be found here: https://github.com/softcite/softcite_dataset_v2/blob/master/annotation_guidelines_tei_xml.md.

## name

See the abbreviation section.

### SoMeSci

### Softcite

When an acronym is present, it is included in the software name.

### SoftMeScite

TBD

## software-type

This element is probably the more complicated one to match.

### SoMeSci

Here are the software types of SoMeSci : Application, Plugin, OperatingSystem, ProgrammingLanguage and CoReference.

#### Application
SPSS, Stata, SAS, SPM, Prism, STATA, ImageJ, SPSS Statistics, FSL, Excel, PLINK, MEGA, AFNI, GitHub, Statistical Package for the Social Sciences

#### Plugin
Chaste, MSM-All,IDEPI, scPipe, PyMS, glmnet, DriverNet, Bioconductor, Redirector, illuminaio, Fiji, DELLY

#### OperatingSystem
Windows, Linux, Mac, windows, Mac OS X, Macintosh, Unix, RHEL, OpenSUSE, MacOS, linux

#### ProgrammingLanguage
Matlab, RMATLAB, Python, Java, C++, Perl, C, C#, Visual Basic, Objective-C, JavaScript, IDL, Fortran

### Softcite

Here are the software types of Softcite : environment, component, implicit and software.

#### environment
SPSS, SAS, R, Stata, MATLAB, STATA, GraphPad

#### component
limma, Limma, caret, rms, PanelWhiz, Materials Studio Modules, seriation, glamm, mi, proCIs

#### implicit
script, scripts, code, program, software, library, programs, routine, routines, module

#### software
ImageJ, Mobyle, MUMMALS, Excel, AURIN, BLAST, ProbCons, PlatProm, OnlineTED, pFlexAna

### SoftMeScite
* SoMeSci Application should match Softcite Software: Compare lists and see overlap.
* SoMeSci OperatingSystems and ProgrammingLanguage should match Softcite environment: Compare lists and see overlap.
* SoMeSci Component should match Softcite Plugin: Compare lists and see overlap.
* Softcite implicit -> no match in SoMeSci (Re-examine Programming Languages, Re-examine URL mentions without software mentions, to update them in SoMeSci) or throw it away ?

#### Implicit mentions
- Softcite: remove implicit mentions without an anchor (language/environment)
- Softcite: examine anchors 
- SoMeSci: Annotate all contexts of Softcite anchors for implicit mentions. 
- (SoMeSci: identify further implicit mentions through heuristics based on Softcite contexts, quality issues)

#### Component/PlugIn
- Definition: not a standalone software
- Name: use sub-component to express the dependence on other software 
- Softcite+SoMeSci: compare mentions string-based in a table and look at the confusion; discuss mismatches
- Known mismatches: Bioconductor, Fiji 

#### Operating Systems
- Softcite: recode cases where an Operating System is mentioned as a version, e.g., "SPSS for Windows"; Regex Matching

#### Software Merge
- Define overlapping categories:
- SoMeSci: merge Application and Operating System as "Software"
- Softcite: merge Environment and Software as "Software"

#### Programming Languages
- SoMeSci: drop "allusions", this ensures conformance with the Softcite definition, where programming language are considered as formal languages, and only annotated if used. 
- SoMeSci: Re-annotate Prog other cases connecting them to the software.

#### Co-Reference
- Drop SoMeSci co-reference

#### Extension 
- SoMeSci: add extension to the software name to match Softcite annotation; Regex matching

#### Packages
- Softcite: Re-examine contexts of R and Python to adjust sub-component annotation

#### Annotation
- Setup annotation configuration for new scheme

## version

### SoMeSci

SoMeSci has version, release and extension.

### Softcite

Softcite has only a version element that catch the version number or the date string. If any prefix like "version", "v" or "v.", it is not included.

### SoftMeScite

The SoMeSci should probably concat version and release.
SoMeSci: merge version and release

## mention-type

### SoMeSci

SoMesci mentions type is mono valuated among allusion, usage, creation and deposition. One mention implicitly suggest that the previous types are true eg. deposition creations means usage and creation, deposition means usage, creation and deposition …

### Softcite

Softcite uses cumulative mentions : used, created and shared. If none of them are present, it should probably match with the “Allusion” mention type of SoMeSci. If multiple types are present, probably the last one between used, created and shared should be kept.

### SoftMeScite

We should probably keep the multi valuated from Softcite and the Allusion from SoMeSci

Take SoMeSci labels, Review Softcite cases that are difficult, e.g., shared, but not created/used

## url

Direct match between SoMeSci url and Softcite url

## Citation / Reference

### SoMeSci

SoMesci has a Citation entry.

### Softcite

Softcite has bibliographical reference callout "bibr".

### SoftMeScite

Softcite needs curation, drop SoMeSci in the meantime.
Softcite would need manual annotation about citations.

# By annotation Difference 

## Developer/Publisher Boundary 

"We used SPSS (IBM Inc.)."

### SoMeSci

Developer: "IBM Inc."

### Softcite

Developer: "IBM Inc"

### SoftMeScite

- SoMeSci: Remove the dot; Regex adjustment 

## Name Abbreviation/Alternative

"We used Statistical Package for the Social Sciences (SPSS) for analysis."

### SoMeSci

Software: Statistical Package for the Social Sciences
Abbreviation: SPSS

### SoftCite

Software: Statistical Package for the Social Sciences (SPSS)

### SoftMeScite

Regex adjustment : Split it up in softcite

## Graphpad Prism (Developer/Publisher + Software)

"We used Graphpad Prism."

### SoMeSci

Software: Prism
Developer: Graphpad

### SoftCite

Software: Graphpad Prism

### SoftMeScite

- Due to ambiguity with other software the name was changed to "GraphPad Prism" by the publisher. 
- SoMeSci: adjust annotation to include "Graphpad" in the software name (Regex matching) 

## Software with merged Version

"We used SPSS16."

### SoMeSci

Software: SPSS
Version: 16

### SoftCite

Software: SPSS16

### SoftMeScite

- SoftCite: re-annotation based on regex matching strings ending in digits.  
- Manual examination is required as this is not generally true for all software. There is software, where the number at the end is not the version, but actually a part of the name.

## Package/PlugIn descriptions

"We used R package lme4."

### SoMeSci

Software: "R" (Programming Environment)
Software: "lme4" (PlugIn)

### SoftCite

Software: "R package lme4"

### SoftMeScite

Softcite: re-examine contexts of R and Python for package mentions and manually update them; Regex matching needed to identify them.  

## Identifier 

Add identifier as a label to extend it to RRID, swMATH, and other identifiers.
