<table>
<tr>
	<th colspan='15'>{{ basename }}</th>
</tr>
{% for f in files %}
<tr>
	{% if f.generate_new_table %}
		<td colspan='15'>{{ f.folder }}</td>
	{% else %}
		<th>{{ f.filename }}</th>
		{% if f.changed %}
			<td>{{ f.list.0 }}</td>
			<td>-&gt;</td>
			{% if disk_changed %}
				<td class="disk_changed">{{ f.list.1 }}</td>
			{% else %}
				<td class="changed">{{ f.list.1 }}</td>
			{% endif %}
		{% else %}
			<td>{{ f.Genre }}</td>
			<td>{{ f.Artist }}</td>
			<td>{{ f.Year }}</td>
			<td>{{ f.Album }}</td>
			<td>{{ f.DiscNum }}</td>
			<td>{{ f.TrackNum }}</td>
			<td>{{ f.Title }}</td>
		{% endif %}
	{% endif %}
</tr>
{% endfor %}
</table>
