import constants
import sys
import json
import pprint

from watson_developer_cloud import NaturalLanguageUnderstandingV1, WatsonException
import watson_developer_cloud.natural_language_understanding.features.v1 as features

pp = pprint.PrettyPrinter(indent=4)

def execute_watson_request(word):
    in_data = json.load(open('./in/fed_speech.json'))
    speech = in_data['speech'].encode('ascii', 'replace')

    natural_language_understanding = NaturalLanguageUnderstandingV1(
        username=constants.WATSON_USER,
        password=constants.WATSON_PASS,
        version="2017-02-27"
    )

    try:
        response = natural_language_understanding.analyze(
            text=speech,
            features=[
                features.Emotion(
                    targets=[word]
                ),
                features.Sentiment(
                    targets=[word]
                )
            ]
        )
        return response
    except WatsonException as error:
        print( str(error) )
        exit(0)

def args_to_string():
    phrase = ""
    for arg in sys.argv[1:]:
        phrase += " " + arg
    phrase = phrase.strip()
    return phrase

def main():
    if len(sys.argv) < 2:
        print("You must supply a word to be looked up")
    else:

        phrase = args_to_string()
        out = execute_watson_request( phrase )

        print("~~ " + phrase + " ~~")

        # EMOTION
        print("="*10 + "EMOTIONS" + "="*10)
        anger   = out['emotion']['targets'][0]['emotion']['anger']
        disgust = out['emotion']['targets'][0]['emotion']['disgust']
        fear    = out['emotion']['targets'][0]['emotion']['fear']
        joy     = out['emotion']['targets'][0]['emotion']['joy']
        sadness = out['emotion']['targets'][0]['emotion']['sadness']

        print("%-10s: %5f" % ("anger"  , anger) )
        print("%-10s: %5f" % ("disgust", disgust) )
        print("%-10s: %5f" % ("fear"   , fear) )
        print("%-10s: %5f" % ("joy"    , joy) )
        print("%-10s: %5f" % ("sadness", sadness) )

        # SENTIMENT
        print("\n" + "="*10 + "SENTIMENT" + "="*10)
        print("sentiment: %-10s %5f" % (out['sentiment']['targets'][0]['label'], out['sentiment']['targets'][0]['score']) )


if __name__ == "__main__":
    main()