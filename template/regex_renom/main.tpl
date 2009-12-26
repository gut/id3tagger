<html>
<head>
	<title>{{ title }}</title>
	<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<h3>Renaming files with regex:</h3>
<form method="get" target="_self">
<table>
	<tr>
		<td>Directory to work:</td><td><input type="text" name="directory" value="{{ directory }}"></input></td>
	</tr>
	<tr>
		<td>Only this kind of file:</td><td><input type="text" name="extension" value="{{ extension }}"></input></td>
	</tr>
	<tr class="spacer">
	</tr>
	<tr>
		<td>Regex to search:</td><td><input type="text" name="search" value="{{ search }}"></input></td>
	</tr>
	<tr>
		<td>Replacement:</td><td><input type="text" name="replacement" value="{{ replacement }}"></input></td>
	</tr>
	<tr>
		<th colspan="2"><input type="submit" value="Update"></th>
	</tr>
</table>
<p>
{% if error %}<div class="error">{% endif %}
{{ content }}
{% if error %}</div>{% endif %}
{% if can_change %}
<p>
<table>
	<tr>
		<th class="submit"><button type="submit" name="change" value="change_it">Apply Changes?</button></th>
	</tr>
</table>
{% endif %}
</form>
</body>
</html>

