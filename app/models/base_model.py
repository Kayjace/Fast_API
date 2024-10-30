from tortoise import fields


class BaseModel:
    """
    앞으로 다른 모델들이 이 Basemodel을 상속받음

    상속 -> 멤버 변수와, 메소드를 물려준다.
    BaseModel은 메소드는 없고 멤버변수 3개만 존재.
    id, create_at, modified_at 총 3개.

    created_at과 modified_at은 aduit 컬럼
    audit은 "누가, 언제, 무엇을, 어떻게 수정했는가"를 기록으로 남기는 것.
    -> 회사가 커지고 오래되다보면 "나쁜 마음"을 품는 직원이 생길 수도 있음
    -> audit 기록을 남겨야만 누가 뭘 바꿨는 지를 알 수 있고, 증거가 남아야 고소도 하고 후속 대응도 가능.

    primary key
    예전에는 primary key의 타입을 bigint
        21억 건 이상의 데이터를 생성할 가능성이 잇다. -> int는 21억이 max라서 모자란다.

    big int vs length 40의 str
    -> str이 더 큼.
    -> 컬럼의 크기가 더 크다는 뜻 -> 성능은 반대로 줄어듬.

    그럼에도 문자열을 사용하는 이유?
    - 실전에서는 pk int 혹은 bigint를 쓰는 게 맞다.
    """

    # 제일 좋은 방법
    # id = fields.
    # external_id = fields.CharField(max_length=40) #외부 통신
    id = fields.CharField(pk=True, max_length=40)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
