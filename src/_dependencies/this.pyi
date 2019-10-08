from typing import Any, List, Tuple

from _dependencies.injector import Injector


class This:

    def __init__(self, expression: Any) -> None: ...

    def __getattr__(self, attrname: str) -> This: ...

    def __getitem__(self, item: Any) -> This: ...

    def __lshift__(self, num: int) -> This: ...


this: This


def make_this_spec(dependency: This) -> Tuple[str, ThisSpec, List[str], int]: ...


class ThisSpec:

    def __init__(self, dependency: This) -> None: ...

    def __call__(self, __self__: Injector) -> Any: ...

    @property
    def __expression__(self) -> Any: ...
