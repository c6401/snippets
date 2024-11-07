on open location schemeUrl
	set runnable to do shell script "/usr/bin/env python3 -c \"import urllib.parse as p; print(p.parse_qs(p.urlparse(''' " & schemeUrl & " ''').query)['run'][0])\" 2>&1 || true"
	set result to do shell script runnable
	--display alert result
end open location
