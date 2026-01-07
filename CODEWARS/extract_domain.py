# Write a function that when given a URL as a string, parses out just the 
# domain name and returns it as a string. For example:
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

import re

def domain_name(url):
    # return re.sub('www\.','',re.sub('https?://','',url)).split('.')[0]
    return re.sub('(https?://)|(www\.)', '', url).split('.')[0]

def other_sol(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]

def name_after_(url):
    n = url.split('#')
    return n[0]

print(domain_name(input('Enter URL: ')))
print(other_sol(input('Enter URL: ')))
print(name_after_(input('Enter URL: ')))