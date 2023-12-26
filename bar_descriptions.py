import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Define a custom style
my_style = LS('#333366', base_style=LCS)

# Create a Bar chart
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

# Define data
plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
]

# Add data to the chart
chart.add('', plot_dicts)

# Render the chart to a file
chart.render_to_file('bar_descriptions.svg')
