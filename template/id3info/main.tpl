{% extends "base.tpl" %}

{% block content %}
<form method="get" target="_self">
<table>
	<tr>
		<td>Directory to work:</td><td><input type="text" name="directory" value="{{ directory }}"></input></td>
	</tr>
	<tr>
		<th colspan="2"><input type="submit" value="Update"></th>
	</tr>
</table>
<p>
{% if error %}<div class="error">{% endif %}
{{ content }}
{% if can_change %}
<p>
<table>
	<tr>
		<th class="submit"><button type="submit" name="change" value="{{ change_value }}">Apply Changes?</button></th>
	</tr>
</table>
{% endif %}
</form>
{% endblock %}
