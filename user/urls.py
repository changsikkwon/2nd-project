from django.urls    import path

from .views         import SignupView, SigninView, KakaoSigninView, KakaoSignInCallbackView

urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/signin', SigninView.as_view()),   
    path('/signin/kakao', KakaoSigninView.as_view()),
    path('/signin/kakao/callback', KakaoSignInCallbackView.as_view()),
]