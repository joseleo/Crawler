# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting

from scrapy.exceptions import DropItem


class OslcrawlerPipeline(object):
    def __init__(self):
        self.file_notags = open('items_notags.txt', 'a')
        self.file_tags = open('items_tags.html', 'a')

    def open_spider(self, spider):
        document_open = '<html><head><title>OSLcrawler</title></head><body>'
        self.file_tags.write(document_open)

    def close_spider(self, spider):
        document_close = '</body></html>'
        self.file_tags.write(document_close)

    def process_item(self, item, spider):
        if len(item['labels']) > 0:
            document_table = '<table style="border:1px solid black"><tr><td>'
            document_table += 'Titulo: '
            document_table += item['title'][0]
            document_table += '</td></tr>'
            document_table += '<tr><td>Autor: '
            document_table += item['author'][0]
            document_table += '</td></tr>'
            document_table += '<tr><td>Categorias: '
            document_table += item['categories'][0]
            document_table += '</td></tr>'
            document_table += '<tr><td>Etiquetas: '
            document_table += item['labels'][0]
            document_table += '</td></tr>'
            document_table += '<tr><td>Fecha: '
            document_table += item['date'][0]
            document_table += '</td></tr>'
            document_table += '</table>'

            self.file_tags.write(document_table)
            return item
        else:
            linea = 'Titulo:' + item['title'][0] + '\n'
            linea += 'Autor:' + item['author'][0] + '\n\n'
            self.file_notags.write(linea)

            raise DropItem("ERROR: ESTE POST NO TIENE ETIQUETAS")
