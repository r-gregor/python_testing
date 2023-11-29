html_doc = """
<html>
<head>
<title>[ start@20161206 ]</title>
<meta http-equiv="Content-Type" content="text/html" charset=utf-8">
<link media="screen" rel="stylesheet" type="text/css" href="index-black.css">
<link media="print" rel="stylesheet" type="text/css" href="index-nova-print.css">
<base target="_blank">

</head>
<body>
<center>
    <div class="header">
        <h1 class="naslov1"> start@20161206 </h1>
    </div>

<p>
	<span style="font-style: oblique; font-size: 10px;">Last change: 06.12.2016 by RgregoR</span>
</p>
</center>

</body>
</html>
"""

from bs4 import *
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
          
            
            

