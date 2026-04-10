from .template_registry import T


def global_templates(request):
    if request.htmx:
        base_template = T["LAYOUT"]["HTMX_BASE"]
    else:
        base_template = T["LAYOUT"]["BASE"]
    return {"T": T, "base_template": base_template}
