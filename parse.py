import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def get_data():
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

    with open('products_id_phones.json', 'w') as file:
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

    with open('phones_list.json', 'w') as file:
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



def main():
    get_data()

if __name__ == '__main__':
    main()
