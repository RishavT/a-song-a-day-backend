from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError

class Publish(APIView):
    """
    View to list all users in the system.

    * Requires auth authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = [IsAuthenticated]

    @classmethod
    def publish_to_facebook(cls, video_id, message, auth):
        """
        Publishes to facebook
        """
        return True

    @classmethod
    def publish_to_youtube(cls, video_id, auth):
        """
        Publishes to YouTube
        """
        return True

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        video_id = request.data.get('video_id')
        message = request.data.get('message')
        if not (video_id and message):
            raise ParseError(detail="Invalid parameters")

        app_user = request.user.app_user
        facebook_response = self.publish_to_facebook(
            video_id=video_id, message=message, auth=app_user.fb_auth)
        response = {}
        if facebook_response:
            response['facebook'] = facebook_response
            youtube_response = self.publish_to_youtube(
                video_id=video_id, auth=app_user.google_auth)
            if youtube_response:
                response['youtube'] = youtube_response
        return Response(response)
