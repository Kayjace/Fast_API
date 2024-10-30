from app.configs.base_settings import Settings


def get_settings() -> Settings:
    """
    1. pydantic은 기본적으로 "환경 변수"에서 설정값을 읽는다.
    2. env_file을 전달한다면 .env를 읽는다.

    env_file과 환경변수 중에서는 항상 환경변수가 우선된다.
        -> 환경변수에 MY_NAME=철수라고 되어 있고, env_file에 MY_NAME=영희라고 되어있다면
            -> 환경변수가 우선하므로 MY_NAME은 철수가 된다.

    내가 했던 실수:
    mypy가 다음 에러를 잡았습니다.

    app/configs/__init__.py:14: error: Unexpected keyword argument "env_file" for "Settings"; did you mean "_env_file"?  [call-arg]
    Found 1 error in 1 file (checked 11 source files)

    번역 -> env_file은 unexpected 입니다. -> unexpected 예기치 않은
    keyword argument란
    """
    return Settings(_env_file=".env", _env_file_encoding="utf-8")


settings = get_settings()
