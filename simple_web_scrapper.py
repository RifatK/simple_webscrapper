
import sys
import urllib2
import re


def get_html_content(url):
    response = urllib2.urlopen(url)
    html_content = response.read()
    return html_content


def get_all_tags_from_html(html_content):
    tag_list = []
    regex_for_all_tags = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"
    for match in re.finditer(regex_for_all_tags, html_content):
        if not "</" in repr(match.group()):
            tagPrefix = repr(match.group()).split(" ")[0][1:]
            tag_list.append(clean_up_tags(tagPrefix))
    return tag_list

def clean_up_tags(tag):
    temp_tag = tag.replace("<","")
    try:
       idx = temp_tag.index(">")
       return temp_tag[0:idx]
    except:
       return temp_tag


def get_count_of_each_tag(tag_list):
    from collections import Counter
    return Counter(tag_list)

def print_summary(tag_summary,n):
    print("The tags used are : ")
    print(tag_summary.keys())
    print("The top %s used are : " % n)
    print tag_summary.most_common(n)

def print_top_n_results(counter_obj,n):
    print counter_obj.most_common(n)


def run_simple_web_scrapper(url):
    html_content = get_html_content(url)
    complete_tag_list = get_all_tags_from_html(html_content )
    tag_summary = get_count_of_each_tag(complete_tag_list )

    print_summary(tag_summary ,5)

def main():
    url = 'http://python.org/'
    run_simple_web_scrapper(url)

if __name__ == "__main__":
    sys.exit(main())


