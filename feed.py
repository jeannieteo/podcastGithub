import yaml
import xml.etree.ElementTree as xmlTree

with open('feed.yaml', 'r') as file:
    yamlData = yaml.safe_load(file)
    rssElement = xmlTree.Element('rss', {'version':'2.0', 
    'xmlns:itunes':'http://www.itunes.com/podcast1.0.dtd',
    'xmlns:itunes':'http://www.itunes.com/podcast1.0.dtd',
    'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})

    
channelElement = xmlTree.SubElement(rssElement, 'channel')
xmlTree.SubElement(channelElement, 'title').text = yamlData['title']
xmlTree.SubElement(channelElement, 'format').text = yamlData['format']
xmlTree.SubElement(channelElement, 'subtitle').text = yamlData['subtitle']
xmlTree.SubElement(channelElement, 'itunes:author').text = yamlData['author']
xmlTree.SubElement(channelElement, 'description').text = yamlData['description']
#xmlTree.SubElement(channelElement, 'itunes:author',{'href':link_prefix + yamlData['image']}).text
xmlTree.SubElement(channelElement, 'language').text = yamlData['language']

for item in yamlData['item']:
    itemData = xmlTree.SubElement(channelElement, 'item')
    xmlTree.SubElement(itemData, 'item').text = item['title']
    xmlTree.SubElement(itemData, 'description').text = item['description']
    xmlTree.SubElement(itemData, 'itunes:duration').text = item['duration']
    xmlTree.SubElement(itemData, 'itunes:author').text = yamlData['author']
    xmlTree.SubElement(itemData, 'pubDate').text = item['published']
    enclosure = xmlTree.SubElement(itemData, 'enclosure',{
        #'url':link_prefix + item['file'],
        'type':'mp3',
        'length': item['length']})
outputTree = xmlTree.ElementTree(rssElement)
outputTree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)