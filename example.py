from bokeh.charts import Bar, show, output_file, vplot

output_file("example.html")

category_list= [{'Pass Rate': [74.78632478632478, 69.12751677852349], 'Categories': ['M', 'F']}, {'Pass Rate': [72.54901960784314, 61.29032258064516, 77.14285714285714, 73.07692307692308, 68.75, 58.333333333333336, 60.0, 70.45454545454545, 90.9090909090909, 80.0, 88.88888888888889, 60.714285714285715, 77.77777777777777], 'Categories': ['East Anglian Region', 'Scotland', 'North Western Region', 'South East Region', 'West Midlands Region', 'Wales', 'North Region', 'South Region', 'Ireland', 'South West Region', 'East Midlands Region', 'Yorkshire Region', 'London Region']}, {'Pass Rate': [73.46938775510205, 71.1340206185567, 73.49397590361446, 87.5], 'Categories': ['HE Qualification', 'A Level or Equivalent', 'Lower Than A Level', 'Post Graduate Qualification']}, {'Pass Rate': [84.61538461538461, 73.03370786516854, 70.39106145251397], 'Categories': ['55<=', '35-55', '0-35']}]
categories = ['gender','region','highest_education','age_band']

p1 = Bar(category_list[0], values = 'Pass Rate', label = 'Categories', title = categories[0], width=1000)
p2 = Bar(category_list[1], values = 'Pass Rate', label = 'Categories', title = categories[1], width=1000)
p3 = Bar(category_list[2], values = 'Pass Rate', label = 'Categories', title = categories[2], width=1000)
p4 = Bar(category_list[3], values = 'Pass Rate', label = 'Categories', title = categories[3], width=1000)

p = vplot(p1,p2,p3,p4)

show(p)