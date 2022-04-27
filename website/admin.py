from django.contrib import admin
from .models import formgroup
#from .models import Pigga
from .models import service
from .models import WorkingTime
from .models import Menu
from .models import Chefs
from .models import Testmonials

admin.site.register(formgroup)
#admin.site.register(Pigga)
admin.site.register(service)
admin.site.register(WorkingTime)
admin.site.register(Menu)
admin.site.register(Chefs)
admin.site.register(Testmonials)
# Register your models here.
