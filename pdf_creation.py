from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

data = [
    {'Name': 'John', 'Age': 25, 'City': 'New York'},
    {'Name': 'Emma', 'Age': 32, 'City': 'San Francisco'},
    {'Name': 'Michael', 'Age': 28, 'City': 'Los Angeles'}
]

doc = SimpleDocTemplate("table_example.pdf", pagesize=letter)
styles = getSampleStyleSheet()

table_data = []
table_data.append(["Name", "Age", "City"])
for entry in data:
    table_data.append([entry['Name'], entry['Age'], entry['City']])

table = Table(table_data, colWidths=100, rowHeights=30)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

content = []
content.append(table)
doc.build(content)
