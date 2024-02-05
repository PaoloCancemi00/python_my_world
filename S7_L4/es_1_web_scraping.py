# Esercizio 1 

'''
Estrazione di Testo Semplice con Scrapy Usare Scrapy per estrarre i titoli di tutte le notizie 
da una pagina di esempio di un blog o di un sito di notizie. 
1. Installazione di Scrapy: Assicurati di avere Scrapy installato nel tuo ambiente di sviluppo. 
2. Crea uno spider chiamato `NewsTitleSpider`. 
3. Definizione degli URL di Partenza: Usa un sito di esempio (come `http://example.com/news`) 
come `start_urls`.
4. Nello spider, implementa il metodo `parse` per estrarre tutti i titoli (elementi `<h1>`). 
5. Salva i titoli estratti in un file JSON o CSV. 6. 
Esegui lo spider e verifica i risultati.
'''

import scrapy

class NewsTitleSpider(scrapy.Spider):
    name = 'NewsTitleSpider'
    start_urls = ['http://example.com/news']  # Sostituisci con l'URL del sito di esempio

    def parse(self, response):
        # Utilizza le regole di estrazione XPath o CSS per estrarre tutti i titoli <h1>
        h1_titles = response.xpath('//h1/text()').extract()
        
        # Stampa i titoli delle notizie estratti
        for title in h1_titles:
            print(title)

        # Puoi anche salvarli in un file JSON come hai fatto prima se lo desideri





















