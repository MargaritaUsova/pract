import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import urllib.request
from PIL import Image
import pillow_avif
import os

def get_data_names_prices_phones():
    cookies = {
        '__lhash_': '4dc15c1b1cd8f6f3d623e3cb2b9a6d93',
        'MVID_AB_TOP_SERVICES': '1',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_STORE_SORTING': 'true',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLP_GLC': '2',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_RECOMENDATION': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod2',
        'MVID_GUEST_ID': '22635780952',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'CACHE_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80': '2433014794.20480.0000',
        'bIPs': '53593859',
        '_ym_uid': '1687034037702065663',
        '_ym_d': '1687034037',
        '_gid': 'GA1.2.777481713.1687034037',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '9d72349e-b6a4-46fd-a358-a2c81835bd3a',
        'tmr_lvid': '5575ddaeb39d37be811069a4d1349b68',
        'tmr_lvidTS': '1687034040384',
        'advcake_track_id': '6a333a53-1395-e22f-3ebf-d95412e5412b',
        'advcake_session_id': '23626ba4-53a7-b189-e116-4ab486335cc7',
        'uxs_uid': '4aa9db80-0d4e-11ee-ae50-6d99611a2389',
        'flocktory-uuid': 'ddfbb3c6-beb6-4383-8a01-632236b4392e-5',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80_clone': '2433014794.20480.0000',
        'afUserId': '663be7db-4700-4881-b924-77ebdd9e0789-p',
        'adrcid': 'AYVBc490MiC10QI1M9_KJxg',
        'AF_SYNC': '1687034048415',
        'JSESSIONID': '6xSnkThYPkyy6phMhdqpzvv1HJ2DrL7TkZD1Nsb2vHnyZspQZxg2!716989621',
        'mindboxDeviceUUID': '5fe7c84f-9592-4d88-8fca-60fa0bbd2041',
        'directCrm-session': '%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D',
        'cookie_ip_add': '79.139.209.174',
        '_ga': 'GA1.2.1990035478.1687034037',
        'tmr_detect': '0%7C1687119843217',
        'gsscgib-w-mvideo': 'AWlft0VUNP8bo1UaLyrjyAjx69lMFi81nSOLxpvIyiTYVxfce1pfTphJ46D9EGPadTOe6N7Jwj1IdeqgWdjZPebo0youwfZyApHD2nKQSBX8qwMgn72+5sWtPfp96eoTN9HObYLiVoDEttu1VsfRZey2bBv+1oe//WvZm3yUPNyGPmbEMLJ4MTJF/sOIujf0u5LtgeRcpIbMGVnXTdsXtkimOdF+zw2huBpHFW4KXc+GYtyL51lEj06JiEsyFXY=',
        'gsscgib-w-mvideo': 'AWlft0VUNP8bo1UaLyrjyAjx69lMFi81nSOLxpvIyiTYVxfce1pfTphJ46D9EGPadTOe6N7Jwj1IdeqgWdjZPebo0youwfZyApHD2nKQSBX8qwMgn72+5sWtPfp96eoTN9HObYLiVoDEttu1VsfRZey2bBv+1oe//WvZm3yUPNyGPmbEMLJ4MTJF/sOIujf0u5LtgeRcpIbMGVnXTdsXtkimOdF+zw2huBpHFW4KXc+GYtyL51lEj06JiEsyFXY=',
        '__rhash_': 'e2b0718bf68d2f4d175c2971424efa82',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        '_sp_ses.d61c': '*',
        '_sp_id.d61c': 'ae2f8cb0-62f2-402e-866a-f75052b0dada.1687034037.10.1687205370.1687119827.c81786e4-191b-4049-b6f2-66aaff9d86b4.f6c8be1c-fd1d-4b06-a87f-2fc3eb83789d.841a6bcc-a523-46fe-8d92-7dbdd4e81c71.1687205369799.2',
        '__hash_': 'b8c2f7d8dc2d5f4d17515dea1f745b35',
        '_ga_CFMZTSS5FM': 'GS1.1.1687205381.10.0.1687205381.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1687205381.10.0.1687205381.60.0.0',
        'cfidsgib-w-mvideo': 'fOYygLn6OJnrJgPcQtbYY8x6FExQoLXfqtMmr2+WKl6zSF/PQoJKpg2oRMOxcKuNWDIjJrkpAAy+QKaKCf5aPONf5m41ldAoZ/qjJC8sWA3aPP8j6UcigdT9mrX6p1a/4jixTL7a11+CG6b7BbYYHopr4W7Qe1dkxs7PFNI=',
        'gssc218': '',
        'fgsscgib-w-mvideo': '14lg5369dc72414be8160e5edba5271870c8bfb3',
        'fgsscgib-w-mvideo': '14lg5369dc72414be8160e5edba5271870c8bfb3',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=307d3b3dc61d4dacb8f552b41ede1049,sentry-sample_rate=0.5',
        # 'cookie': '__lhash_=4dc15c1b1cd8f6f3d623e3cb2b9a6d93; MVID_AB_TOP_SERVICES=1; MVID_ACTOR_API_AVAILABILITY=true; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_AVAILABILITY=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLP_GLC=2; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_RECOMENDATION=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod2; MVID_GUEST_ID=22635780952; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=2; COMPARISON_INDICATOR=false; CACHE_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80=2433014794.20480.0000; bIPs=53593859; _ym_uid=1687034037702065663; _ym_d=1687034037; _gid=GA1.2.777481713.1687034037; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=9d72349e-b6a4-46fd-a358-a2c81835bd3a; tmr_lvid=5575ddaeb39d37be811069a4d1349b68; tmr_lvidTS=1687034040384; advcake_track_id=6a333a53-1395-e22f-3ebf-d95412e5412b; advcake_session_id=23626ba4-53a7-b189-e116-4ab486335cc7; uxs_uid=4aa9db80-0d4e-11ee-ae50-6d99611a2389; flocktory-uuid=ddfbb3c6-beb6-4383-8a01-632236b4392e-5; flacktory=no; BIGipServeratg-ps-prod_tcp80_clone=2433014794.20480.0000; afUserId=663be7db-4700-4881-b924-77ebdd9e0789-p; adrcid=AYVBc490MiC10QI1M9_KJxg; AF_SYNC=1687034048415; JSESSIONID=6xSnkThYPkyy6phMhdqpzvv1HJ2DrL7TkZD1Nsb2vHnyZspQZxg2!716989621; mindboxDeviceUUID=5fe7c84f-9592-4d88-8fca-60fa0bbd2041; directCrm-session=%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D; cookie_ip_add=79.139.209.174; _ga=GA1.2.1990035478.1687034037; tmr_detect=0%7C1687119843217; gsscgib-w-mvideo=AWlft0VUNP8bo1UaLyrjyAjx69lMFi81nSOLxpvIyiTYVxfce1pfTphJ46D9EGPadTOe6N7Jwj1IdeqgWdjZPebo0youwfZyApHD2nKQSBX8qwMgn72+5sWtPfp96eoTN9HObYLiVoDEttu1VsfRZey2bBv+1oe//WvZm3yUPNyGPmbEMLJ4MTJF/sOIujf0u5LtgeRcpIbMGVnXTdsXtkimOdF+zw2huBpHFW4KXc+GYtyL51lEj06JiEsyFXY=; gsscgib-w-mvideo=AWlft0VUNP8bo1UaLyrjyAjx69lMFi81nSOLxpvIyiTYVxfce1pfTphJ46D9EGPadTOe6N7Jwj1IdeqgWdjZPebo0youwfZyApHD2nKQSBX8qwMgn72+5sWtPfp96eoTN9HObYLiVoDEttu1VsfRZey2bBv+1oe//WvZm3yUPNyGPmbEMLJ4MTJF/sOIujf0u5LtgeRcpIbMGVnXTdsXtkimOdF+zw2huBpHFW4KXc+GYtyL51lEj06JiEsyFXY=; __rhash_=e2b0718bf68d2f4d175c2971424efa82; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; _sp_ses.d61c=*; _sp_id.d61c=ae2f8cb0-62f2-402e-866a-f75052b0dada.1687034037.10.1687205370.1687119827.c81786e4-191b-4049-b6f2-66aaff9d86b4.f6c8be1c-fd1d-4b06-a87f-2fc3eb83789d.841a6bcc-a523-46fe-8d92-7dbdd4e81c71.1687205369799.2; __hash_=b8c2f7d8dc2d5f4d17515dea1f745b35; _ga_CFMZTSS5FM=GS1.1.1687205381.10.0.1687205381.0.0.0; _ga_BNX5WPP3YK=GS1.1.1687205381.10.0.1687205381.60.0.0; cfidsgib-w-mvideo=fOYygLn6OJnrJgPcQtbYY8x6FExQoLXfqtMmr2+WKl6zSF/PQoJKpg2oRMOxcKuNWDIjJrkpAAy+QKaKCf5aPONf5m41ldAoZ/qjJC8sWA3aPP8j6UcigdT9mrX6p1a/4jixTL7a11+CG6b7BbYYHopr4W7Qe1dkxs7PFNI=; gssc218=; fgsscgib-w-mvideo=14lg5369dc72414be8160e5edba5271870c8bfb3; fgsscgib-w-mvideo=14lg5369dc72414be8160e5edba5271870c8bfb3',
        'referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205?from=homepage',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '307d3b3dc61d4dacb8f552b41ede1049-a8dbdc6b9234d2e8-0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-gib-fgsscgib-w-mvideo': '14lg5369dc72414be8160e5edba5271870c8bfb3',
        'x-gib-gsscgib-w-mvideo': 'AWlft0VUNP8bo1UaLyrjyAjx69lMFi81nSOLxpvIyiTYVxfce1pfTphJ46D9EGPadTOe6N7Jwj1IdeqgWdjZPebo0youwfZyApHD2nKQSBX8qwMgn72+5sWtPfp96eoTN9HObYLiVoDEttu1VsfRZey2bBv+1oe//WvZm3yUPNyGPmbEMLJ4MTJF/sOIujf0u5LtgeRcpIbMGVnXTdsXtkimOdF+zw2huBpHFW4KXc+GYtyL51lEj06JiEsyFXY=',
        'x-set-application-id': 'e2c35809-2382-4b0c-a071-7427890f10f1',
    }

    params = {
        'categoryId': '205',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()

    products_id = response.get('body').get('products')

    with open('phones_data/products_id_phones.json', 'w') as file:
        json.dump(products_id, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_id,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('phones_data/phones_list.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
    products_names = response.get('body').get('products')


    products_id_str = ','.join(products_id)

    params = {
        'productIds': products_id_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('phone_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    item_prices = {}
    phone_prices = response.get('body').get('materialPrices')
    for item in phone_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_discount_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        item_prices[item_id] = {
            'item_base_price' : item_base_price,
            'item_discount_price' : item_discount_price,
            'item_bonus' : item_bonus,
            'id' : item_id
        }


    item_names = {}
    for item in products_names:
        item_id = item.get('productId')
        item_name = item.get('name')
        item_names[item_id] = {'item_name' : item_name, 'id' : item_id}


    for i in item_prices:
        for j in item_names:
            if j == i:
                print(i, j)
                item_prices[j].update(item_names[i])

    with open('phone_prices.json', 'w') as file:
        json.dump(item_prices, file, indent=4, ensure_ascii=False)

def get_data_cashback_phones():
    with open('phone_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in prices:
            item_cashback[i] = {'item_cashback': '10%'}
            prices[i].update(item_cashback[i])

    with open('phone_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_data_characteristics_phones():
    item_characteristics = {}
    shoma_characteristics = {}
    with open('phones_data/phones_list.json') as f2:
        data = json.load(f2)
        for i in data['products']:
            #print(i['productId']) id
            prod_id = i['productId']
            #print(i['brandName']) brand
            item_characteristics[prod_id] = {
                'id' : prod_id,
                'brand' : i['brandName']
            }
            for j in i['propertiesPortion']:
                #print(f"{j['name'] + ' ' + j['value']}", j['name'] + ' ' + j['value'])
                shoma_characteristics[prod_id] = {
                    f"{j['name']}": j['name'] + ' ' + j['value']
                }
                item_characteristics[prod_id].update(shoma_characteristics[prod_id])

    with open('phone_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in item_characteristics:
            prices[i].update(item_characteristics[i])

    with open('phone_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_data_href_phones():
    with open('phones_data/phones_list.json') as f1:
        prices = json.load(f1)
        hrefs = {}
        for i in prices['products']:
            id = i['productId']
            hrefs[id] = {
                'nameTranslit': i['nameTranslit']
            }

    with open('phone_prices.json') as f1:
        prices = json.load(f1)
        for i in prices:
            prices[i].update(hrefs[i])

    with open('phone_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_images_phones():
    with open('phones_data/phones_list.json') as f1:
        prices = json.load(f1)
        phone_images = {}
        for i in prices['products']:
            phone_images[i['productId']] = {
                'image' : 'http://static.mvideo.ru/' + i['images'][0],
                'image1' : 'http://static.mvideo.ru/' + i['images'][1],
                'image2' : 'http://static.mvideo.ru/' + i['images'][2],
                'image3' : 'http://static.mvideo.ru/' + i['images'][3]

            }
    with open('phone_prices.json') as f2:
        prices = json.load(f2)
        for i in prices:
            prices[i].update(phone_images[i])

    with open('phone_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)

    for i in prices:
        img = prices[i]['image']
        img1 = prices[i]['image1']


        resource = urllib.request.urlopen(img)
        out = open(f"pract/renessans_tech/static/pictures/phones/{i}.jpg", 'wb')
        out.write(resource.read())
        out.close()

    '''
        resource = urllib.request.urlopen(img1)
        out = open(f"pract/renessans_tech/static/pictures/phones/img1/{i}.jpg", 'wb')
        out.write(resource.read())
        JPGimg = Image.open(f"pract/renessans_tech/static/pictures/phones/img1/{i}.jpg")
        JPGimg.save(f"pract/renessans_tech/static/pictures/phones/img1/{i}"+ '.AVIF', 'AVIF')
        os.remove(f"pract/renessans_tech/static/pictures/phones/img1/{i}.jpg")
        out.close()

        img2 = prices[i]['image2']
        img3 = prices[i]['image3']
        resource = urllib.request.urlopen(img2)
        out = open(f"pract/renessans_tech/static/pictures/phones/img2/{i}.jpg", 'wb')
        out.write(resource.read())
        JPGimg = Image.open(f"pract/renessans_tech/static/pictures/phones/img2/{i}.jpg")
        JPGimg.save(f"pract/renessans_tech/static/pictures/phones/img2/{i}" + '.AVIF', 'AVIF')
        os.remove(f"pract/renessans_tech/static/pictures/phones/img2/{i}.jpg")
        out.close()

        resource = urllib.request.urlopen(img3)
        out = open(f"pract/renessans_tech/static/pictures/phones/img3/{i}.jpg", 'wb')
        out.write(resource.read())
        JPGimg = Image.open(f"pract/renessans_tech/static/pictures/phones/img3/{i}.jpg")
        JPGimg.save(f"pract/renessans_tech/static/pictures/phones/img3/{i}" + '.AVIF', 'AVIF')
        os.remove(f"pract/renessans_tech/static/pictures/phones/img3/{i}.jpg")
        out.close()
        
    '''


def get_data_laptops():
    cookies = {
        '__lhash_': '4dc15c1b1cd8f6f3d623e3cb2b9a6d93',
        'MVID_AB_TOP_SERVICES': '1',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_STORE_SORTING': 'true',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLP_GLC': '2',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_RECOMENDATION': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod2',
        'MVID_GUEST_ID': '22635780952',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'CACHE_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80': '2433014794.20480.0000',
        'bIPs': '53593859',
        '_ym_uid': '1687034037702065663',
        '_ym_d': '1687034037',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '9d72349e-b6a4-46fd-a358-a2c81835bd3a',
        'tmr_lvid': '5575ddaeb39d37be811069a4d1349b68',
        'tmr_lvidTS': '1687034040384',
        'advcake_track_id': '6a333a53-1395-e22f-3ebf-d95412e5412b',
        'advcake_session_id': '23626ba4-53a7-b189-e116-4ab486335cc7',
        'uxs_uid': '4aa9db80-0d4e-11ee-ae50-6d99611a2389',
        'flocktory-uuid': 'ddfbb3c6-beb6-4383-8a01-632236b4392e-5',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80_clone': '2433014794.20480.0000',
        'afUserId': '663be7db-4700-4881-b924-77ebdd9e0789-p',
        'adrcid': 'AYVBc490MiC10QI1M9_KJxg',
        'AF_SYNC': '1687034048415',
        'cookie_ip_add': '79.139.209.174',
        '_gid': 'GA1.2.890673097.1687432336',
        '_ym_isad': '2',
        'gssc218': '',
        'gsscgib-w-mvideo': 'pJmhAeRSVY/9PhYjxtZB73G89LQAQ+5AFuNZHVVYKBc8Dpnpj+oowkzkR/37jWvSxMJsl/AbVjQFNcWeHF3lfhbbJFbsHTPF7pIDZ68Ruj65z74XGxZBPfhVdrg2+3X3iqfK7F7GFFUoT4+/tgNga8ZU7YmSM7ZNBzLg9391T6XoIoVnFnXnXEzrrvRTzvMoWVlRCG79wL3z5nWFCRGq1SpJECzPAFnZYRYeNTAcKECpRGli1HjE7mQY3aeCsIwYYpE=',
        'gsscgib-w-mvideo': 'pJmhAeRSVY/9PhYjxtZB73G89LQAQ+5AFuNZHVVYKBc8Dpnpj+oowkzkR/37jWvSxMJsl/AbVjQFNcWeHF3lfhbbJFbsHTPF7pIDZ68Ruj65z74XGxZBPfhVdrg2+3X3iqfK7F7GFFUoT4+/tgNga8ZU7YmSM7ZNBzLg9391T6XoIoVnFnXnXEzrrvRTzvMoWVlRCG79wL3z5nWFCRGq1SpJECzPAFnZYRYeNTAcKECpRGli1HjE7mQY3aeCsIwYYpE=',
        'fgsscgib-w-mvideo': '6a4ub0c32243f1043948b598d7a612da187c3602',
        'fgsscgib-w-mvideo': '6a4ub0c32243f1043948b598d7a612da187c3602',
        'cfidsgib-w-mvideo': 'GBm3Zuidr9K6A7n0Z+m8kJCvRRn3Vy1+taZ9GjAu23pBMbwfd98cebV78dttmE3McsA8C899pblb3Tuu3Bl+x6TIu2AlKtnJ22LxVft85rpOUemdl9KDiYIE3WHvGvmS52hFYYQv+pWuU2QL8nRDzSxkdl6eJ9QSa+BYpfs=',
        '__hash_': 'b8c2f7d8dc28df9fb7515dea1f745b35',
        '_ga_BNX5WPP3YK': 'GS1.1.1687525517.17.1.1687527348.60.0.0',
        '_ga_CFMZTSS5FM': 'GS1.1.1687525517.17.1.1687527348.0.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=0da594e4e6824d9295a62f4fa2fea93c,sentry-sample_rate=0.5',
        # 'cookie': '__lhash_=4dc15c1b1cd8f6f3d623e3cb2b9a6d93; MVID_AB_TOP_SERVICES=1; MVID_ACTOR_API_AVAILABILITY=true; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLP_GLC=2; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_RECOMENDATION=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod2; MVID_GUEST_ID=22635780952; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=2; COMPARISON_INDICATOR=false; CACHE_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80=2433014794.20480.0000; bIPs=53593859; _ym_uid=1687034037702065663; _ym_d=1687034037; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=9d72349e-b6a4-46fd-a358-a2c81835bd3a; tmr_lvid=5575ddaeb39d37be811069a4d1349b68; tmr_lvidTS=1687034040384; advcake_track_id=6a333a53-1395-e22f-3ebf-d95412e5412b; advcake_session_id=23626ba4-53a7-b189-e116-4ab486335cc7; uxs_uid=4aa9db80-0d4e-11ee-ae50-6d99611a2389; flocktory-uuid=ddfbb3c6-beb6-4383-8a01-632236b4392e-5; flacktory=no; BIGipServeratg-ps-prod_tcp80_clone=2433014794.20480.0000; afUserId=663be7db-4700-4881-b924-77ebdd9e0789-p; adrcid=AYVBc490MiC10QI1M9_KJxg; AF_SYNC=1687034048415; cookie_ip_add=79.139.209.174; _gid=GA1.2.890673097.1687432336; _ym_isad=2; gssc218=; gsscgib-w-mvideo=pJmhAeRSVY/9PhYjxtZB73G89LQAQ+5AFuNZHVVYKBc8Dpnpj+oowkzkR/37jWvSxMJsl/AbVjQFNcWeHF3lfhbbJFbsHTPF7pIDZ68Ruj65z74XGxZBPfhVdrg2+3X3iqfK7F7GFFUoT4+/tgNga8ZU7YmSM7ZNBzLg9391T6XoIoVnFnXnXEzrrvRTzvMoWVlRCG79wL3z5nWFCRGq1SpJECzPAFnZYRYeNTAcKECpRGli1HjE7mQY3aeCsIwYYpE=; gsscgib-w-mvideo=pJmhAeRSVY/9PhYjxtZB73G89LQAQ+5AFuNZHVVYKBc8Dpnpj+oowkzkR/37jWvSxMJsl/AbVjQFNcWeHF3lfhbbJFbsHTPF7pIDZ68Ruj65z74XGxZBPfhVdrg2+3X3iqfK7F7GFFUoT4+/tgNga8ZU7YmSM7ZNBzLg9391T6XoIoVnFnXnXEzrrvRTzvMoWVlRCG79wL3z5nWFCRGq1SpJECzPAFnZYRYeNTAcKECpRGli1HjE7mQY3aeCsIwYYpE=; fgsscgib-w-mvideo=6a4ub0c32243f1043948b598d7a612da187c3602; fgsscgib-w-mvideo=6a4ub0c32243f1043948b598d7a612da187c3602; cfidsgib-w-mvideo=GBm3Zuidr9K6A7n0Z+m8kJCvRRn3Vy1+taZ9GjAu23pBMbwfd98cebV78dttmE3McsA8C899pblb3Tuu3Bl+x6TIu2AlKtnJ22LxVft85rpOUemdl9KDiYIE3WHvGvmS52hFYYQv+pWuU2QL8nRDzSxkdl6eJ9QSa+BYpfs=; __hash_=b8c2f7d8dc28df9fb7515dea1f745b35; _ga_BNX5WPP3YK=GS1.1.1687525517.17.1.1687527348.60.0.0; _ga_CFMZTSS5FM=GS1.1.1687525517.17.1.1687527348.0.0.0',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=homepage',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '0da594e4e6824d9295a62f4fa2fea93c-a7736c31c482a1fe-0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-set-application-id': '4c5df736-1a11-4e91-a0c8-95954338d903',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()

    products_id = response.get('body').get('products')

    json_data = {
        'productIds': products_id,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('laptops_data/laptops_list.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_names = response.get('body').get('products')

    products_id_str = ','.join(products_id)

    params = {
        'productIds': products_id_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    item_prices = {}
    phone_prices = response.get('body').get('materialPrices')
    for item in phone_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_discount_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        item_prices[item_id] = {
            'item_base_price': item_base_price,
            'item_discount_price': item_discount_price,
            'item_bonus': item_bonus,
            'id': item_id
        }

    item_names = {}
    for item in products_names:
        item_id = item.get('productId')
        item_name = item.get('name')
        item_names[item_id] = {'item_name': item_name, 'id': item_id}

    for i in item_prices:
        for j in item_names:
            if j == i:
                item_prices[j].update(item_names[i])

    with open('laptop_prices.json', 'w') as file:
        json.dump(item_prices, file, indent=4, ensure_ascii=False)


def get_characteristics_laptops():
    item_characteristics = {}
    shoma_characteristics = {}
    with open('laptops_data/laptops_list.json') as f2:
        data = json.load(f2)
        for i in data['products']:
            # print(i['productId']) id
            prod_id = i['productId']
            # print(i['brandName']) brand
            item_characteristics[prod_id] = {
                'id': prod_id,
                'brand': i['brandName'],
                'nameTranslit': i['nameTranslit']
            }
            for j in i['propertiesPortion']:
                # print(f"{j['name'] + ' ' + j['value']}", j['name'] + ' ' + j['value'])
                shoma_characteristics[prod_id] = {
                    f"{j['name']}": j['name'] + ' ' + j['value']
                }
                item_characteristics[prod_id].update(shoma_characteristics[prod_id])

    with open('laptop_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in item_characteristics:
            prices[i].update(item_characteristics[i])

    with open('laptop_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_images_laptopsssss():
    with open('laptops_data/laptops_list.json') as f1:
        prices = json.load(f1)
        phone_images = {}
        for i in prices['products']:
            phone_images[i['productId']] = {
                'image' : 'http://static.mvideo.ru/' + i['images'][0]
            }
    with open('laptop_prices.json') as f2:
        prices = json.load(f2)
        for i in prices:
            prices[i].update(phone_images[i])

    with open('laptop_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)

    for i in prices:
        img = prices[i]['image']
        resource = urllib.request.urlopen(img)
        out = open(f"pract/renessans_tech/static/pictures/laptops/{i}.jpg", 'wb')
        out.write(resource.read())
        out.close()


def get_cashback_laptops():
    with open('laptop_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in prices:
            item_cashback[i] = {'item_cashback': '10%'}
            prices[i].update(item_cashback[i])

    with open('laptop_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_data_tv():
    cookies = {
        'MVID_AB_TOP_SERVICES': '1',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_STORE_SORTING': 'true',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLP_GLC': '2',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_RECOMENDATION': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_GUEST_ID': '22635780952',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        '_ym_uid': '1687034037702065663',
        '_ym_d': '1687034037',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '9d72349e-b6a4-46fd-a358-a2c81835bd3a',
        'tmr_lvid': '5575ddaeb39d37be811069a4d1349b68',
        'tmr_lvidTS': '1687034040384',
        'advcake_track_id': '6a333a53-1395-e22f-3ebf-d95412e5412b',
        'advcake_session_id': '23626ba4-53a7-b189-e116-4ab486335cc7',
        'uxs_uid': '4aa9db80-0d4e-11ee-ae50-6d99611a2389',
        'flocktory-uuid': 'ddfbb3c6-beb6-4383-8a01-632236b4392e-5',
        'afUserId': '663be7db-4700-4881-b924-77ebdd9e0789-p',
        'adrcid': 'AYVBc490MiC10QI1M9_KJxg',
        'cookie_ip_add': '79.139.209.174',
        '_gid': 'GA1.2.511097384.1687527353',
        'MVID_ENVCLOUD': 'prod2',
        'SMSError': '',
        'authError': '',
        'BIGipServeratg-ps-prod_tcp80': '2466569226.20480.0000',
        'bIPs': '-314595793',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80_clone': '2466569226.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        '__lhash_': '4dc15c1b1cd8f6f3d623e3cb2b9a6d93',
        'AF_SYNC': '1687714758733',
        '__rhash_': 'e2b0718bf684dfed675c2971424efa82',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        '_sp_ses.d61c': '*',
        '__hash_': 'b8c2f7d8dc24efed67515dea1f745b35',
        'JSESSIONID': 'R4wskhyYQYpC6vRDhn6rR5TTSgtzC02yJxvTycLXmVntMjWgc25P!685572310',
        'CACHE_INDICATOR': 'false',
        'gssc218': '',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        'mindboxDeviceUUID': '5fe7c84f-9592-4d88-8fca-60fa0bbd2041',
        'directCrm-session': '%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D',
        'gsscgib-w-mvideo': 'm7OZnTaYP6L0aVw44FLlGsdevSmtPFD5jPPVZXuaUql9bLIGncyBwJs/YUr7tpO8xDK2yQEqid6ntgjZAkJyuwGa1qjKnk+Oz/om5xQvN7Ew8IcoJkQjuKMneEDG8T4+E6wKm1OUjQOzCpA/IVy/0QbunAhfp3kaa9KJfl0Gq3nCccV2vZJM1a0gGWVjwSCHnT+Z8zoriXF42+eu2nqTzKlP5wnnRicB3X6QUuUygHwZFOrxCDWdKmKqQgCB2g==',
        'gsscgib-w-mvideo': 'm7OZnTaYP6L0aVw44FLlGsdevSmtPFD5jPPVZXuaUql9bLIGncyBwJs/YUr7tpO8xDK2yQEqid6ntgjZAkJyuwGa1qjKnk+Oz/om5xQvN7Ew8IcoJkQjuKMneEDG8T4+E6wKm1OUjQOzCpA/IVy/0QbunAhfp3kaa9KJfl0Gq3nCccV2vZJM1a0gGWVjwSCHnT+Z8zoriXF42+eu2nqTzKlP5wnnRicB3X6QUuUygHwZFOrxCDWdKmKqQgCB2g==',
        '_sp_id.d61c': '2a8f65ed-0abf-4d12-bcea-0cdf4026919e.1687527353.12.1687859848.1687784015.3bc6ec58-aaf1-458f-b520-b38a3bdebfc3.1b8c9b52-c913-48ae-b911-e9df50689f72.fd52b527-1b6d-4e31-a38a-85a33424994a.1687859828505.22',
        '_ga_CFMZTSS5FM': 'GS1.1.1687859829.25.1.1687859847.0.0.0',
        '_ga': 'GA1.2.838583662.1687527353',
        'tmr_detect': '0%7C1687859853585',
        'fgsscgib-w-mvideo': 'hPqw4eb250b2bf0bf7e35c5a9976bdb1c1804980',
        'fgsscgib-w-mvideo': 'hPqw4eb250b2bf0bf7e35c5a9976bdb1c1804980',
        'cfidsgib-w-mvideo': 'KVZpeE/zl/cpIiUz6tYqtd55taF7/ivTC4i2lFaJLGc6QR1NpTxZQBxKa8dk8K7nT/KoO+Dgegt1x/ci5pwMP/hCJoUr42lmLs7VMuwEw184s1LyANjJhMYmSVUs5AzjXNLR0Ls9pXb0VKOfDh0Ji25EhaBV54/z10RVl2O0',
        '_ga_BNX5WPP3YK': 'GS1.1.1687859829.25.1.1687859854.35.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=ff9fc318dc1345a4ac051fb7c7817208,sentry-sample_rate=0.5',
        # 'cookie': 'MVID_AB_TOP_SERVICES=1; MVID_ACTOR_API_AVAILABILITY=true; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLP_GLC=2; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_RECOMENDATION=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_GUEST_ID=22635780952; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=2; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; _ym_uid=1687034037702065663; _ym_d=1687034037; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=9d72349e-b6a4-46fd-a358-a2c81835bd3a; tmr_lvid=5575ddaeb39d37be811069a4d1349b68; tmr_lvidTS=1687034040384; advcake_track_id=6a333a53-1395-e22f-3ebf-d95412e5412b; advcake_session_id=23626ba4-53a7-b189-e116-4ab486335cc7; uxs_uid=4aa9db80-0d4e-11ee-ae50-6d99611a2389; flocktory-uuid=ddfbb3c6-beb6-4383-8a01-632236b4392e-5; afUserId=663be7db-4700-4881-b924-77ebdd9e0789-p; adrcid=AYVBc490MiC10QI1M9_KJxg; cookie_ip_add=79.139.209.174; _gid=GA1.2.511097384.1687527353; MVID_ENVCLOUD=prod2; SMSError=; authError=; BIGipServeratg-ps-prod_tcp80=2466569226.20480.0000; bIPs=-314595793; flacktory=no; BIGipServeratg-ps-prod_tcp80_clone=2466569226.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __lhash_=4dc15c1b1cd8f6f3d623e3cb2b9a6d93; AF_SYNC=1687714758733; __rhash_=e2b0718bf684dfed675c2971424efa82; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; _sp_ses.d61c=*; __hash_=b8c2f7d8dc24efed67515dea1f745b35; JSESSIONID=R4wskhyYQYpC6vRDhn6rR5TTSgtzC02yJxvTycLXmVntMjWgc25P!685572310; CACHE_INDICATOR=false; gssc218=; _ym_isad=2; _ym_visorc=w; mindboxDeviceUUID=5fe7c84f-9592-4d88-8fca-60fa0bbd2041; directCrm-session=%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D; gsscgib-w-mvideo=m7OZnTaYP6L0aVw44FLlGsdevSmtPFD5jPPVZXuaUql9bLIGncyBwJs/YUr7tpO8xDK2yQEqid6ntgjZAkJyuwGa1qjKnk+Oz/om5xQvN7Ew8IcoJkQjuKMneEDG8T4+E6wKm1OUjQOzCpA/IVy/0QbunAhfp3kaa9KJfl0Gq3nCccV2vZJM1a0gGWVjwSCHnT+Z8zoriXF42+eu2nqTzKlP5wnnRicB3X6QUuUygHwZFOrxCDWdKmKqQgCB2g==; gsscgib-w-mvideo=m7OZnTaYP6L0aVw44FLlGsdevSmtPFD5jPPVZXuaUql9bLIGncyBwJs/YUr7tpO8xDK2yQEqid6ntgjZAkJyuwGa1qjKnk+Oz/om5xQvN7Ew8IcoJkQjuKMneEDG8T4+E6wKm1OUjQOzCpA/IVy/0QbunAhfp3kaa9KJfl0Gq3nCccV2vZJM1a0gGWVjwSCHnT+Z8zoriXF42+eu2nqTzKlP5wnnRicB3X6QUuUygHwZFOrxCDWdKmKqQgCB2g==; _sp_id.d61c=2a8f65ed-0abf-4d12-bcea-0cdf4026919e.1687527353.12.1687859848.1687784015.3bc6ec58-aaf1-458f-b520-b38a3bdebfc3.1b8c9b52-c913-48ae-b911-e9df50689f72.fd52b527-1b6d-4e31-a38a-85a33424994a.1687859828505.22; _ga_CFMZTSS5FM=GS1.1.1687859829.25.1.1687859847.0.0.0; _ga=GA1.2.838583662.1687527353; tmr_detect=0%7C1687859853585; fgsscgib-w-mvideo=hPqw4eb250b2bf0bf7e35c5a9976bdb1c1804980; fgsscgib-w-mvideo=hPqw4eb250b2bf0bf7e35c5a9976bdb1c1804980; cfidsgib-w-mvideo=KVZpeE/zl/cpIiUz6tYqtd55taF7/ivTC4i2lFaJLGc6QR1NpTxZQBxKa8dk8K7nT/KoO+Dgegt1x/ci5pwMP/hCJoUr42lmLs7VMuwEw184s1LyANjJhMYmSVUs5AzjXNLR0Ls9pXb0VKOfDh0Ji25EhaBV54/z10RVl2O0; _ga_BNX5WPP3YK=GS1.1.1687859829.25.1.1687859854.35.0.0',
        'referer': 'https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65?from=homepage',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'ff9fc318dc1345a4ac051fb7c7817208-a97fd6cf42848546-0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-set-application-id': '1b20578e-bed3-4598-9fc4-08da7ba84694',
    }

    params = {
        'categoryId': '65',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    products_id = response.get('body').get('products')

    json_data = {
        'productIds': products_id,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('tv_data/tv_list.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_names = response.get('body').get('products')

    products_id_str = ','.join(products_id)

    params = {
        'productIds': products_id_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    item_prices = {}
    phone_prices = response.get('body').get('materialPrices')
    for item in phone_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_discount_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        item_prices[item_id] = {
            'item_base_price': item_base_price,
            'item_discount_price': item_discount_price,
            'item_bonus': item_bonus,
            'id': item_id
        }

    item_names = {}
    for item in products_names:
        item_id = item.get('productId')
        item_name = item.get('name')
        item_names[item_id] = {'item_name': item_name, 'id': item_id}

    for i in item_prices:
        for j in item_names:
            if j == i:
                item_prices[j].update(item_names[i])

    with open('tv_prices.json', 'w') as file:
        json.dump(item_prices, file, indent=4, ensure_ascii=False)


def get_characteristics_tv():
    item_characteristics = {}
    shoma_characteristics = {}
    with open('tv_data/tv_list.json') as f2:
        data = json.load(f2)
        for i in data['products']:
            # print(i['productId']) id
            prod_id = i['productId']
            # print(i['brandName']) brand
            item_characteristics[prod_id] = {
                'id': prod_id,
                'brand': i['brandName'],
                'nameTranslit': i['nameTranslit']
            }
            for j in i['propertiesPortion']:
                # print(f"{j['name'] + ' ' + j['value']}", j['name'] + ' ' + j['value'])
                shoma_characteristics[prod_id] = {
                    f"{j['name']}": j['name'] + ' ' + j['value']
                }
                item_characteristics[prod_id].update(shoma_characteristics[prod_id])

    with open('tv_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in item_characteristics:
            prices[i].update(item_characteristics[i])

    with open('tv_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_images_tv():
    with open('tv_data/tv_list.json') as f1:
        prices = json.load(f1)
        phone_images = {}
        for i in prices['products']:
            phone_images[i['productId']] = {
                'image' : 'http://static.mvideo.ru/' + i['images'][0]
            }
    with open('tv_prices.json') as f2:
        prices = json.load(f2)
        for i in prices:
            prices[i].update(phone_images[i])

    with open('tv_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)

    for i in prices:
        img = prices[i]['image']
        resource = urllib.request.urlopen(img)
        out = open(f"pract/renessans_tech/static/pictures/tv/{i}.jpg", 'wb')
        out.write(resource.read())
        out.close()


def get_cashback_laptops():
    with open('laptop_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in prices:
            item_cashback[i] = {'item_cashback': '10%'}
            prices[i].update(item_cashback[i])

    with open('laptop_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def full_data_tv():
    with open('tv_prices.json') as f1:
        prices = json.load(f1)
        smart_tv = {}
        hdr = {}
        for i in prices:
            if 'Поддержка Smart TV' not in prices[i]:
                smart_tv[i] = {"Поддержка Smart TV": "Поддержка Smart TV Нет"}
                prices[i].update(smart_tv[i])
            if 'Технология HDR' not in prices[i]:
                hdr[i] = {"Технология HDR": "Технология HDR Нет"}
                prices[i].update(hdr[i])

    with open('tv_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_data_computers():
    cookies = {
        '__lhash_': '4dc15c1b1cd8f6f3d623e3cb2b9a6d93',
        'MVID_AB_TOP_SERVICES': '1',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_STORE_SORTING': 'true',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLP_GLC': '2',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_RECOMENDATION': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_GUEST_ID': '22635780952',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        '_ym_uid': '1687034037702065663',
        '_ym_d': '1687034037',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '9d72349e-b6a4-46fd-a358-a2c81835bd3a',
        'tmr_lvid': '5575ddaeb39d37be811069a4d1349b68',
        'tmr_lvidTS': '1687034040384',
        'advcake_track_id': '6a333a53-1395-e22f-3ebf-d95412e5412b',
        'advcake_session_id': '23626ba4-53a7-b189-e116-4ab486335cc7',
        'uxs_uid': '4aa9db80-0d4e-11ee-ae50-6d99611a2389',
        'flocktory-uuid': 'ddfbb3c6-beb6-4383-8a01-632236b4392e-5',
        'afUserId': '663be7db-4700-4881-b924-77ebdd9e0789-p',
        'adrcid': 'AYVBc490MiC10QI1M9_KJxg',
        'AF_SYNC': '1687034048415',
        'cookie_ip_add': '79.139.209.174',
        '_gid': 'GA1.2.511097384.1687527353',
        'MVID_ENVCLOUD': 'prod2',
        '_ym_isad': '2',
        'SMSError': '',
        'authError': '',
        '_sp_ses.d61c': '*',
        '__hash_': 'b8c2f7d8dc2e8fb507515dea1f745b35',
        'JSESSIONID': '179GkX0QlYYMphMNhDW1n7dzPzX3RcXfBWr8tRdwhSdsThnn1rHP!1147724801',
        'BIGipServeratg-ps-prod_tcp80': '2466569226.20480.0000',
        'bIPs': '-314595793',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80_clone': '2466569226.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        '_ym_visorc': 'w',
        'CACHE_INDICATOR': 'true',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        'mindboxDeviceUUID': '5fe7c84f-9592-4d88-8fca-60fa0bbd2041',
        'directCrm-session': '%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D',
        '_ga': 'GA1.2.838583662.1687527353',
        'tmr_detect': '0%7C1687630942647',
        '_sp_id.d61c': '2a8f65ed-0abf-4d12-bcea-0cdf4026919e.1687527353.9.1687630952.1687624945.2eb45269-98b8-413a-b27a-99193c0cf772.3b975766-b53c-4849-8f7e-77090389a4dd.b290bcdc-6ee6-4f2c-8e14-2d312badf4cc.1687628823168.37',
        'gssc218': '',
        'gsscgib-w-mvideo': 'bSNGU2P5rHd05eQfBknoQBxH7UeWr8TrUcvfbkOzUavArUzhQUFGlghUpC2NAxp3xDE5efB9vC3a+renojeL4u7KUwMh0cFLLH1kui+UdtCT6hE0wUfyOk+OJN/hEfQd/UpN/VUau+a398J6a2IeVZ18RJFT3z8LD3U9O5Qy2tijY/FjPr/TkUmZRLUywf8zul0Eqoo+1k+s02BA5TOeTkl7x7CVsBwCWQFSRvR2vMBPPIQ+xFfn9HuwtftO3rMLDg==',
        'gsscgib-w-mvideo': 'bSNGU2P5rHd05eQfBknoQBxH7UeWr8TrUcvfbkOzUavArUzhQUFGlghUpC2NAxp3xDE5efB9vC3a+renojeL4u7KUwMh0cFLLH1kui+UdtCT6hE0wUfyOk+OJN/hEfQd/UpN/VUau+a398J6a2IeVZ18RJFT3z8LD3U9O5Qy2tijY/FjPr/TkUmZRLUywf8zul0Eqoo+1k+s02BA5TOeTkl7x7CVsBwCWQFSRvR2vMBPPIQ+xFfn9HuwtftO3rMLDg==',
        '_ga_CFMZTSS5FM': 'GS1.1.1687630894.22.1.1687630969.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1687630894.22.1.1687630969.45.0.0',
        'cfidsgib-w-mvideo': 'BvQ0s1XyfWWh3r8/3A4sQMeC5UkP0fT7kXJmCLQz/PNt8NggUFxYuZ+2fXUjqFfY0JIYSsXSF/6HAVlv8HJkR1LD3VIycmxsy4tHiLJLRhjkWZWky8mzk4E5zmIGUVLtvSuIJA78d0OnrtJbEh3tBx/Z2hoigMSotOMbNvYB',
        'fgsscgib-w-mvideo': 'QLL4408720a1d6172e809f66c0d4161ab07e876a',
        'fgsscgib-w-mvideo': 'QLL4408720a1d6172e809f66c0d4161ab07e876a',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=a3192e67cb2d4c9aa5c36b6f1119816b,sentry-sample_rate=0.5',
        # 'cookie': '__lhash_=4dc15c1b1cd8f6f3d623e3cb2b9a6d93; MVID_AB_TOP_SERVICES=1; MVID_ACTOR_API_AVAILABILITY=true; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLP_GLC=2; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_RECOMENDATION=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_GUEST_ID=22635780952; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=2; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; _ym_uid=1687034037702065663; _ym_d=1687034037; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=9d72349e-b6a4-46fd-a358-a2c81835bd3a; tmr_lvid=5575ddaeb39d37be811069a4d1349b68; tmr_lvidTS=1687034040384; advcake_track_id=6a333a53-1395-e22f-3ebf-d95412e5412b; advcake_session_id=23626ba4-53a7-b189-e116-4ab486335cc7; uxs_uid=4aa9db80-0d4e-11ee-ae50-6d99611a2389; flocktory-uuid=ddfbb3c6-beb6-4383-8a01-632236b4392e-5; afUserId=663be7db-4700-4881-b924-77ebdd9e0789-p; adrcid=AYVBc490MiC10QI1M9_KJxg; AF_SYNC=1687034048415; cookie_ip_add=79.139.209.174; _gid=GA1.2.511097384.1687527353; MVID_ENVCLOUD=prod2; _ym_isad=2; SMSError=; authError=; _sp_ses.d61c=*; __hash_=b8c2f7d8dc2e8fb507515dea1f745b35; JSESSIONID=179GkX0QlYYMphMNhDW1n7dzPzX3RcXfBWr8tRdwhSdsThnn1rHP!1147724801; BIGipServeratg-ps-prod_tcp80=2466569226.20480.0000; bIPs=-314595793; flacktory=no; BIGipServeratg-ps-prod_tcp80_clone=2466569226.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; _ym_visorc=w; CACHE_INDICATOR=true; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; mindboxDeviceUUID=5fe7c84f-9592-4d88-8fca-60fa0bbd2041; directCrm-session=%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D; _ga=GA1.2.838583662.1687527353; tmr_detect=0%7C1687630942647; _sp_id.d61c=2a8f65ed-0abf-4d12-bcea-0cdf4026919e.1687527353.9.1687630952.1687624945.2eb45269-98b8-413a-b27a-99193c0cf772.3b975766-b53c-4849-8f7e-77090389a4dd.b290bcdc-6ee6-4f2c-8e14-2d312badf4cc.1687628823168.37; gssc218=; gsscgib-w-mvideo=bSNGU2P5rHd05eQfBknoQBxH7UeWr8TrUcvfbkOzUavArUzhQUFGlghUpC2NAxp3xDE5efB9vC3a+renojeL4u7KUwMh0cFLLH1kui+UdtCT6hE0wUfyOk+OJN/hEfQd/UpN/VUau+a398J6a2IeVZ18RJFT3z8LD3U9O5Qy2tijY/FjPr/TkUmZRLUywf8zul0Eqoo+1k+s02BA5TOeTkl7x7CVsBwCWQFSRvR2vMBPPIQ+xFfn9HuwtftO3rMLDg==; gsscgib-w-mvideo=bSNGU2P5rHd05eQfBknoQBxH7UeWr8TrUcvfbkOzUavArUzhQUFGlghUpC2NAxp3xDE5efB9vC3a+renojeL4u7KUwMh0cFLLH1kui+UdtCT6hE0wUfyOk+OJN/hEfQd/UpN/VUau+a398J6a2IeVZ18RJFT3z8LD3U9O5Qy2tijY/FjPr/TkUmZRLUywf8zul0Eqoo+1k+s02BA5TOeTkl7x7CVsBwCWQFSRvR2vMBPPIQ+xFfn9HuwtftO3rMLDg==; _ga_CFMZTSS5FM=GS1.1.1687630894.22.1.1687630969.0.0.0; _ga_BNX5WPP3YK=GS1.1.1687630894.22.1.1687630969.45.0.0; cfidsgib-w-mvideo=BvQ0s1XyfWWh3r8/3A4sQMeC5UkP0fT7kXJmCLQz/PNt8NggUFxYuZ+2fXUjqFfY0JIYSsXSF/6HAVlv8HJkR1LD3VIycmxsy4tHiLJLRhjkWZWky8mzk4E5zmIGUVLtvSuIJA78d0OnrtJbEh3tBx/Z2hoigMSotOMbNvYB; fgsscgib-w-mvideo=QLL4408720a1d6172e809f66c0d4161ab07e876a; fgsscgib-w-mvideo=QLL4408720a1d6172e809f66c0d4161ab07e876a',
        'referer': 'https://www.mvideo.ru/komputernaya-tehnika-4107/monobloki-181/f/category=monobloki-603?reff=menu_main',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'a3192e67cb2d4c9aa5c36b6f1119816b-ae3c6b4c2a48becc-0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-gib-fgsscgib-w-mvideo': 'QLL4408720a1d6172e809f66c0d4161ab07e876a',
        'x-gib-gsscgib-w-mvideo': 'bSNGU2P5rHd05eQfBknoQBxH7UeWr8TrUcvfbkOzUavArUzhQUFGlghUpC2NAxp3xDE5efB9vC3a+renojeL4u7KUwMh0cFLLH1kui+UdtCT6hE0wUfyOk+OJN/hEfQd/UpN/VUau+a398J6a2IeVZ18RJFT3z8LD3U9O5Qy2tijY/FjPr/TkUmZRLUywf8zul0Eqoo+1k+s02BA5TOeTkl7x7CVsBwCWQFSRvR2vMBPPIQ+xFfn9HuwtftO3rMLDg==',
        'x-set-application-id': '0ac46c8c-12cc-4c94-aae9-2837bb1f5aa6',
    }

    params = {
        'categoryId': '181',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJjYXRlZ29yeSIsIiIsIm1vbm9ibG9raS02MDMiXQ==',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }


    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    products_id = response.get('body').get('products')

    json_data = {
        'productIds': products_id,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('computers_data/computers_list.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_names = response.get('body').get('products')

    products_id_str = ','.join(products_id)

    params = {
        'productIds': products_id_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    item_prices = {}
    phone_prices = response.get('body').get('materialPrices')
    for item in phone_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_discount_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        item_prices[item_id] = {
            'item_base_price': item_base_price,
            'item_discount_price': item_discount_price,
            'item_bonus': item_bonus,
            'id': item_id
        }

    item_names = {}
    for item in products_names:
        item_id = item.get('productId')
        item_name = item.get('name')
        item_names[item_id] = {'item_name': item_name, 'id': item_id}

    for i in item_prices:
        for j in item_names:
            if j == i:
                item_prices[j].update(item_names[i])

    with open('computers_prices.json', 'w') as file:
        json.dump(item_prices, file, indent=4, ensure_ascii=False)


def get_characteristics_computers():
    item_characteristics = {}
    shoma_characteristics = {}
    with open('computers_data/computers_list.json') as f2:
        data = json.load(f2)
        for i in data['products']:
            # print(i['productId']) id
            prod_id = i['productId']
            # print(i['brandName']) brand
            item_characteristics[prod_id] = {
                'id': prod_id,
                'brand': i['brandName'],
                'nameTranslit': i['nameTranslit']
            }
            for j in i['propertiesPortion']:
                # print(f"{j['name'] + ' ' + j['value']}", j['name'] + ' ' + j['value'])
                shoma_characteristics[prod_id] = {
                    f"{j['name']}": j['name'] + ' ' + j['value']
                }
                item_characteristics[prod_id].update(shoma_characteristics[prod_id])

    with open('computers_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in item_characteristics:
            prices[i].update(item_characteristics[i])

    with open('computers_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_images_computers():
    with open('computers_data/computers_list.json') as f1:
        prices = json.load(f1)
        phone_images = {}
        for i in prices['products']:

            phone_images[i['productId']] = {
                'image': 'http://static.mvideo.ru/' + i['images'][0],
                'image1': 'http://static.mvideo.ru/' + i['images'][1],
                'image2': 'http://static.mvideo.ru/' + i['images'][2],
                'image3': 'http://static.mvideo.ru/' + i['images'][0]
            }
            
    with open('computers_prices.json') as f2:
        prices = json.load(f2)
        for i in prices:
            prices[i].update(phone_images[i])

    with open('computers_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)

    for i in prices:
        img = prices[i]['image']
        img1 = prices[i]['image1']

        resource = urllib.request.urlopen(img)
        out = open(f"pract/renessans_tech/static/pictures/computers/{i}.jpg", 'wb')
        out.write(resource.read())
        out.close()

        resource = urllib.request.urlopen(img1)
        out = open(f"pract/renessans_tech/static/pictures/computers/img1/{i}.jpg", 'wb')
        out.write(resource.read())
        JPGimg = Image.open(f"pract/renessans_tech/static/pictures/computers/img1/{i}.jpg")
        JPGimg.save(f"pract/renessans_tech/static/pictures/computers/img1/{i}" + '.AVIF', 'AVIF')
        os.remove(f"pract/renessans_tech/static/pictures/computers/img1/{i}.jpg")
        out.close()

        img2 = prices[i]['image2']
        img3 = prices[i]['image3']
        resource = urllib.request.urlopen(img2)
        out = open(f"pract/renessans_tech/static/pictures/computers/img2/{i}.jpg", 'wb')
        out.write(resource.read())
        JPGimg = Image.open(f"pract/renessans_tech/static/pictures/computers/img2/{i}.jpg")
        JPGimg.save(f"pract/renessans_tech/static/pictures/computers/img2/{i}" + '.AVIF', 'AVIF')
        os.remove(f"pract/renessans_tech/static/pictures/computers/img2/{i}.jpg")
        out.close()

        resource = urllib.request.urlopen(img3)
        out = open(f"pract/renessans_tech/static/pictures/computers/img3/{i}.jpg", 'wb')
        out.write(resource.read())
        JPGimg = Image.open(f"pract/renessans_tech/static/pictures/computers/img3/{i}.jpg")
        JPGimg.save(f"pract/renessans_tech/static/pictures/computers/img3/{i}" + '.AVIF', 'AVIF')
        os.remove(f"pract/renessans_tech/static/pictures/computers/img3/{i}.jpg")
        out.close()


def get_cashback_computers():
    with open('computers_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in prices:
            item_cashback[i] = {'item_cashback': '5%'}
            prices[i].update(item_cashback[i])

    with open('computers_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def full_data_computers():
    with open('computers_prices.json') as f1:
        prices = json.load(f1)
        proc = {}
        ram = {}
        comtroller = {}
        ssd = {}
        hdd = {}
        for i in prices:
            if 'Тип процессора' not in prices[i]:
                proc[i] = {"Тип процессора": "Не указан"}
                prices[i].update(proc[i])
            if 'Оперативная память (RAM)' not in prices[i]:
                ram[i] = {"Оперативная память (RAM)": "Не указана"}
                prices[i].update(ram[i])
            if 'Графический контроллер' not in prices[i]:
                comtroller[i] = {"Графический контроллер": "Не указан"}
                prices[i].update(comtroller[i])
            if 'Объем SSD' not in prices[i]:
                ssd[i] = {"Объем SSD": "Не указан"}
                prices[i].update(ssd[i])
            if 'Объем HDD' not in prices[i]:
                hdd[i] = {"Объем HDD": "Не указан"}
                prices[i].update(hdd[i])

    with open('computers_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_data_tablets():
    cookies = {
        '__lhash_': '4dc15c1b1cd8f6f3d623e3cb2b9a6d93',
        'MVID_AB_TOP_SERVICES': '1',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_STORE_SORTING': 'true',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLP_GLC': '2',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_RECOMENDATION': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_GUEST_ID': '22635780952',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        '_ym_uid': '1687034037702065663',
        '_ym_d': '1687034037',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '9d72349e-b6a4-46fd-a358-a2c81835bd3a',
        'tmr_lvid': '5575ddaeb39d37be811069a4d1349b68',
        'tmr_lvidTS': '1687034040384',
        'advcake_track_id': '6a333a53-1395-e22f-3ebf-d95412e5412b',
        'advcake_session_id': '23626ba4-53a7-b189-e116-4ab486335cc7',
        'uxs_uid': '4aa9db80-0d4e-11ee-ae50-6d99611a2389',
        'flocktory-uuid': 'ddfbb3c6-beb6-4383-8a01-632236b4392e-5',
        'afUserId': '663be7db-4700-4881-b924-77ebdd9e0789-p',
        'adrcid': 'AYVBc490MiC10QI1M9_KJxg',
        'AF_SYNC': '1687034048415',
        'cookie_ip_add': '79.139.209.174',
        '_gid': 'GA1.2.511097384.1687527353',
        'MVID_ENVCLOUD': 'prod2',
        '_ym_isad': '2',
        'SMSError': '',
        'authError': '',
        '_sp_ses.d61c': '*',
        'BIGipServeratg-ps-prod_tcp80': '2466569226.20480.0000',
        'bIPs': '-314595793',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80_clone': '2466569226.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        '_ym_visorc': 'w',
        'tmr_detect': '0%7C1687630988083',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        '__rhash_': 'e2b0718bf68f0fb5f75c2971424efa82',
        'gssc218': '',
        '__hash_': 'b8c2f7d8dc2f5fb5f7515dea1f745b35',
        'JSESSIONID': '0cyhkX7pplrcbLz8m22cvpy6y3KD5DwJ13lTynJPTnDgp2k2VBBv!1147724801',
        'CACHE_INDICATOR': 'false',
        'mindboxDeviceUUID': '5fe7c84f-9592-4d88-8fca-60fa0bbd2041',
        'directCrm-session': '%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D',
        'gsscgib-w-mvideo': 'jt9pJdbir8JU96NLB6TEu+6TLYJOKc9yo9ym2khkCIxjE4jL/xbfqgYPoGg53gqKlsq5e1jCpoOB7i8bJ4JkrnH83/Vqw+bRQmV/cyRLIEUAkUUz7b6Fy+Q8T9nJ7PFBmMGCUKvkUvh+TvbfkB/Hp7CgdhsCRhdlxK1vhoPM1uszQlHL6xSNTNn+zdyjO04tCqpcjIkXAhv1nrkEOI9FPsfTxj1/CUNEVIvYFtgSf216vXyTs3LscUIvF3mN+kLelg==',
        'gsscgib-w-mvideo': 'jt9pJdbir8JU96NLB6TEu+6TLYJOKc9yo9ym2khkCIxjE4jL/xbfqgYPoGg53gqKlsq5e1jCpoOB7i8bJ4JkrnH83/Vqw+bRQmV/cyRLIEUAkUUz7b6Fy+Q8T9nJ7PFBmMGCUKvkUvh+TvbfkB/Hp7CgdhsCRhdlxK1vhoPM1uszQlHL6xSNTNn+zdyjO04tCqpcjIkXAhv1nrkEOI9FPsfTxj1/CUNEVIvYFtgSf216vXyTs3LscUIvF3mN+kLelg==',
        '_sp_id.d61c': '2a8f65ed-0abf-4d12-bcea-0cdf4026919e.1687527353.9.1687632681.1687624945.2eb45269-98b8-413a-b27a-99193c0cf772.3b975766-b53c-4849-8f7e-77090389a4dd.b290bcdc-6ee6-4f2c-8e14-2d312badf4cc.1687628823168.69',
        '_ga_CFMZTSS5FM': 'GS1.1.1687630894.22.1.1687632680.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1687630894.22.1.1687632680.43.0.0',
        '_ga': 'GA1.2.838583662.1687527353',
        'cfidsgib-w-mvideo': 'cUu1XTZC2E/mZrU/Ig0D/I4HcSvHW1I8JuWlEtMyk+YYu8H7I1WM13N2jyHG7bx8jOjcgE+wazvEpUGgMj0pIEZWf+aYTUTLLJRbf/OmBU4aBj+VUhM21tiH12QaTSc8mgNRrumC/dtjZTqoXjX7YPufbxC1nsxAdWuHiR1A',
        'fgsscgib-w-mvideo': 'TOjUac5e6840649d27320ae1f9ad07da4f6d145d',
        'fgsscgib-w-mvideo': 'TOjUac5e6840649d27320ae1f9ad07da4f6d145d',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=6a88a932c9db452e91368aceb9a9fdcc,sentry-sample_rate=0.5',
        # 'cookie': '__lhash_=4dc15c1b1cd8f6f3d623e3cb2b9a6d93; MVID_AB_TOP_SERVICES=1; MVID_ACTOR_API_AVAILABILITY=true; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLP_GLC=2; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_RECOMENDATION=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_GUEST_ID=22635780952; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=2; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; _ym_uid=1687034037702065663; _ym_d=1687034037; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=9d72349e-b6a4-46fd-a358-a2c81835bd3a; tmr_lvid=5575ddaeb39d37be811069a4d1349b68; tmr_lvidTS=1687034040384; advcake_track_id=6a333a53-1395-e22f-3ebf-d95412e5412b; advcake_session_id=23626ba4-53a7-b189-e116-4ab486335cc7; uxs_uid=4aa9db80-0d4e-11ee-ae50-6d99611a2389; flocktory-uuid=ddfbb3c6-beb6-4383-8a01-632236b4392e-5; afUserId=663be7db-4700-4881-b924-77ebdd9e0789-p; adrcid=AYVBc490MiC10QI1M9_KJxg; AF_SYNC=1687034048415; cookie_ip_add=79.139.209.174; _gid=GA1.2.511097384.1687527353; MVID_ENVCLOUD=prod2; _ym_isad=2; SMSError=; authError=; _sp_ses.d61c=*; BIGipServeratg-ps-prod_tcp80=2466569226.20480.0000; bIPs=-314595793; flacktory=no; BIGipServeratg-ps-prod_tcp80_clone=2466569226.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; _ym_visorc=w; tmr_detect=0%7C1687630988083; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; __rhash_=e2b0718bf68f0fb5f75c2971424efa82; gssc218=; __hash_=b8c2f7d8dc2f5fb5f7515dea1f745b35; JSESSIONID=0cyhkX7pplrcbLz8m22cvpy6y3KD5DwJ13lTynJPTnDgp2k2VBBv!1147724801; CACHE_INDICATOR=false; mindboxDeviceUUID=5fe7c84f-9592-4d88-8fca-60fa0bbd2041; directCrm-session=%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D; gsscgib-w-mvideo=jt9pJdbir8JU96NLB6TEu+6TLYJOKc9yo9ym2khkCIxjE4jL/xbfqgYPoGg53gqKlsq5e1jCpoOB7i8bJ4JkrnH83/Vqw+bRQmV/cyRLIEUAkUUz7b6Fy+Q8T9nJ7PFBmMGCUKvkUvh+TvbfkB/Hp7CgdhsCRhdlxK1vhoPM1uszQlHL6xSNTNn+zdyjO04tCqpcjIkXAhv1nrkEOI9FPsfTxj1/CUNEVIvYFtgSf216vXyTs3LscUIvF3mN+kLelg==; gsscgib-w-mvideo=jt9pJdbir8JU96NLB6TEu+6TLYJOKc9yo9ym2khkCIxjE4jL/xbfqgYPoGg53gqKlsq5e1jCpoOB7i8bJ4JkrnH83/Vqw+bRQmV/cyRLIEUAkUUz7b6Fy+Q8T9nJ7PFBmMGCUKvkUvh+TvbfkB/Hp7CgdhsCRhdlxK1vhoPM1uszQlHL6xSNTNn+zdyjO04tCqpcjIkXAhv1nrkEOI9FPsfTxj1/CUNEVIvYFtgSf216vXyTs3LscUIvF3mN+kLelg==; _sp_id.d61c=2a8f65ed-0abf-4d12-bcea-0cdf4026919e.1687527353.9.1687632681.1687624945.2eb45269-98b8-413a-b27a-99193c0cf772.3b975766-b53c-4849-8f7e-77090389a4dd.b290bcdc-6ee6-4f2c-8e14-2d312badf4cc.1687628823168.69; _ga_CFMZTSS5FM=GS1.1.1687630894.22.1.1687632680.0.0.0; _ga_BNX5WPP3YK=GS1.1.1687630894.22.1.1687632680.43.0.0; _ga=GA1.2.838583662.1687527353; cfidsgib-w-mvideo=cUu1XTZC2E/mZrU/Ig0D/I4HcSvHW1I8JuWlEtMyk+YYu8H7I1WM13N2jyHG7bx8jOjcgE+wazvEpUGgMj0pIEZWf+aYTUTLLJRbf/OmBU4aBj+VUhM21tiH12QaTSc8mgNRrumC/dtjZTqoXjX7YPufbxC1nsxAdWuHiR1A; fgsscgib-w-mvideo=TOjUac5e6840649d27320ae1f9ad07da4f6d145d; fgsscgib-w-mvideo=TOjUac5e6840649d27320ae1f9ad07da4f6d145d',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195?from=homepage',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '6a88a932c9db452e91368aceb9a9fdcc-93ea1527663658ef-1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-gib-fgsscgib-w-mvideo': 'TOjUac5e6840649d27320ae1f9ad07da4f6d145d',
        'x-gib-gsscgib-w-mvideo': 'jt9pJdbir8JU96NLB6TEu+6TLYJOKc9yo9ym2khkCIxjE4jL/xbfqgYPoGg53gqKlsq5e1jCpoOB7i8bJ4JkrnH83/Vqw+bRQmV/cyRLIEUAkUUz7b6Fy+Q8T9nJ7PFBmMGCUKvkUvh+TvbfkB/Hp7CgdhsCRhdlxK1vhoPM1uszQlHL6xSNTNn+zdyjO04tCqpcjIkXAhv1nrkEOI9FPsfTxj1/CUNEVIvYFtgSf216vXyTs3LscUIvF3mN+kLelg==',
        'x-set-application-id': '6a61b39f-b2fe-4c2a-b377-14cf90294e59',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    products_id = response.get('body').get('products')

    json_data = {
        'productIds': products_id,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('tablets_data/tablets_list.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_names = response.get('body').get('products')

    products_id_str = ','.join(products_id)

    params = {
        'productIds': products_id_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    item_prices = {}
    phone_prices = response.get('body').get('materialPrices')
    for item in phone_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_discount_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        item_prices[item_id] = {
            'item_base_price': item_base_price,
            'item_discount_price': item_discount_price,
            'item_bonus': item_bonus,
            'id': item_id
        }

    item_names = {}
    for item in products_names:
        item_id = item.get('productId')
        item_name = item.get('name')
        item_names[item_id] = {'item_name': item_name, 'id': item_id}

    for i in item_prices:
        for j in item_names:
            if j == i:
                item_prices[j].update(item_names[i])

    with open('tablets_prices.json', 'w') as file:
        json.dump(item_prices, file, indent=4, ensure_ascii=False)


def get_characteristics_tablets():
    item_characteristics = {}
    shoma_characteristics = {}
    with open('tablets_data/tablets_list.json') as f2:
        data = json.load(f2)
        for i in data['products']:
            # print(i['productId']) id
            prod_id = i['productId']
            # print(i['brandName']) brand
            item_characteristics[prod_id] = {
                'id': prod_id,
                'brand': i['brandName'],
                'nameTranslit': i['nameTranslit']
            }
            for j in i['propertiesPortion']:
                # print(f"{j['name'] + ' ' + j['value']}", j['name'] + ' ' + j['value'])
                shoma_characteristics[prod_id] = {
                    f"{j['name']}": j['name'] + ' ' + j['value']
                }
                item_characteristics[prod_id].update(shoma_characteristics[prod_id])

    with open('tablets_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in item_characteristics:
            prices[i].update(item_characteristics[i])

    with open('tablets_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_images_tablets():
    with open('tablets_data/tablets_list.json') as f1:
        prices = json.load(f1)
        phone_images = {}
        for i in prices['products']:
            phone_images[i['productId']] = {
                'image' : 'http://static.mvideo.ru/' + i['images'][0]
            }
    with open('tablets_prices.json') as f2:
        prices = json.load(f2)
        for i in prices:
            prices[i].update(phone_images[i])

    with open('tablets_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)

    for i in prices:
        img = prices[i]['image']
        resource = urllib.request.urlopen(img)
        out = open(f"pract/renessans_tech/static/pictures/tablets/{i}.jpg", 'wb')
        out.write(resource.read())
        out.close()


def get_cashback_tablets():
    with open('tablets_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in prices:
            item_cashback[i] = {'item_cashback': '7%'}
            prices[i].update(item_cashback[i])

    with open('tablets_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def full_data_tablets():
    with open('tablets_prices.json') as f1:
        prices = json.load(f1)
        ram = {}
        yadra = {}
        proc = {}
        for i in prices:
            if 'Оперативная память (RAM)' not in prices[i]:
                ram[i] = {"Оперативная память (RAM)": "Не указана"}
                prices[i].update(ram[i])
            if 'Количество ядер' not in prices[i]:
                yadra[i] = {"Количество ядер": "Не указано"}
                prices[i].update(yadra[i])
            if 'Частота процессора' not in prices[i]:
                proc[i] = {"Частота процессора": "Не указана"}
                prices[i].update(proc[i])

    with open('tablets_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_data_accessories():
    cookies = {
        '__lhash_': '4dc15c1b1cd8f6f3d623e3cb2b9a6d93',
        'MVID_AB_TOP_SERVICES': '1',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_STORE_SORTING': 'true',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLP_GLC': '2',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_RECOMENDATION': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_GUEST_ID': '22635780952',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        '_ym_uid': '1687034037702065663',
        '_ym_d': '1687034037',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '9d72349e-b6a4-46fd-a358-a2c81835bd3a',
        'tmr_lvid': '5575ddaeb39d37be811069a4d1349b68',
        'tmr_lvidTS': '1687034040384',
        'advcake_track_id': '6a333a53-1395-e22f-3ebf-d95412e5412b',
        'advcake_session_id': '23626ba4-53a7-b189-e116-4ab486335cc7',
        'uxs_uid': '4aa9db80-0d4e-11ee-ae50-6d99611a2389',
        'flocktory-uuid': 'ddfbb3c6-beb6-4383-8a01-632236b4392e-5',
        'afUserId': '663be7db-4700-4881-b924-77ebdd9e0789-p',
        'adrcid': 'AYVBc490MiC10QI1M9_KJxg',
        'AF_SYNC': '1687034048415',
        'cookie_ip_add': '79.139.209.174',
        '_gid': 'GA1.2.511097384.1687527353',
        'MVID_ENVCLOUD': 'prod2',
        '_ym_isad': '2',
        'SMSError': '',
        'authError': '',
        '_sp_ses.d61c': '*',
        'BIGipServeratg-ps-prod_tcp80': '2466569226.20480.0000',
        'bIPs': '-314595793',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80_clone': '2466569226.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        '_ym_visorc': 'w',
        'JSESSIONID': 'J2dJkXBXGCZGfv96mphpLqhQ2FPltLHnDfS727YzLQWtkdnYDgbh!1147724801',
        '__hash_': 'b8c2f7d8dc23efb267515dea1f745b35',
        'CACHE_INDICATOR': 'true',
        '_dc_gtm_UA-1873769-37': '1',
        '_dc_gtm_UA-1873769-1': '1',
        'gssc218': '',
        'mindboxDeviceUUID': '5fe7c84f-9592-4d88-8fca-60fa0bbd2041',
        'directCrm-session': '%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D',
        'gsscgib-w-mvideo': '3v+BX278OCmuAe+FJfBndrUHx74kAz178Js3qyePuQEpuoiwXokTjtNHHEzFNflBqc7aT0A2JPET25wtUNeTirKOmAp7GKjiD5hD7BFq8uutnXRuQzdizkS70uuyBXbhF0DCPlg/XSAEL8J8NjVUsuzKiNSylmVYKa2Zr2AOb1mR4v7X48NANX0hc1ZXFkkgAy48s8bYdIDoJGJOfx1Tmw0AC1CpEeljQmdhxgUpMCUPpAU7LOz1eSLkecDSli3wWg==',
        'gsscgib-w-mvideo': '3v+BX278OCmuAe+FJfBndrUHx74kAz178Js3qyePuQEpuoiwXokTjtNHHEzFNflBqc7aT0A2JPET25wtUNeTirKOmAp7GKjiD5hD7BFq8uutnXRuQzdizkS70uuyBXbhF0DCPlg/XSAEL8J8NjVUsuzKiNSylmVYKa2Zr2AOb1mR4v7X48NANX0hc1ZXFkkgAy48s8bYdIDoJGJOfx1Tmw0AC1CpEeljQmdhxgUpMCUPpAU7LOz1eSLkecDSli3wWg==',
        '_sp_id.d61c': '2a8f65ed-0abf-4d12-bcea-0cdf4026919e.1687527353.9.1687635036.1687624945.2eb45269-98b8-413a-b27a-99193c0cf772.3b975766-b53c-4849-8f7e-77090389a4dd.b290bcdc-6ee6-4f2c-8e14-2d312badf4cc.1687628823168.129',
        '_ga': 'GA1.2.838583662.1687527353',
        'tmr_detect': '0%7C1687635042616',
        '_ga_CFMZTSS5FM': 'GS1.1.1687630894.22.1.1687635043.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1687630894.22.1.1687635043.49.0.0',
        'cfidsgib-w-mvideo': 'KjRaYstiNG9HkLQvBlb7SpgP+828vrh1wJPrpllxFMgHsvsf5D3LeD0E7l5lpVejgMKI1N5/PnzcbhNlp4ViYSUzHViw/71s7z3caYT2cWRrLWSItMF8pEUlwE4gKRNsuZj4gau19aBtFtuIgc4uihMroZHQmFH58texeseS',
        'fgsscgib-w-mvideo': 'jH4Ae871c588f5b8a10e2f9eaf511a6f7b42d512',
        'fgsscgib-w-mvideo': 'jH4Ae871c588f5b8a10e2f9eaf511a6f7b42d512',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=6a78d423feb648279c2879e00d7d0767,sentry-sample_rate=0.5',
        # 'cookie': '__lhash_=4dc15c1b1cd8f6f3d623e3cb2b9a6d93; MVID_AB_TOP_SERVICES=1; MVID_ACTOR_API_AVAILABILITY=true; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLP_GLC=2; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_RECOMENDATION=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_GUEST_ID=22635780952; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=2; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; _ym_uid=1687034037702065663; _ym_d=1687034037; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=9d72349e-b6a4-46fd-a358-a2c81835bd3a; tmr_lvid=5575ddaeb39d37be811069a4d1349b68; tmr_lvidTS=1687034040384; advcake_track_id=6a333a53-1395-e22f-3ebf-d95412e5412b; advcake_session_id=23626ba4-53a7-b189-e116-4ab486335cc7; uxs_uid=4aa9db80-0d4e-11ee-ae50-6d99611a2389; flocktory-uuid=ddfbb3c6-beb6-4383-8a01-632236b4392e-5; afUserId=663be7db-4700-4881-b924-77ebdd9e0789-p; adrcid=AYVBc490MiC10QI1M9_KJxg; AF_SYNC=1687034048415; cookie_ip_add=79.139.209.174; _gid=GA1.2.511097384.1687527353; MVID_ENVCLOUD=prod2; _ym_isad=2; SMSError=; authError=; _sp_ses.d61c=*; BIGipServeratg-ps-prod_tcp80=2466569226.20480.0000; bIPs=-314595793; flacktory=no; BIGipServeratg-ps-prod_tcp80_clone=2466569226.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; _ym_visorc=w; JSESSIONID=J2dJkXBXGCZGfv96mphpLqhQ2FPltLHnDfS727YzLQWtkdnYDgbh!1147724801; __hash_=b8c2f7d8dc23efb267515dea1f745b35; CACHE_INDICATOR=true; _dc_gtm_UA-1873769-37=1; _dc_gtm_UA-1873769-1=1; gssc218=; mindboxDeviceUUID=5fe7c84f-9592-4d88-8fca-60fa0bbd2041; directCrm-session=%7B%22deviceGuid%22%3A%225fe7c84f-9592-4d88-8fca-60fa0bbd2041%22%7D; gsscgib-w-mvideo=3v+BX278OCmuAe+FJfBndrUHx74kAz178Js3qyePuQEpuoiwXokTjtNHHEzFNflBqc7aT0A2JPET25wtUNeTirKOmAp7GKjiD5hD7BFq8uutnXRuQzdizkS70uuyBXbhF0DCPlg/XSAEL8J8NjVUsuzKiNSylmVYKa2Zr2AOb1mR4v7X48NANX0hc1ZXFkkgAy48s8bYdIDoJGJOfx1Tmw0AC1CpEeljQmdhxgUpMCUPpAU7LOz1eSLkecDSli3wWg==; gsscgib-w-mvideo=3v+BX278OCmuAe+FJfBndrUHx74kAz178Js3qyePuQEpuoiwXokTjtNHHEzFNflBqc7aT0A2JPET25wtUNeTirKOmAp7GKjiD5hD7BFq8uutnXRuQzdizkS70uuyBXbhF0DCPlg/XSAEL8J8NjVUsuzKiNSylmVYKa2Zr2AOb1mR4v7X48NANX0hc1ZXFkkgAy48s8bYdIDoJGJOfx1Tmw0AC1CpEeljQmdhxgUpMCUPpAU7LOz1eSLkecDSli3wWg==; _sp_id.d61c=2a8f65ed-0abf-4d12-bcea-0cdf4026919e.1687527353.9.1687635036.1687624945.2eb45269-98b8-413a-b27a-99193c0cf772.3b975766-b53c-4849-8f7e-77090389a4dd.b290bcdc-6ee6-4f2c-8e14-2d312badf4cc.1687628823168.129; _ga=GA1.2.838583662.1687527353; tmr_detect=0%7C1687635042616; _ga_CFMZTSS5FM=GS1.1.1687630894.22.1.1687635043.0.0.0; _ga_BNX5WPP3YK=GS1.1.1687630894.22.1.1687635043.49.0.0; cfidsgib-w-mvideo=KjRaYstiNG9HkLQvBlb7SpgP+828vrh1wJPrpllxFMgHsvsf5D3LeD0E7l5lpVejgMKI1N5/PnzcbhNlp4ViYSUzHViw/71s7z3caYT2cWRrLWSItMF8pEUlwE4gKRNsuZj4gau19aBtFtuIgc4uihMroZHQmFH58texeseS; fgsscgib-w-mvideo=jH4Ae871c588f5b8a10e2f9eaf511a6f7b42d512; fgsscgib-w-mvideo=jH4Ae871c588f5b8a10e2f9eaf511a6f7b42d512',
        'referer': 'https://www.mvideo.ru/aksessuary-dlya-telefonov-58/chehly-dlya-telefonov-342?reff=menu_main_acc',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '6a78d423feb648279c2879e00d7d0767-a9568910e15872c1-0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-gib-fgsscgib-w-mvideo': 'jH4Ae871c588f5b8a10e2f9eaf511a6f7b42d512',
        'x-gib-gsscgib-w-mvideo': '3v+BX278OCmuAe+FJfBndrUHx74kAz178Js3qyePuQEpuoiwXokTjtNHHEzFNflBqc7aT0A2JPET25wtUNeTirKOmAp7GKjiD5hD7BFq8uutnXRuQzdizkS70uuyBXbhF0DCPlg/XSAEL8J8NjVUsuzKiNSylmVYKa2Zr2AOb1mR4v7X48NANX0hc1ZXFkkgAy48s8bYdIDoJGJOfx1Tmw0AC1CpEeljQmdhxgUpMCUPpAU7LOz1eSLkecDSli3wWg==',
        'x-set-application-id': 'fb21cc9b-5edc-4d3c-8054-74cbe98b6697',
    }

    params = {
        'categoryId': '342',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    products_id = response.get('body').get('products')

    json_data = {
        'productIds': products_id,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('accessories_data/accessories_list.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_names = response.get('body').get('products')

    products_id_str = ','.join(products_id)

    params = {
        'productIds': products_id_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    item_prices = {}
    phone_prices = response.get('body').get('materialPrices')
    for item in phone_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_discount_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        item_prices[item_id] = {
            'item_base_price': item_base_price,
            'item_discount_price': item_discount_price,
            'item_bonus': item_bonus,
            'id': item_id
        }

    item_names = {}
    for item in products_names:
        item_id = item.get('productId')
        item_name = item.get('name')
        item_names[item_id] = {'item_name': item_name, 'id': item_id}

    for i in item_prices:
        for j in item_names:
            if j == i:
                item_prices[j].update(item_names[i])

    with open('accessories_prices.json', 'w') as file:
        json.dump(item_prices, file, indent=4, ensure_ascii=False)


def get_characteristics_accessories():
    item_characteristics = {}
    shoma_characteristics = {}
    with open('accessories_data/accessories_list.json') as f2:
        data = json.load(f2)
        for i in data['products']:
            # print(i['productId']) id
            prod_id = i['productId']
            # print(i['brandName']) brand
            item_characteristics[prod_id] = {
                'id': prod_id,
                'brand': i['brandName'],
                'nameTranslit': i['nameTranslit']
            }
            for j in i['propertiesPortion']:
                # print(f"{j['name'] + ' ' + j['value']}", j['name'] + ' ' + j['value'])
                shoma_characteristics[prod_id] = {
                    f"{j['name']}": j['name'] + ' ' + j['value']
                }
                item_characteristics[prod_id].update(shoma_characteristics[prod_id])

    with open('accessories_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in item_characteristics:
            prices[i].update(item_characteristics[i])

    with open('accessories_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_images_accessories():
    with open('accessories_data/accessories_list.json') as f1:
        prices = json.load(f1)
        phone_images = {}
        for i in prices['products']:
            phone_images[i['productId']] = {
                'image' : 'http://static.mvideo.ru/' + i['images'][0]
            }
    with open('accessories_prices.json') as f2:
        prices = json.load(f2)
        for i in prices:
            prices[i].update(phone_images[i])

    with open('accessories_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)

    for i in prices:
        img = prices[i]['image']
        resource = urllib.request.urlopen(img)
        out = open(f"pract/renessans_tech/static/pictures/accessories/{i}.jpg", 'wb')
        out.write(resource.read())
        out.close()


def get_cashback_accessories():
    with open('accessories_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in prices:
            item_cashback[i] = {'item_cashback': '30%'}
            prices[i].update(item_cashback[i])

    with open('accessories_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def full_data_accessories():
    with open('accessories_prices.json') as f1:
        prices = json.load(f1)
        screen = {}
        suits = {}
        type = {}
        material = {}
        for i in prices:
            if 'Для моделей с диагональю экрана' not in prices[i]:
                screen[i] = {"Для моделей с диагональю экрана": "Не указано"}
                prices[i].update(screen[i])
            if 'Подходит для' not in prices[i]:
                suits[i] = {"Подходит для": "Не указано"}
                prices[i].update(suits[i])
            if 'Тип корпуса' not in prices[i]:
                type[i] = {"Тип корпуса": "Не указан"}
                prices[i].update(type[i])
            if 'Материал чехла' not in prices[i]:
                material[i] = {"Материал чехла": "Не указан"}
                prices[i].update(material[i])

    with open('accessories_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)

def clear_screen_data():
    with open('phone_prices.json') as f1:
        prices = json.load(f1)
        new_screens = {}
        for i in prices:
            if '"' in prices[i]['Экран']:
                new_screens[i] = {
                    'Экран' : prices[i]['Экран'].replace('"', '')
                }
                prices[i].update(new_screens[i])
        with open('phone_prices.json', 'w') as file:
            json.dump(prices, file, indent=4, ensure_ascii=False)


def full_data_phones():
    with open('phone_prices.json') as f1:
        prices = json.load(f1)
        proc = {}
        techn_screen = {}
        type_proc = {}
        front_cam = {}
        ram = {}
        for i in prices:
            if 'Процессор' not in prices[i]:
                proc[i] = {"Процессор": "Не указан"}
                prices[i].update(proc[i])
            if 'Технология экрана' not in prices[i]:
                techn_screen[i] = {"Технология экрана": "Не указана"}
                prices[i].update(techn_screen[i])
            if 'Тип процессора' not in prices[i]:
                type_proc[i] = {"Тип процессора": "Не указан"}
                prices[i].update(type_proc[i])
            if 'Фронтальная камера МПик' not in prices[i]:
                front_cam[i] = {"Фронтальная камера МПик": "Не указана"}
                prices[i].update(front_cam[i])
            if 'Оперативная память (RAM)' not in prices[i]:
                ram[i] = {"Оперативная память (RAM)": "Не указана"}
                prices[i].update(ram[i])

    with open('phone_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def full_data_laptops():
    with open('laptop_prices.json') as f1:
        prices = json.load(f1)
        graph_contr = {}
        ssd = {}
        akk = {}
        sens_screen = {}
        for i in prices:
            if 'Графический контроллер' not in prices[i]:
                graph_contr[i] = {"Графический контроллер": "Не указан"}
                prices[i].update(graph_contr[i])
            if 'Объем SSD' not in prices[i]:
                ssd[i] = {'Объем SSD' : 'Не указан'}
                prices[i].update(ssd[i])
            if 'Работа от аккумулятора' not in prices[i]:
                akk[i] = {'Работа от аккумулятора' : 'Не указано'}
                prices[i].update(akk[i])
            if 'Сенсорный экран' not in prices[i]:
                sens_screen[i] = {'Сенсорный экран' : 'Не указан'}
                prices[i].update(sens_screen[i])

    with open('laptop_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)

def full_data_tvs():
    with open('tv_prices.json') as f1:
        prices = json.load(f1)
        diag = {}
        proc_type = {}
        ram = {}
        graph_proc = {}
        ssd = {}
        bl = {}
        qled = {}
        os = {}
        usb_a = {}
        usb = {}
        oled = {}
        for i in prices:
            if 'Экран' not in prices[i]:
                diag[i] = {'Экран': 'Не указан'}
                prices[i].update(diag[i])
            if 'Частота обновления' not in prices[i]:
                proc_type[i] = {'Частота обновления': 'Не указана'}
                prices[i].update(proc_type[i])
            if 'Поддержка Smart TV' not in prices[i]:
                ram[i] = {'Поддержка Smart TV': 'Не указана'}
                prices[i].update(ram[i])
            if 'Технология HDR' not in prices[i]:
                graph_proc[i] = {'Технология HDR': 'Не указано'}
                prices[i].update(graph_proc[i])
            if 'Мощность фронтальных АС' not in prices[i]:
                ssd[i] = {'Мощность фронтальных АС': 'Не указана'}
                prices[i].update(ssd[i])
            if 'Встроенный модуль Bluetooth' not in prices[i]:
                bl[i] = {'Встроенный модуль Bluetooth': 'Не указан'}
                prices[i].update(bl[i])
            if 'Технология QLED' not in prices[i]:
                qled[i] = {'Технология QLED': 'Не указана'}
                prices[i].update(qled[i])
            if 'Операционная система' not in prices[i]:
                os[i] = {'Операционная система': 'Не указана'}
                prices[i].update(os[i])
            if 'Порт USB 2.0 тип A' not in prices[i]:
                usb_a[i] = {'Порт USB 2.0 тип A': 'Не указан'}
                prices[i].update(usb_a[i])
            if 'Воспроизведение с USB' not in prices[i]:
                usb[i] = {'Воспроизведение с USB': 'Не указано'}
                prices[i].update(usb[i])
            if 'Технология OLED' not in prices[i]:
                oled[i] = {'Технология OLED': 'Не указана'}
                prices[i].update(oled[i])






    with open('tv_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def full_data_computers():
    with open('computers_prices.json') as f1:
        prices = json.load(f1)
        mas = []
        add_item = []
        for i in prices:
            for j in list(prices[i].keys()):
                if j not in mas and j != 'Объем HDD':
                    mas.append(j)

        for i in prices:
            for j in mas:
                if j not in prices[i] :
                    add_item[i] = {j: 'Не указано'}
                    prices[i].update(add_item[i])

    with open('computers_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def full_data_tablets():
    with open('tablets_prices.json') as f1:
        prices = json.load(f1)
        rom = []
        ram = []
        y = []
        proc = []
        t = []
        wifi = []
        bl = []
        camera = []
        for i in prices:
            if 'Встроенная память (ROM)' not in prices[i]:
                rom[i] = {'Встроенная память (ROM)': 'Не указана'}
                prices[i].update(rom[i])
            if 'Оперативная память (RAM)' not in prices[i]:
                ram[i] = {'Оперативная память (RAM)': 'Не указана'}
                prices[i].update(ram[i])
            if 'Количество ядер' not in prices[i]:
                y[i] = {'Количество ядер': 'Не указано'}
                prices[i].update(y[i])
            if 'Частота процессора' not in prices[i]:
                proc[i] = {'Частота процессора': 'Не указано'}
                prices[i].update(proc[i])
    with open('tablets_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def full_data_accessories():
    with open('accessories_prices.json') as f1:
        prices = json.load(f1)
        suits = []
        corp = []
        screen = []
        material = []
        col = []
        type_z = []
        mag_safe = []
        weight = []
        for i in prices:
            if 'Подходит для' not in prices[i]:
                suits[i] = {'Подходит для': 'Не указано'}
                prices[i].update(suits[i])
            if 'Тип корпуса' not in prices[i]:
                corp[i] = {'Тип корпуса': 'Не указано'}
                prices[i].update(corp[i])
            if 'Для моделей с диагональю экрана' not in prices[i]:
                screen[i] = {'Для моделей с диагональю экрана': 'Не указано'}
                prices[i].update(screen[i])
            if 'Материал чехла' not in prices[i]:
                material[i] = {'Материал чехла': 'Не указано'}
                prices[i].update(material[i])





    with open('accessories_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)


def get_images_laptops():
    with open('laptops_data/laptops_list.json') as f1:
        prices = json.load(f1)
        phone_images = {}
        for i in prices['products']:
            phone_images[i['productId']] = {
                'image': 'http://static.mvideo.ru/' + i['images'][0],
                'image1': 'http://static.mvideo.ru/' + i['images'][1],
                'image2': 'http://static.mvideo.ru/' + i['images'][2],
                'image3': 'http://static.mvideo.ru/' + i['images'][3]

            }
    with open('laptop_prices.json') as f2:
        prices = json.load(f2)
        for i in prices:
            prices[i].update(phone_images[i])

    with open('laptop_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)

    for i in prices:
        img = prices[i]['image']
        img1 = prices[i]['image1']

        resource = urllib.request.urlopen(img)
        out = open(f"pract/renessans_tech/static/pictures/laptops/{i}.jpg", 'wb')
        out.write(resource.read())
        out.close()

        resource = urllib.request.urlopen(img1)
        out = open(f"pract/renessans_tech/static/pictures/laptops/img1/{i}.jpg", 'wb')
        out.write(resource.read())
        JPGimg = Image.open(f"pract/renessans_tech/static/pictures/laptops/img1/{i}.jpg")
        JPGimg.save(f"pract/renessans_tech/static/pictures/laptops/img1/{i}"+ '.AVIF', 'AVIF')
        os.remove(f"pract/renessans_tech/static/pictures/laptops/img1/{i}.jpg")
        out.close()

        img2 = prices[i]['image2']
        img3 = prices[i]['image3']
        resource = urllib.request.urlopen(img2)
        out = open(f"pract/renessans_tech/static/pictures/laptops/img2/{i}.jpg", 'wb')
        out.write(resource.read())
        JPGimg = Image.open(f"pract/renessans_tech/static/pictures/laptops/img2/{i}.jpg")
        JPGimg.save(f"pract/renessans_tech/static/pictures/laptops/img2/{i}" + '.AVIF', 'AVIF')
        os.remove(f"pract/renessans_tech/static/pictures/laptops/img2/{i}.jpg")
        out.close()

        resource = urllib.request.urlopen(img3)
        out = open(f"pract/renessans_tech/static/pictures/laptops/img3/{i}.jpg", 'wb')
        out.write(resource.read())
        JPGimg = Image.open(f"pract/renessans_tech/static/pictures/laptops/img3/{i}.jpg")
        JPGimg.save(f"pract/renessans_tech/static/pictures/laptops/img3/{i}" + '.AVIF', 'AVIF')
        os.remove(f"pract/renessans_tech/static/pictures/laptops/img3/{i}.jpg")
        out.close()

def get_cashback_tvs():
    with open('tv_prices.json') as f1:
        prices = json.load(f1)
        item_cashback = {}
        for i in prices:
            item_cashback[i] = {'item_cashback': '5%'}
            prices[i].update(item_cashback[i])

    with open('tv_prices.json', 'w') as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)



def main():
    '''
    with open('computers_prices.json') as file:
        mas = []
        prices = json.load(file)
        for i in prices:
            for j in list(prices[i].keys()):
                if j not in mas:
                    mas.append(j)
        print(mas)
    '''
    #full_data_computers()
    get_images_computers()

    '''
    with open('tv_prices.json') as file:
        prices = json.load(file)
        new_screens = {}
        for i in prices:
            if '"' in prices[i]['Экран']:
                new_screens[i] = {
                    'Экран': prices[i]['Экран'].replace('"', '')
                }
                prices[i].update(new_screens[i])
        with open('tv_prices.json', 'w') as file:
            json.dump(prices, file, indent=4, ensure_ascii=False)
            
     '''





if __name__ == '__main__':
    main()
