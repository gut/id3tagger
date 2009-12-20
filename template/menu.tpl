What do you wanna do:<p>
{% for url in entries %}
<a href="{{ url }}/">{{ url }}</a><br>
{% endfor %}
