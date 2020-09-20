from . import register_plugin

@register_plugin
def hello():
    print("Hello from Plugin")
