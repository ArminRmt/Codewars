# first soloution

def domain_name(url):
    url = url.replace("https://", '')
    url = url.replace("http://", '')
    url = url.replace("www.", '')
    return url.split('.')[0]


# second soloution

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


# third soloution

def domain_name(url):
    if url[0:5] == 'https':
        index = find_dot_index(url)
        return url[8:index]
    elif url[0:4] == 'http' and url[7] == 'w':
        url = url[11:]
        index = find_dot_index(url)
        return url[0:index]
    elif url[0:4] == 'http':
        index = find_dot_index(url)
        return url[7:index]
    else:
        url = url[4:]
        index = find_dot_index(url)
        return url[0:index]


def find_dot_index(url):
    list1 = list(url)
    return [i for i, x in enumerate(list1) if x == '.'][0]
