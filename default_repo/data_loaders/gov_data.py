import pandas as pd
from pandas import DataFrame
import json
import xmltodict
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



@data_loader
def load_data_from_api(**kwargs) -> DataFrame:
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    funds_file = '/filedrop/Funds 01-May-2023.xml'

    with open(funds_file) as f:
        xml_doc = xmltodict.parse(f.read())
        
    df = pd.json_normalize(xml_doc['Funds']['Fund'])
    df.rename(columns={
        'RelatedBrandNames.Brand.@UseToBrandPHIS': 'RelatedBrand@UseToBrandPHIS',
        'RelatedBrandNames.Brand.BrandName': 'RelatedBrandName',
        'RelatedBrandNames.Brand.BrandCode': 'RelatedBrandCode',
        'RelatedBrandNames.Brand.BrandPhone': 'RelatedBrandPhone',
        'RelatedBrandNames.Brand.BrandEmail': 'RelatedBrandEmail',
        'RelatedBrandNames.Brand.BrandWebsite': 'RelatedBrandWebsite',
        'RelatedBrandNames.Brand.BrandWebsiteLinks.Link': 'RelatedBrandWebsiteLink',
        'Address.AddressLine1': 'AddressLine1',
        'Address.Town': 'AddressTown',
        'Address.State': 'AddressState',
        'Address.Postcode': 'AddressPostcode'
    }, inplace=True)

    df.info()

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
