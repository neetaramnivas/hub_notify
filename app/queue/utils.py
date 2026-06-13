import aio_pika
from app.config import settings
from app.queue.schemas import ALL_QUEUES

async def setup_queues():
    """Declares all required queues on startup."""
    connection = await aio_pika.connect_robust(settings.rabbitmq_url)
    async with connection:
        channel = await connection.channel()
        for queue_name in ALL_QUEUES:
            await channel.declare_queue(queue_name, durable=True)