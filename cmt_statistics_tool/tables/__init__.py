from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

from cmt_statistics_tool.tables.metareview import (  # noqa: E402
    RevisionMetareview,
    SubmissionMetareview,
)
from cmt_statistics_tool.tables.paper import Revision, Submission  # noqa: E402
from cmt_statistics_tool.tables.people import (  # noqa: E402
    People,
    RevisionPeople,
    SubmissionPeople,
)
from cmt_statistics_tool.tables.review import (  # noqa: E402
    RevisionReview,
    SubmissionReview,
)
from cmt_statistics_tool.tables.seniormetareview import (  # noqa: E402
    RevisionSeniormetareview,
    SubmissionSeniormetareview,
)

def get_new_engine() -> any:
    return create_async_engine(
        # Please change this connection string to your specification
        "postgresql+asyncpg://postgres:postgres@localhost/CMT_STATISTICS",
        echo=False,
    )

engine = get_new_engine()
async_session = sessionmaker(get_new_engine(), expire_on_commit=False, class_=AsyncSession, autoflush=False)

__all__ = (
    "Base",
    "RevisionMetareview",
    "SubmissionMetareview",
    "Revision",
    "Submission",
    "People",
    "SubmissionPeople",
    "RevisionPeople",
    "RevisionReview",
    "SubmissionReview",
    "RevisionSeniormetareview",
    "SubmissionSeniormetareview",
    "engine",
    "async_session",
)
