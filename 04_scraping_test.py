#!/bin/python
# encoding: utf-8

import urllib.request
import codecs

class Twitter:
    def get_followers(self, account):

        response = urllib.request.urlopen("https://twitter.com/%s" % account)
        page_source = str(response.read())

        page_source_upper = page_source.upper() #find bug when html content use different case link

        index_last      =   page_source_upper.find('HREF="/%s/FOLLOWERS"' % account.upper())
        index_first     =   page_source_upper[:index_last].rfind("TITLE")

        follower_tag = page_source_upper[index_first : index_last]
        #print(follower_tag)

        follower_title_tag = follower_tag.split()
        follower_amount = follower_title_tag[0].split("=")[1].replace('"','')

        return "Twitter name: %s has %s followers" % (account, follower_amount,)

if __name__ == '__main__':

    Twitter_obj = Twitter()
    print(Twitter_obj.get_followers("KMbappe")) #exp result: 4,010,813 at 28Mar2020 18:00
    print(Twitter_obj.get_followers("zidane_zinedine")) #exp result: 58,014 at 28Mar2020 18:00 (Is it fake?)