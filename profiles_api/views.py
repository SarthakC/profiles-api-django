from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api.serializers import HelloSerializer, UserProfileSerializer, ProfileFeedItemSerializer
from profiles_api.models import UserProfile, ProfileFeedItem
from profiles_api.permissions import UpdateOwnProfile, UpdateOwnStatus


class HelloApiView(APIView):
    """Test API View."""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""
        an_apiview = ["testing1", "testing2", "testing3"]

        return Response({"message": "Hello", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({"message": message})

        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Patch an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})


class HelloViewSet(ViewSet):
    """Test API ViewSet"""

    serializer_class = HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            "viewset-test1",
            "viewset-test2",
            "viewset-test3",
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}!'
            return Response({"message": message})

        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST
            )

    def retreive(self, request, pk=None):
        """Handle getting and object by id"""

        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Patch an object"""

        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Delete an object"""

        return Response({"http_method": "DELETE"})


class UserProfileViewSet(ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(ModelViewSet):
    """Handles creating, reading, and updating profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (UpdateOwnStatus,IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
