import simple_web_scrapper as sw


def print_tags(src, dpth = 0, key = ''):

    for key in src:
        string_to_print = key
        subDict=src[key]
        subKey =subDict.keys()[0]
        while subKey != 'count':
            try:
               if subKey != 'count':
                  string_to_print+=subKey
               subDict=subDict[subKey]
               subKey =subDict.keys()[0]
               if subKey == 'count':
                  print("%s appeared % s time " % (string_to_print,str(subDict['count'])))
            except:
               break

def make_trie(*args):
    
    trie = {}
 
    for word in args:
        if type(word) != str:
            raise TypeError("Trie only works on str!")
        temp_trie = trie

        nested_keys = in_trie(temp_trie, word)
        if nested_keys is not None:
           current_val = get_nested_default(temp_trie, nested_keys )['count']
           set_nested(temp_trie, nested_keys,current_val+1)
        else:
            for letter in word:
                temp_trie = temp_trie.setdefault(letter, {})
            temp_trie = temp_trie.setdefault('count',1)
 
    return trie

def get_nested_default(d, path):
    return reduce(lambda d, k: d.setdefault(k, {}), path, d)
def set_nested(d, path, value):
    get_nested_default(d, path[:-1])[path[-1]]['count'] = value



def in_trie(trie, word):
    if type(word) != str:
        raise TypeError("Trie only works on str!")
    keys=[]
    temp_trie = trie
    for letter in word:
        if letter not in temp_trie:
            return None
        temp_trie = temp_trie[letter]
        keys.append(letter)
    return keys
 

 
if __name__ == '__main__':
    url = 'http://python.org/'
    html_content = sw.get_html_content(url)
    complete_tag_list = sw.get_all_tags_from_html(html_content )
    trie = make_trie(*complete_tag_list)
    print_tags(trie )
 
