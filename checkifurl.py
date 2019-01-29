def check_url(url):
    tld = ['com','org','net']
    a = []
    for i in tld:
        if i in url:
            a.append('is url')
        a.append('not url')
    if 'is url' in a:
        return 'is url'
    else:
        return 'not url'
