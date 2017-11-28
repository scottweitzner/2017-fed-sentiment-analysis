import constants

import sys

from watson_developer_cloud import NaturalLanguageUnderstandingV1, WatsonException
import watson_developer_cloud.natural_language_understanding.features.v1 as features

import json
import pprint
pp = pprint.PrettyPrinter(indent=4)


def execute_watson_request(text):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        username=constants.WATSON_USER,
        password=constants.WATSON_PASS,
        version="2017-02-27"
    )

    try:
        response = natural_language_understanding.analyze(
            text=text,
            features=[
                features.Concepts(),
                features.Categories(),
                features.Emotion(),
                features.Entities(
                    emotion=True,
                    sentiment=True
                ),
                features.Keywords(
                    emotion=True,
                    sentiment=True
                ),
                features.Sentiment()
            ]
        )
        return response
    except WatsonException as error:
        return str(error)

def main():
    in_data = json.load(open('./in/fed_speech.json'))
    speech = in_data['speech'].encode('ascii', 'replace')
    out = execute_watson_request( speech )

    # DOCUMENT
    print("="*10 + "DOCUMENT" + "="*10)
    print("sentiment: %-10s %5f" % (out['sentiment']['document']['label'], out['sentiment']['document']['score']) )

    # CATEGORIES
    print("\n" + "="*10 + "CATEGORIES" + "="*10)
    for category in out['categories']:
        print("label: %-40s score: %f" % (category['label'], category['score']) )

    # CONCEPTS
    print("\n" + "="*10 + "CONCEPTS" + "="*10)
    for concept in out['concepts']:
        print("text: %-40s relevance: %f" % (concept['text'], concept['relevance']) )

    # EMOTIONS
    print("\n" + "="*10 + "EMOTIONS" + "="*10)
    anger   = out['emotion']['document']['emotion']['anger']
    disgust = out['emotion']['document']['emotion']['disgust']
    fear    = out['emotion']['document']['emotion']['fear']
    joy     = out['emotion']['document']['emotion']['joy']
    sadness = out['emotion']['document']['emotion']['sadness']

    print("%-10s: %5f" % ("anger"  , anger) )
    print("%-10s: %5f" % ("disgust", disgust) )
    print("%-10s: %5f" % ("fear"   , fear) )
    print("%-10s: %5f" % ("joy"    , joy) )
    print("%-10s: %5f" % ("sadness", sadness) )

    # ENTITIES
    print("\n" + "="*10 + "ENTITIES" + "="*10)
    for ent in out['entities']:
        print("entity: %-15s \t type: %-15s relevance: %f" % (ent['text'], ent['type'], ent['relevance']) )
        print("\tsentiment: %-10s %5f" % (ent['sentiment']['label'], ent['sentiment']['score']) )
        if 'emotion' in ent:
            print("\t%-10s: %5f" % ("anger"  , ent['emotion']['anger']) )
            print("\t%-10s: %5f" % ("disgust", ent['emotion']['disgust']) )
            print("\t%-10s: %5f" % ("fear"   , ent['emotion']['fear']) )
            print("\t%-10s: %5f" % ("joy"    , ent['emotion']['joy']) )
            print("\t%-10s: %5f" % ("sadness", ent['emotion']['sadness']) )

     # KEYWORDS
    print("\n" + "="*10 + "KEYWORDS" + "="*10)
    for key in out['keywords']:
        print("keyword: %-25s \t relevance: %f" % (key['text'], key['relevance']) )
        print("\tsentiment: %-10s %5f" % (key['sentiment']['label'], key['sentiment']['score']) )
        if 'emotion' in key:
            print("\t%-10s: %5f" % ("anger"  , key['emotion']['anger']) )
            print("\t%-10s: %5f" % ("disgust", key['emotion']['disgust']) )
            print("\t%-10s: %5f" % ("fear"   , key['emotion']['fear']) )
            print("\t%-10s: %5f" % ("joy"    , key['emotion']['joy']) )
            print("\t%-10s: %5f" % ("sadness", key['emotion']['sadness']) )

if __name__ == "__main__":
    main()
