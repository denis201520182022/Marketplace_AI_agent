from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
import uuid
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """
    Generic asynchronous CRUD repository implementing Clean Architecture principles.
    """

    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def get_by_id(self, id: Union[uuid.UUID, str, int]) -> Optional[ModelType]:
        """Fetch single record by its primary key ID."""
        if isinstance(id, str):
            try:
                id = uuid.UUID(id)
            except ValueError:
                pass
        return await self.session.get(self.model, id)

    async def list_all(
        self,
        skip: int = 0,
        limit: int = 100,
    ) -> List[ModelType]:
        """Fetch multiple records with pagination."""
        stmt = select(self.model).offset(skip).limit(limit)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def create(self, **kwargs: Any) -> ModelType:
        """Create and persist a new record."""
        instance = self.model(**kwargs)
        self.session.add(instance)
        await self.session.flush()
        await self.session.refresh(instance)
        return instance

    async def update(
        self,
        db_obj: ModelType,
        update_data: Dict[str, Any],
    ) -> ModelType:
        """Update existing record attributes."""
        for field, value in update_data.items():
            if hasattr(db_obj, field):
                setattr(db_obj, field, value)
        self.session.add(db_obj)
        await self.session.flush()
        await self.session.refresh(db_obj)
        return db_obj

    async def delete(self, id: Union[uuid.UUID, str, int]) -> bool:
        """Delete record by ID."""
        db_obj = await self.get_by_id(id)
        if db_obj:
            await self.session.delete(db_obj)
            await self.session.flush()
            return True
        return False
