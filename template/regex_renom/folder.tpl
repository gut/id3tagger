<table>
<tr>
	<th colspan='3'>{{ basename }}</th>
</tr>
{% for f in files %}
<tr>
	{% ifequal f.1 'generate_new_table' %}
	<td colspan='3'>{{ f.0 }}</td>
	{% else %}
	<td>{{ f.0 }}</td>
	<td>=&gt;</td>
	<td>{{ f.1 }}</td>
	{% endifequal %}
<tr>
{% endfor %}
</table>
