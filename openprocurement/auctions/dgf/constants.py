from datetime import datetime, timedelta
from openprocurement.api.models import TZ, ORA_CODES


def read_json(name):
    import os.path
    from json import loads
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(curr_dir, name)
    with open(file_path) as lang_file:
        data = lang_file.read()
    return loads(data)

#document types
DOCUMENT_TYPE_OFFLINE = ['x_dgfAssetFamiliarization']
DOCUMENT_TYPE_URL_ONLY = ['virtualDataRoom']

#requiremnt periods
MINIMAL_EXPOSITION_PERIOD = timedelta(days=7)
VERIFY_AUCTION_PROTOCOL_TIME = timedelta(days=6)
AWARD_PAYMENT_TIME = timedelta(days=20)
CONTRACT_SIGNING_TIME = timedelta(days=20)

#time constants
MINIMAL_EXPOSITION_REQUIRED_FROM = datetime(2017, 11, 17, tzinfo=TZ)
CLASSIFICATION_PRECISELY_FROM = datetime(2017, 7, 19, tzinfo=TZ)
DGF_ID_REQUIRED_FROM = datetime(2017, 1, 1, tzinfo=TZ)
DGF_DECISION_REQUIRED_FROM = datetime(2017, 1, 1, tzinfo=TZ)
DGF_ADDRESS_LOCATION_REQUIRED_FROM = datetime(2017, 1, 1, tzinfo=TZ)

#codes
CAVPS_CODES = read_json('cav_ps.json')
CPVS_CODES = read_json('cpvs.json')
ORA_CODES[0:0] = ["UA-IPN", "UA-FIN"]

#code units
CPV_NON_SPECIFIC_LOCATION_UNITS = ('71', '72', '73', '75', '76', '77', '79', '80', '85', '90', '92', '98')
CAV_NON_SPECIFIC_LOCATION_UNITS = ('07', '08')
