from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    "/health",
    name="health:check",
    status_code=status.HTTP_200_OK,
)
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
