from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.authentication import TokenAuthentication

from profiles_api.serializers import HelloSerializer, UserProfileSerializer
from profiles_api.models import UserProfile
from profiles_api.permissions import UpdateOwnProfile


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
