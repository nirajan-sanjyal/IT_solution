from django import template
from django.utils.html import strip_tags, escape
from django.utils.safestring import mark_safe
import html

register = template.Library()

@register.filter
def decode_html(value):
    """Decodes HTML entities and removes tags"""
    decoded = html.unescape(value)  # Decode HTML entities
    return mark_safe(decoded)

@register.filter
def richtext_truncatewords(value, num_words):
    """Truncate rich text content safely"""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html.unescape(value), "html.parser")  # Decode and parse HTML
    text = soup.get_text()  # Extract plain text
    truncated = " ".join(text.split()[:num_words]) + "..."  # Truncate words
    return mark_safe(truncated)
