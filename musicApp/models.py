from django.db.models import Model, AutoField, CharField, DateField, PositiveIntegerField


class Albums(Model):
    id = AutoField(primary_key=True)
    artist = CharField(max_length=500)
    album = CharField(max_length=500)
    album_creation_year = PositiveIntegerField()
    label = CharField(max_length=500)
    tags = CharField(max_length=500)
    published_date = DateField()
    comment_number = PositiveIntegerField()
    album_url = CharField(max_length=500)
    image_urls = CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'albums'

