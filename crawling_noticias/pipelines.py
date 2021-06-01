# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from noticias.models import Noticia
from datetime import datetime
from django.utils.text import slugify


def transforma_string_data(param):
    param = datetime.strptime(param, '%d/%m/%Y').date()
    return param


class CrawlingNoticiasPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['conteudo']:
            if 'FGTS' not in adapter['conteudo'] or 'Caixa' not in adapter['conteudo']:
                raise DropItem(
                    f"A matéria {item['titulo']} não aborda o tema FGTS")
            else:
                try:
                    data = transforma_string_data(item['data_noticia'])
                    Noticia.objects.create(
                        titulo=item['titulo'],
                        data_noticia=data,
                        fonte=item['fonte'],
                        conteudo=item['conteudo'],
                        url=item['url'],
                        slug=slugify(item['titulo'])
                    )
                except:
                    print('Esta matéria já consta no banco de dados')
