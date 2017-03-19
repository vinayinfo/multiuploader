from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.core.signing import Signer
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from multiuploader.forms import MultiUploadForm

register = template.Library()


@register.simple_tag(takes_context=True)
def media_type(context, media_type):
    mu_forms = getattr(settings, "MULTIUPLOADER_FORMS_SETTINGS", settings.MULTIUPLOADER_FORMS_SETTINGS)

    signer = Signer()

    if media_type:
        import warnings

        if media_type == '' or media_type not in mu_forms:
            if settings.DEBUG:
                warnings.warn("A {% media_type %} was used in a template but such media_type ({}) was not provided"
                              "in settings, default used instead".format(media_type))

            return mark_safe(
                u"<div style='display:none'><input type='hidden' name='media_type' value='{}' /></div>".format(signer.sign(
                    'default')))

        else:
            return mark_safe(
                u"<div style='display:none'><input type='hidden' name='media_type' value='{}' /></div>".format(signer.sign(
                    media_type)))
    else:
        # It's very probable that the media_type is missing because of
        # misconfiguration, so we raise a warning
        import warnings
        if settings.DEBUG:
            warnings.warn("A {% media_type %} was used in a template but form_type was not provided")

        return mark_safe(u"")


@register.simple_tag(takes_context=True)
def multiuploader_form(context, form_type="default", template="multiuploader/form.html", target_form_fieldname=None,
                       js_prefix="jQuery", send_button_selector=None,
                       wrapper_element_id="", lock_while_uploading=True, number_files_attached=0):
    return render_to_string(template, {
        'multiuploader_form': MultiUploadForm(form_type=form_type),
        'csrf_token': context["csrf_token"],
        'type': form_type,
        'prefix': js_prefix,
        'send_button_selector': send_button_selector,
        'wrapper_element_id': wrapper_element_id,
        'target_form_fieldname': target_form_fieldname,
        'lock_while_uploading': lock_while_uploading,
        'number_files_attached': number_files_attached
    })


@register.inclusion_tag('multiuploader/noscript.html')
def multiuploader_noscript(uploaded_field=None):
    return {
        'uploaded_widget_html_name': uploaded_field
    }
