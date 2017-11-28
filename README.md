# FED_2017_sentiment_analysis

## About
This is for an econimcs writing class at Emory University. The assignment was to analyze the release of the FED press conference release for the central bank meeting on september 19-20

From The syllabus:
```
The policy making body of the US central bank will meet on September 19-20.
There will be many news articles leading up to and after this. Chair Yellen
will hold a press conference right afterward (which can be seen later on
YouTube). You should evaluate the decisions made at this meeting based on
what was known at the time
```

## Run Instructions

##### Change the `constants_example.py` file to `constants.py` and input your Watson credentials
##### Make executable with `chmod 700 run`
##### Run with `./run`
##### Output from `run` found in `/out`

##### For specific phrase lookup run with `./run [phrase]`
-  Note: this will return the emotions and sentiment of the given phrase

##### Note: If you wish to change the name of the out directory, change the variable `OUTDIR` in the bash script `run`

## Sources

9/20/2017 FOMC Press Conference [here](https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20170920.pdf)