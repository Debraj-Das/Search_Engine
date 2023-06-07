from bs4 import BeautifulSoup

# Example HTML input
html = '''
<html>
<head>
</head>
<body>
    <div fdprocessedid="123">
        <p>This is a paragraph.</p>
    </div>
</body>
</html>
'''

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the element with the "fdprocessedid" attribute
element = soup.find(attrs={"fdprocessedid": "123"})

# Print the element
print(element)
