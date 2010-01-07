{% extends "base.tpl" %}

{% block content %}
What do you wanna do:<p>
{% for url in entries %}
<a href="{{ url }}/">{{ url }}</a><br>
{% endfor %}
{% endblock %}
