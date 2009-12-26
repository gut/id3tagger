<table>
<tr>
	<th colspan='3'>{{ basename }}</th>
</tr>
{% for f in files %}
<tr>
	{% ifequal f.type 'generate_new_table' %}
		<td colspan='3'>{{ f.folder }}</td>
	{% else %}
		{% ifequal f.type 'changed' %}
			<td>{{ f.list.0 }}</td>
			<td>-&gt;</td>
			<td class="changed">{{ f.list.1 }}</td>
		{% else %}
			<td colspan='3'>{{ f }}</td>
		{% endifequal %}
	{% endifequal %}
</tr>
{% endfor %}
</table>
