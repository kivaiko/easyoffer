import json
import warnings

from django import VERSION
from django.forms.utils import flatatt
from django.templatetags.static import static
from django.utils.html import format_html, html_safe, mark_safe


__all__ = ("JS", "static")


_sentinel = object()


class JS:
    """
    Use this to insert a script tag via ``forms.Media`` containing additional
    attributes (such as ``id`` and ``data-*`` for CSP-compatible data
    injection.)::

        forms.Media(js=[
            JS('asset.js', {
                'id': 'asset-script',
                'data-answer': '"42"',
            }),
        ])

    The rendered media tag (via ``{{ media.js }}`` or ``{{ media }}`` will
    now contain a script tag as follows, without line breaks::

        <script type="text/javascript" src="/static/asset.js"
            data-answer="&quot;42&quot;" id="asset-script"></script>

    The attributes are automatically escaped. The data attributes may now be
    accessed inside ``asset.js``::

        var answer = document.querySelector('#asset-script').dataset.answer;
    """

    def __init__(self, js, attrs=None, static=_sentinel):
        self.js = js
        self.attrs = attrs or {}
        if static is not _sentinel:
            warnings.warn(
                "JS automatically determines whether it received an absolute"
                " path or not. Stop passing the 'static' argument please.",
                DeprecationWarning,
                stacklevel=2,
            )

    def startswith(self, _):
        # Masquerade as absolute path so that we are returned as-is.
        return True

    def __repr__(self):
        return f"JS({self.js}, {json.dumps(self.attrs, sort_keys=True)})"

    if VERSION >= (4, 1):

        def __str__(self):
            return format_html(
                '<script src="{}"{}></script>',
                self.js
                if self.js.startswith(("http://", "https://", "/"))
                else static(self.js),
                mark_safe(flatatt(self.attrs)),
            )

    else:

        def __html__(self):
            js = (
                self.js
                if self.js.startswith(("http://", "https://", "/"))
                else static(self.js)
            )
            return (
                format_html('{}"{}', js, mark_safe(flatatt(self.attrs)))[:-1]
                if self.attrs
                else js
            )

    def __eq__(self, other):
        if isinstance(other, JS):
            return self.js == other.js and self.attrs == other.attrs
        return self.js == other and not self.attrs

    def __hash__(self):
        return hash((self.js, json.dumps(self.attrs, sort_keys=True)))


if VERSION >= (4, 1):
    JS = html_safe(JS)
