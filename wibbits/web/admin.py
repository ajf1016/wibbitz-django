from django.contrib import admin
from web.models import Subscribe,Customer,Feature,VideoBlog,Testimonial,MarketingFeature,Product,Blog,Contact

admin.site.register(Subscribe)
admin.site.register(Customer)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id","image","icon","icon_background","title","description","testimonial_description","testimonial_author","author_designation","testimonial_logo"]
    
admin.site.register(Feature,FeatureAdmin)

admin.site.register(Testimonial)
admin.site.register(MarketingFeature)
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(VideoBlog)
admin.site.register(Contact)