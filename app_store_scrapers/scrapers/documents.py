from django_elasticsearch_dsl import DocType, Index
from .models import IOSAppObservation, Keyword

# Name of the Elasticsearch index
keyword = Index('keyword')
# See Elasticsearch Indices API reference for available settings
keyword.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@keyword.doc_type
class KeywordDocument(DocType):
    class Meta:
        model = Keyword # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'text'
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True
        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False
        # Paginate the django queryset used to populate the index with the specified size
        # (by default there is no pagination)
        # queryset_pagination = 5000

# Name of the Elasticsearch index
app_observation = Index('app_observation')
# See Elasticsearch Indices API reference for available settings
app_observation.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@app_observation.doc_type
class ObservationDocument(DocType):
    class Meta:
        model = IOSAppObservation # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'description'
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True
        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False
        # Paginate the django queryset used to populate the index with the specified size
        # (by default there is no pagination)
        # queryset_pagination = 5000