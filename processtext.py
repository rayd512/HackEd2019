def processtext(text):
    if 'http' in text:
        idx = text.find('http')
        text = text.replace(text[idx:],'')    
    
    if ':' in text:
        idx = text.find(':')
        text = text.replace(text[:idx+1],'')

    if ',' in text:
        text = text.split(',')[0]

    if '.' in text:
        text = text.split('.')[0]

    return(text)
