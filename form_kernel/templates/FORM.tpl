{% extends 'script.tpl' %}

{% block input %}
{%- set cmd1 = cell.source|trim|lower -%}
{% if cmd1.split(' ')[0] == "read" %}{% else %}
{{ cell.source }}{% endif %}
{% endblock input %}

## Add markdown cells
{%- block markdowncell -%}
* {{ cell.source }}
{% endblock markdowncell %}
