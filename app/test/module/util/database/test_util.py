from app.main.modules.util.mysql import *


def test_get_column_definition():
    result = get_column_definition('column1', 'VARCHAR(255)', 'NULL', 'UNIQUE')
    print(f"\nTEST Result: {result}")
    assert isinstance(result, str)


def test_get_create_table_statement():
    columns = ['id', 'mraid_version', 'video_encoding_complete', 'description', 'decimal_assets', 'vast_xml_url',
               'duration', 'width',
               'image_assets', 'landing_page_url', 'text_assets', 'third_party_impression_tracking_url2',
               'right_media_offer_type_id', 'skippable', 'clickthrough_url', 'ad_server_creative_id', 'creative_id',
               'is_player_retargeting_enabled', 'third_party_tracking_tags', 'landing_page_urls', 'ad_server_name',
               'image_url',
               'third_party_impression_tracking_url', 'is_securable', 'click_through_url', 'height', 'creative_type',
               'video_asset', 'creative_name', 'third_party_impression_tracking_url3', 'vast_tag_url',
               'companion_creative_ids',
               'tracking_events', 'ad_tag', 'ad_technology_ids', 'advertiser_id',
               'third_party_video_viewability_enabled']

    column_definition_list = [get_column_definition(i, 'VARCHAR(255)', 'NULL') for i in columns]
    result = get_create_table_statement(
        table_name='table_name',
        column_definition_list=column_definition_list
    )
    print(f"\nTEST Result: {result}")
    assert isinstance(result, str)


def test_get_add_index_statement():
    result = get_add_index_statement('table_name', 'index_test', ['column1'])
    print(f"\nTEST Result: {result}")
    assert isinstance(result, str)


def test_get_add_column_statement():
    result = get_add_column_statement('table_name', get_column_definition('column4', 'VARCHAR(255)', 'NULL'))
    print(f"\nTEST Result: {result}")
    assert isinstance(result, str)
