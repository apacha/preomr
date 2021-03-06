from google.appengine.ext import db

class Author(db.Model):
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    name = db.StringProperty()
    info = db.TextProperty()
    site = db.StringProperty()
    siteurl = db.LinkProperty()

class Work(db.Model):
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    name = db.StringProperty(required=True)
    link = db.LinkProperty(required=True)
    author = db.ReferenceProperty(Author)
    site = db.StringProperty()
    contentlink = db.LinkProperty()
    blobtype = db.StringProperty(choices = [
        "pdf", "tif","jpg","png" ])
    data = db.BlobProperty()

class Site(db.Model):
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    name = db.StringProperty()

class SavedList(db.Model):
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    name = db.StringProperty()
    size = db.IntegerProperty()
    keys = db.ListProperty(db.Key)
    ids = db.ListProperty(int)
    site = db.StringProperty()

