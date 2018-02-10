from app.feed import parse, parse_all

from . import get_data_file


def test_parse_ntv_gundem():
    links = parse(get_data_file('data/ntv_gundem.xml'))
    expected_links = [
        'https://www.ntv.com.tr/turkiye/cumhurbaskani-erdogandan-chpli-mahmut-tanal-hakkinda-suc-duyurusu,BY23sb14_kOoDCM3di5V3A',
        'https://www.ntv.com.tr/galeri/dunya/rusya-lideri-vladimir-putin-akilli-telefonum-yok,CoGBcD4e_EC2t9dOq97QDw',
        'https://www.ntv.com.tr/galeri/yasam/elon-muskin-ozel-hayatina-dair-detaylar,EUEgDLdzmUiyxUdSdQa6AQ'
    ]
    assert expected_links == links


def test_parse_all_ntv():
    links = parse_all([
        get_data_file('data/ntv_gundem.xml'),
        get_data_file('data/ntv_teknoloji.xml')])
    expected_links = [
        'https://www.ntv.com.tr/turkiye/cumhurbaskani-erdogandan-chpli-mahmut-tanal-hakkinda-suc-duyurusu,BY23sb14_kOoDCM3di5V3A',
        'https://www.ntv.com.tr/galeri/dunya/rusya-lideri-vladimir-putin-akilli-telefonum-yok,CoGBcD4e_EC2t9dOq97QDw',
        'https://www.ntv.com.tr/galeri/yasam/elon-muskin-ozel-hayatina-dair-detaylar,EUEgDLdzmUiyxUdSdQa6AQ',
        'https://www.ntv.com.tr/ekonomi/unlu-bankaci-qnb-finansinvesti-birakti-bitcoin-aracilik-sirketi-aldi,BMKaUVAu_0KbscTmi94j-A',
        'https://www.ntv.com.tr/teknoloji/cin-internet-uzerinden-calisacak-internet-mahkemesi-kurdu,e2l_8Ckn5k2NO9HUe9FY-A'
    ]
    assert expected_links == links
