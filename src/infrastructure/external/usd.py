import xml.etree.ElementTree as ET

import httpx

from src.domain.repositories.usd import USDRepository
from src.infrastructure.config import env


class CentroBankUSDRepository(USDRepository): 
    async def get_now_data(self) -> float:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(env.external.url)
                response.raise_for_status()
            except httpx.HTTPError:
                return None

        root = ET.fromstring(response.content)

        for valute in root.findall('Valute'):
            if valute.get('ID') == 'R01235': # R01235 - код доллара
                value_text = valute.find('VunitRate').text.replace(',', '.')
                value = float(value_text)
       
                return value
        
        return 0
