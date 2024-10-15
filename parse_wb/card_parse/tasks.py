from celery import shared_task

from .services.wb_card_parser import WBCardParser


@shared_task
def parse_article(
    article: str,
) -> None:
    parser = WBCardParser()
    parser.save_to_db(article)
