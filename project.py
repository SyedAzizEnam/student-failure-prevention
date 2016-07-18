import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA


Vle = pd.read_csv('studentVle.csv')

info = pd.read_csv('studentinfo.csv')

course = Vle[(Vle['code_module'] == 'AAA') & (Vle['code_presentation']=='2013J')]

info = info[(info['code_module']=='AAA') & (info['code_presentation']=='2013J')]

course = course.groupby(['code_module','code_presentation','id_student','id_site'], as_index = False).sum()

students, sites = course['id_student'].unique(), course['id_site'].unique()
 
genders, regions, education, age = info['gender'].unique(), info['region'].unique(), info['highest_education'].unique(), info['age_band'].unique()

category_statistics = list()

categories = ['gender','region','highest_education','age_band']

for category in categories:
	
	data = {}
	stats = list()
	entries = info[category].unique().tolist()

	data['Categories'] = entries

	for entry in entries:

		total = info[info[category] == entry]
		passrate = 100*float(total[(total['final_result'] =='Pass') | (total['final_result'] =='Distinction')]['final_result'].size) / total['final_result'].size

		stats.append(passrate)

	data['Pass Rate'] = stats

	category_statistics.append(data)


category_list= [{'Pass Rate': [74.78632478632478, 69.12751677852349], 'Categories': ['M', 'F']}, {'Pass Rate': [72.54901960784314, 61.29032258064516, 77.14285714285714, 73.07692307692308, 68.75, 58.333333333333336, 60.0, 70.45454545454545, 90.9090909090909, 80.0, 88.88888888888889, 60.714285714285715, 77.77777777777777], 'Categories': ['East Anglian Region', 'Scotland', 'North Western Region', 'South East Region', 'West Midlands Region', 'Wales', 'North Region', 'South Region', 'Ireland', 'South West Region', 'East Midlands Region', 'Yorkshire Region', 'London Region']}, {'Pass Rate': [73.46938775510205, 71.1340206185567, 73.49397590361446, 87.5], 'Categories': ['HE Qualification', 'A Level or Equivalent', 'Lower Than A Level', 'Post Graduate Qualification']}, {'Pass Rate': [84.61538461538461, 73.03370786516854, 70.39106145251397], 'Categories': ['55<=', '35-55', '0-35']}]
categories = ['gender','region','highest_education','age_band']

passedornot = list()

features = np.zeros((students.size, sites.size))

sites_to_index = {}

for i in range(len(sites)):
	sites_to_index[sites[i]] = i

for i in range(len(students)):

	student_info = info.loc[info['id_student']==students[i]]

	result = student_info['final_result'].tolist()[0]

	passedornot.append('green' if ((result=='Pass') | (result =='Distinction')) else 'red')

	df = course[course['id_student']==students[i]]

	for site in df['id_site']:

		features[i,sites_to_index[site]] = df.loc[df['id_site']==site]['sum_click'] 

features = preprocessing.normalize(features, axis=0)

pca = PCA(n_components=2)

pca.fit(features)

projected_features = pca.transform(features)

####PLOTS####

from bokeh.charts import Bar, show, output_file, vplot

output_file("plot1.html")

p1 = Bar(category_statistics[0], values = 'Pass Rate', label = 'Categories', title = categories[0], width=1000)
p2 = Bar(category_statistics[1], values = 'Pass Rate', label = 'Categories', title = categories[1], width=1000)
p3 = Bar(category_statistics[2], values = 'Pass Rate', label = 'Categories', title = categories[2], width=1000)
p4 = Bar(category_statistics[3], values = 'Pass Rate', label = 'Categories', title = categories[3], width=1000)

p = vplot(p1,p2,p3,p4)

show(p)

from bokeh.plotting import figure, show, output_file

p = figure(title = "2-D Projection of student vle interactions")
p.xaxis.axis_label = 'Dimension 1'
p.yaxis.axis_label = 'Dimension 2'

p.circle(features[:,0], features[:,1],
         color=passedornot, fill_alpha=0.2, size=10)

output_file("plot2.html", title="2-D Projection of student vle interactions")

show(p)
