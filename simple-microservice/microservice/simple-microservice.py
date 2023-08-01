import fastapi
import httpx
from scrapy.selector import Selector


api = fastapi.FastAPI()


@api.get('/api/weather/{city}')
def get_weather(city: str) -> dict:
    with httpx.Client() as client:
        response = client.get(url=f'https://pogoda.mail.ru/prognoz/{city}/')
        response.raise_for_status()

    selector = Selector(text=response.text)
    t = selector.xpath(
        '//div[@class="information__content__temperature"]/text()').getall()[1].strip()

    result = {'city': city,
              'temp': t,
              'src': 'vk'}

    # print(result)

    return result
