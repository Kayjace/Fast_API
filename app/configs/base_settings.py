from enum import StrEnum

from pydantic_settings import BaseSettings


class Env(StrEnum):
    """
    enum을 만드는 이유: 자동완성과 타입체킹
    -> LOCAl로 실수 했을 때 IDE가 이를 잡아줄 수 있다.

    Mypy 에러 예제:
    app/configs/base_settings.py:16: error: "type[Env]" has no attribute "LOCAᅵ"  [attr-defined]
    Found 1 error in 1 file (checked 6 source files)

    type Env 에는 LOCAl 라는 속성이 없다.
    .(접근 연산자) 연산자로 접근 해 보았을 때,  Env 안에는 "LOCAl"이 없었다.
    """

    LOCAL = "local"  # 내가 개발하는 컴퓨터
    STAGE = "stage"  # QA와 함께 정상 동작을 확인하는 곳
    PROD = "prod"  # 실제 배포되는 곳, "진짜" 서버


class Settings(BaseSettings):
    ENV: Env = Env.LOCAL
    DB_HOST: str = "127.0.0.1"  # = localhost
    DB_PORT: int = 3306
    DB_USER: str = "root"  # mysql의 기본 계정
    DB_PASSWORD: str = "1234"
    DB_DB: str = "oz_fastapi"
