from hashlib import sha1

from .models import User


class OpencartBackend:
    # Django 로그인 프로시저가 호출하는 인증 메소드
    def authenticate(self, username=None, password=None):

        try:
            # 커스텀 User 모델에서 이메일 주소를 username으로 사용한 경우
            user = User.objects.get(email=username)

            # Salted password SHA1 hashing 3 iterations
            # Opencart PHP 프로그램의 비밀번호 암호화 알고리즘
            hashed = sha1(
                (user.salt + sha1(
                    (user.salt + sha1(
                        password.encode('utf8')
                    ).hexdigest()).encode('utf8')
                ).hexdigest()).encode('utf8')
            ).hexdigest()

            if user.password == hashed:
                return user
            else:
                return None

        except User.DoesNotExist:
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None