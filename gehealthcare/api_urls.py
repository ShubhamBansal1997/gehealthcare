# Third Party Stuff
from rest_framework.routers import DefaultRouter

# gehealthcare Stuff
from gehealthcare.base.api.routers import SingletonRouter
from gehealthcare.users.api import CurrentUserViewSet
from gehealthcare.users.auth.api import AuthViewSet
from gehealthcare.diagnoses.api.viewsets import (IcCodeViewSet, DiagnosesViewSet)
from gehealthcare.labevents.api.viewsets import (ItemViewSet, LabeventViewSet)
from gehealthcare.prescriptions.api.viewsets import PrescriptionViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register('auth', AuthViewSet, base_name='auth')
singleton_router.register('me', CurrentUserViewSet, base_name='me')
default_router.register('iccode', IcCodeViewSet, base_name='iccode')
default_router.register('diagnose', DiagnosesViewSet, base_name='diagnose')
default_router.register('item', ItemViewSet, base_name='item')
default_router.register('labevent', LabeventViewSet, base_name='labevent')
default_router.register('prescription', PrescriptionViewSet, base_name='prescription')


# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls
