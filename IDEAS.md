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
Statistical Package for the Social Sciences, GitHub, AFNI, MEGA, PLINK, Excel, FSL, SPSS Statistics, ImageJ, STATA, Prism, SPM, SAS, Stata, SPSS

#### Plugin
DELLY, Fiji, illuminaio, Redirector, Bioconductor, DriverNet, glmnet, PyMS, scPipe, IDEPI, MSM-All, Chaste

#### OperatingSystem
linux, MacOS, OpenSUSE, RHEL, Unix, Macintosh, Mac OS X, windows, Mac, Linux, Windows

#### ProgrammingLanguage
Fortran, IDL, JavaScript, Objective-C, Visual Basic, C#, C, Perl, C++, Java, Python, Matlab, MATLAB, R

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

For now: when someone is interested in implicit mentions Softcite has to be used; SoMeSci could be updated with silver standard data through heuristics 

Subcomponent: not a standalone software
Component matches PlugIn: There is further need for discussion on Bioconductor. 
There are probably mismatches: Fiji. 
Compare complete set of labels 
Manually inspect intersection to find out mismatch
confusion matrix based on string table 

Operating system recode in context "SPSS for Windows". (regex)
Otherwise model: SoMeSci Application + Operating Sytem = Softcite Environment + software 
We drop SoMeSci operating System 

SoMeSci Programming language: drop cases where the language is not used only mentioned. 
Re-annotate the other cases connecting them to the software.

Implicit mention: Update softcite so it needs to be conntected to a language, this allows us to re-annotate SoMeSci contexts where a language is mentioned and update the implicit mentions in the context.
Make a list of everything matched to an implicit mention, use this list to re-examine SoMeSci. Drop things without an anchor.

SoMeSci: drop co-reference 

Add SoMeSci Extension to the name to match Softcite annotation

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

# By annotation Difference 

## Developer/Publisher Boundary 

"We used SPSS (IBM Inc.)."

### SoMeSci

Developer: "IBM Inc."

### Softcite

Developer: "IBM Inc"

### SoftMeScite

Regex adjustment (direction to be decided)
Remove the dot. 

## Name Abbreviation/Alternative

"We used Statistical Package for the Social Sciences (SPSS) for analysis."

### SoMeSci

Software: Statistical Package for the Social Sciences
Abbreviation: SPSS

### SoftCite

Software: Statistical Package for the Social Sciences (SPSS)

### SoftMeScite

Regex adjustment : Split it up 

## Graphpad Prism (Developer/Publisher + Software)

"We used Graphpad Prism."

### SoMeSci

Software: Prism
Developer: Graphpad

### SoftCite

Software: Graphpad Prism

### SoftMeScite

Regex adjustment (direction to be decided). 
The Problem is that the software is often called "Graphpad" by mistake even so the software name is "Prism" and the developer is "Graphpad". 

## Software with merged Version

"We used SPSS16."

### SoMeSci

Software: SPSS
Version: 16

### SoftCite

Software: SPSS16

### SoftMeScite

Regex adjustment (direction to be decided). 
This is not generally true for all software. There is software, where the number at the end ist not the version, but actually a part of the name.

## Package/PlugIn descriptions

"We used R package lme4."

### SoMeSci

Software: "R" (Programming Environment)
Software: "lme4" (PlugIn)

### SoftCite

Software: "R package lme4"

### SoftMeScite

Regex adjustment (direction to be decided). 

## Identifier 

Add identifier as a label to extend it to RRID, swMATH, and other identifiers.