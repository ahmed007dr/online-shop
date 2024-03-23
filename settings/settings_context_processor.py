from django.core.cache import cache
from .models import Settings




def get_settings(request):
    settings_data = cache.get('settings_data')
    settings_data = Settings.objects.last()
    return {'settings_data': settings_data}


# def get_settings(request):
#     try:
#         settings_data = cache.get('settings_data')

#     except Exception:
#         settings_data = Settings.objects.last()
#         #cache.set('settings_data', settings_data, 60 * 60 * 24)

#     return {'settings_data': settings_data}

'''
- retrieve the settings data from the cache using the key 'settings_data'
- If there's an exception raised during this process, it will be caught by the except block.
- If the settings data is not found in the cache or if an exception occurs while trying to retrieve it
-this code retrieves the latest Settings object from the database using Settings.objects.last().
 It then sets this data into the cache with a timeout of 24 hours (60 seconds * 60 minutes * 24 hours).
'''

#make cach to data will change  every time you save your Setting model instance