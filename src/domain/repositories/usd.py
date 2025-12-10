from typing import Coroutine, Any
import abc


class USDRepository(abc.ABC): 
    @abc.abstractmethod
    async def get_now_data() -> Coroutine[Any, Any, float]: ...