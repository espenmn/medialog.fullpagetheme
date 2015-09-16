from zope.interface import Interface


class IFullpageTheme(Interface):
    """Marker interface that defines a Zope 3 browser layer.
    This interface is referred in browserlayer.xml.
    All views and viewlets register against this layer will appear on
    your Plone site only when the add-on installer has been run,
    for example: full folder view (all content)
    """
