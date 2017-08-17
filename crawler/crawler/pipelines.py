from scrapy.exceptions import DropItem
from elasticsearch import Elasticsearch
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud import ToneAnalyzerV3
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


class ValidationPipeline(object):

    def process_item(self, item, spider):
        if not item['text']:
            raise DropItem("Item text is empty")
        return item


class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['hash_key'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['hash_key'])
            return item


class WatsonPipeline(object):
    # Uses Natural Language Understanding-np (Lite plan) Credentials-1
    nlu = NaturalLanguageUnderstandingV1(
        username="0120587b-fbb4-4cdf-ab49-1727a7d00ca5",
        password="W6UXahJMFRJo",
        version="2017-02-27",
    )
    nlu_features = [
        features.Entities(limit=20),
        features.Keywords(limit=20),
        features.Emotion()
    ]
    # Uses Tone Analyzer-sa (Lite plan) Credentials-1
    sentiment = ToneAnalyzerV3(
        username="685e3e2d-b292-42fe-b82a-c725305f41f6",
        password="0uAVT2Z1bx6w",
        version="2016-05-19",
    )

    def clean_nlu_analysis(self, nlu_analysis):
        cleaned_nlu_analysis = {
            "keywords": nlu_analysis['keywords'],
            "entities": nlu_analysis['entities'],
        }
        return cleaned_nlu_analysis

    def clean_tone_analysis(self, tone_analysis):
        cleaned_tone_analysis = {}
        for cat in tone_analysis['document_tone']['tone_categories']:
            for tone in cat['tones']:
                cleaned_tone_analysis.update({tone['tone_id']: tone['score']})
        return cleaned_tone_analysis

    def process_item(self, item, spider):
        nlu_analysis = self.nlu.analyze(features=self.nlu_features,
                                        text=item['text'])
        tone_analysis = self.sentiment.tone(item['text'],
                                            sentences=False)
        item['nlu_analysis'] = self.clean_nlu_analysis(nlu_analysis)
        item['tone_analysis'] = self.clean_tone_analysis(tone_analysis)
        return item


class ElasticsearchPipeline(object):

    def open_spider(self, spider):
        self.es = Elasticsearch()
        if not self.es.ping():
            raise Exception('Elasticsearch could not be reached')
        self.es.indices.create(index='crawl', ignore=400)

    def process_item(self, item, spider):
        result = self.es.create(index='crawl', doc_type='article', id=item['hash_key'], body=dict(item))
        return item
