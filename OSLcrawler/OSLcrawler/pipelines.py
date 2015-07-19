# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class OslcrawlerPipeline(object):
    #def open_spider(self, spider):
	#self.file = open('index.html', 'a')
        #document_open = '<html><head><title>OSLcrawler</title></head><body>'
	#self.file.write(document_open)		 	

    def close_spider(self, spider):
	document_close = '</body></html>' 	
	self.file.write(document_close)		 	
	
    def process_item(self, item, spider):
        if len(item['labels']) > 0:        
	    self.file = open('index.html', 'a')
	    document_table = '<table style="border:1px"><tr><td>'
	    document_table += item['title'][0]
	    document_table += '</td></tr>'
	    document_table += '<tr><td>'
	    document_table += item['author'][0]
	    document_table += '</td></tr>'
            document_table += '<tr><td>'
            document_table += item['content'][0]
	    document_table += '</td></tr>'

	    self.file.write(document_table)			
	    return item
        else:
            self.file = open('items_notags.txt', 'a')
            
            linea = 'Titulo:' + item['title'][0] + '\n'
            linea += 'Autor:' + item['author'][0] + '\n\n'
            self.file.write(linea)
            
	    raise DropItem("ERROR: ESTE POST NO TIENE ETIQUETAS")


