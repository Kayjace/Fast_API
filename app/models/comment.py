from __future__ import annotations

from tortoise import Model, fields

from app.models.article import Article
from app.models.base_model import BaseModel


class Comment(BaseModel, Model):  # pydantic의 basemodel을 import 하지 않도록 주의.
    article: fields.ForeignKeyRelation[Article] = fields.ForeignKeyField(
        "models.Article",
        related_name="comments",
        db_constraint=False,
    )
    # fields.ForeignKeyRelation[Article]는 타입
    # fields.ForeignKeyField(...)는 실제 값.

    author = fields.CharField(max_length=255)
    content = fields.TextField()

    class Meta:
        table = "comments"

    @classmethod
    async def get_all_by_article(cls, article_id: str) -> list[Comment]:
        """
        filter().all()... 이거 어디서 많이 봤는데?
        tortoise orm은 처음부터 설계 의도가 "Django ORM과 흡사하게" 이다.
        django에 있던 웬만한 것들은 tortoise orm에도 존재한다.
        django 공부를 했다면 tortoise는 거의 바로 사용 가능.
        """
        return await cls.filter(article=article_id).all()
