from typing import Any, List, NoReturn, Tuple


class Package:

    def __init__(self, name: str) -> None: ...

    def __getattr__(self, attrname: str) -> Package: ...


def make_package_spec(
    dependency: Package
) -> Tuple[str, ImportSpec, List[Any], int]: ...


class ImportSpec:

    def __init__(self, dependency: Package) -> None: ...

    def __call__(self) -> NoReturn: ...
