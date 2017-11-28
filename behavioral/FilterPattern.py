class ContentFilter(object):
    # not sure the count of filters so use *
    def __init__(self, *filters):
        self.filters = list()
        if filters is not None:
            self.filters += filters

    def filter(self, content):
        print "base filtering "
        for f in self.filters:
            f.filter(content)


class PronContentFilter(ContentFilter):
    def filter(self, contents):
        print "pron content filtering "
        for content in contents:
            if str(content).__contains__("pron"):
                contents.remove(content)


class AdFilter(ContentFilter):
    def filter(self, contents):
        print "ad  filtering "
        for content in contents:
            if str(content).__contains__("ad"):
                contents.remove(content)


adFilter = AdFilter()
pronFilter = PronContentFilter()
contentFilter = ContentFilter(adFilter, pronFilter)

contentList = ['youtube_video', 'pron_video', 'ad_video']
contentFilter.filter(contentList)
print contentList
