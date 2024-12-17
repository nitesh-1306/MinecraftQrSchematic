from tdotly import tly
from dotenv import dotenv_values

class LinkShortner:
    def __init__(self):
        token = dotenv_values('.env')['TLY_TOKEN']
        self.shortner = tly.tly_shorturl()
        self.shortner.initialize(token)

    def short_url(self, url):
        return self.shortner.create_short_url(url)

if __name__ == '__main__':
    a = LinkShortner()
    print(a.short_url('https://www.google.com'))