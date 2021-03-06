from typing import Type
from typing import TypeVar
from typing import Union

from django.views.generic import FormView
from django.views.generic import View

from _dependencies.injector import Injector

_T = TypeVar("_T", View, FormView)

def view(injector: Injector) -> Injector: ...
def form_view(injector: Injector) -> Injector: ...
def create_handler(from_view: Type[_T], injector: Injector) -> Type[_T]: ...
def apply_http_methods(handler: Type[_T], injector: Injector) -> None: ...
def apply_form_methods(handler: Type[_T], injector: Injector) -> None: ...
