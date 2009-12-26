<table>
<tr>
	<th colspan='3'>{{ basename }}</th>
</tr>
{% for f in files %}
<tr>
	{% if f.generate_new_table %}
		<td colspan='3'>{{ f.folder }}</td>
	{% else %}
		{% if f.changed %}
			<td>{{ f.list.0 }}</td>
			<td>-&gt;</td>
			{% if disk_changed %}
				<td class="disk_changed">{{ f.list.1 }}</td>
			{% else %}
				<td class="changed">{{ f.list.1 }}</td>
			{% endif %}
		{% else %}
			<td colspan='3'>{{ f }}</td>
		{% endif %}
	{% endif %}
</tr>
{% endfor %}
</table>
