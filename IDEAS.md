# By sementical elements

## name

### SoMeSci

### Softcite

### SoftMeScite

## software-type

### SoMeSci

### Softcite

### SoftMeScite

## version

### SoMeSci

### Softcite

### SoftMeScite

## mention-type

### SoMeSci

SoMesci mentions type is mono valuated among allusion, usage, creation and deposition. One mention implicitly suggest that the previous types are true eg. deposition creations means usage and creation, deposition means usage, creation and deposition …

### Softcite

Softcite uses cumulative mentions : used, created and shared. If none of them are present, it should probably match with the “Allusion” mention type of SoMeSci. If multiple types are present, probably the last one between used, created and shared should be kept.

### SoftMeScite

We should probably keep the multi valuated from Softcite and the Allusion from SoMeSci


# By annotation Difference 

## Developer/Publisher Boundary 

"We used SPSS (IBM Inc.)."

### SoMeSci

Developer: "IBM Inc."

### Softcite

Developer: "IBM Inc"

### SoftMeScite

Regex adjustment (direction to be decided)

## Name Abbreviation/Alternative

"We used Statistical Package for the Social Sciences (SPSS) for analysis."

### SoMeSci

Software: Statistical Package for the Social Sciences
Abbreviation: SPSS

### SoftCite

Software: Statistical Package for the Social Sciences (SPSS)

### SoftMeScite

Regex adjustment (direction to be decided)

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