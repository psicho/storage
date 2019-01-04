from rest_framework import generics, permissions,viewsets,filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework.response import Response
import django_filters

from .serializers import *
from .models import *

# from crm import repository
# from crm.repository import Repository
# from disclosure.models import HomeServiceType
# from utils.django_permissions import IsSuperUser, QQubePermissions
# from utils.pagination import StandardResultsSetPagination
# import counters.repository