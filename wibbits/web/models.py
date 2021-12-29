from django.db import models


cndnt_type = (
    ("blog_post","Blog post"),
    ("webinar","Webinar"),
    ("report","Report"),
)

COMPANY_SIZE = (
    ("1","1-10"),
    ("2","11-50"),
    ("3","51-200"),
    ("4","201-500")    
)

INDUSTRY = (
    ("1","Agriculture"),
    ("2","Banking & Finance"),
    ("3","Business Sevice & Software"),   
)
JOB_ROLE = (
    ("1","C-Suite"),
    ("2","VP")
)
COUNTRY = (
    ("1","United States"),
    ("2","Albania")    
)


class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    
class Customer(models.Model):
    product = models.ForeignKey("web.Product",on_delete=models.CASCADE)
    image = models.FileField(upload_to="customer/")
    whiteImage = models.FileField(upload_to="customer/")
    

class Feature(models.Model):
    image = models.ImageField(upload_to='feature/')
    icon = models.FileField(upload_to="feature/")
    icon_background  = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.TextField()  
    testimonial_description =  models.TextField()
    testimonial_author = models.CharField(max_length=128)
    author_designation = models.CharField(max_length=128)
    testimonial_logo = models.FileField(upload_to="feature/")
    
    def __str__(self):
        return self.title

class VideoBlog(models.Model):
    play_icon = models.FileField(upload_to="blog/")
    image = models.ImageField(upload_to="blog/")
    title = models.TextField()
    logo = models.FileField(upload_to="blog/")
    
    # def __str__(self):
        # self.title
        
class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/")
    logo = models.FileField(upload_to="testimonial/")
    description = models.TextField()    
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class MarketingFeature(models.Model):
    image = models.FileField(upload_to="marketing/")
    title = models.CharField(max_length=128)
    description = models.TextField()
    
    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to="product/")
    hero_image = models.ImageField(upload_to="product/")
    logo = models.FileField(upload_to="product/")
    title = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    background_color = models.CharField(max_length=128)
    description = models.TextField()
    class_name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.title

class Blog(models.Model):
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(max_length=128)
    content_type = models.CharField(max_length=128,choices=cndnt_type)
    link_text = models.CharField(max_length=128)
    
    class Meta:
        db_table = 'web_blog'
        ordering = ["-id"]
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    company_size = models.CharField(max_length=128,choices=COMPANY_SIZE)
    industry = models.CharField(max_length=128,choices=INDUSTRY)
    job_role = models.CharField(max_length=128,choices=JOB_ROLE)
    country = models.CharField(max_length=128,choices=COUNTRY)
    user_agreement = models.BooleanField(default=False)
    
class Meta:
    db_table = 'web_contact'
    ordering = ["-id"]

def __str__(self):
    return self.first_name
