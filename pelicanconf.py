AUTHOR = "Joel Berman"
SITENAME = "joelberman.net"
# SITEURL = "http://joelberman.net"

PATH = "content"

ARTICLE_PATHS = ["articles"]

PAGE_PATHS = ["pages"]

THEME = "./themes/notmyidea_photos"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

# Base settings where to find the galleries with images
PHOTO_LIBRARY = "content/galleries"

PHOTO_INLINE_GALLERY_ENABLED = True
# We use the default settings here
# PHOTO_INLINE_GALLERY_TEMPLATE = "inline_gallery"

# Use the name of the site as watermark text
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = "©2022 Joel Berman"
PHOTO_EXIF_COPYRIGHT = "CC-BY-SA"
#PHOTO_ARTICLE = (760, 506, 80)
PHOTO_ARTICLE = (380, 253, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_EXIF_COPYRIGHT_AUTHOR = 'Joel Berman'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
