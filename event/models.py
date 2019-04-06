from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'event_{0}/{1}'.format(instance.event.id, filename)

class EventDetail(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=500, blank=True, null=True)
    fee = models.CharField(max_length=150, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    organized_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def shortDetails(self):
        return self.description[:50]

    def pub_date_pretty(self):
        return self.created_at.strftime('%B %e %Y')


class EventReg(models.Model):
    # CHOICES = (
    # ('One', 'One'),
    # ('Two', 'Two'),
    # ('Three', 'Three'),
    # ('Four', 'Four'),
    # )
    title = models.ForeignKey(EventDetail, on_delete=models.CASCADE)
    fullname= models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    squadname = models.CharField(max_length=255, blank=True, null=True)
    membernumber = models.CharField(max_length =10,  blank=True)
    
    p1name = models.CharField(max_length=255, blank=True, null=True)
    p1userid = models.CharField(blank=True, max_length=50, null=True)

    p2name = models.CharField(max_length=255, blank=True, null=True)
    p2userid = models.CharField(blank=True, max_length=50, null=True)

    p3name = models.CharField(max_length=255, blank=True, null=True)
    p3userid = models.CharField(max_length=50, blank=True, null=True)
    
    p4name = models.CharField(max_length=255, blank=True, null=True)
    p4userid = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{} ,  {} , {}'.format (self.title, self.fullname,  self.squadname)
