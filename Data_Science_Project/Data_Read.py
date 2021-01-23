import pandas as pd 
data_frame1=pd.read_csv(r'E:\Data_Science_Project\data.csv')
#print(data_frame.shape)
#print(data_frame.describe())
#print(data_frame.values)
#print('\n')
age_data=data_frame1[data_frame1['Age']>40].head()
#print(age_data)
df1=pd.DataFrame(data_frame1,columns=['Name','Age','Wage','Value'])
def fn_convert_str_float(string):
	if type(string)==int or type(string)==float :
		return string
	elif string is None:
		return 0
	elif type(string)==str and len(string)>1:
		if string[-1::].upper()=='K':
			return 1000*float(string[:-1:])
		elif string[-1::].upper()=='M':
			return 1000000*float(string[:-1:])
		elif string[-1::].upper()=='B':
			return 1000000000*float(string[:-1:])
		else:
			return float(string[:-1:])
var_wage=df1['Wage'].replace(r'[\€,]','',regex=True).apply(fn_convert_str_float)
var_value=df1['Value'].replace(r'[\€,]','',regex=True).apply(fn_convert_str_float)
var_diff=var_wage-var_value
#v_str='#556m'
#print( fn_convert_str_float(v_str.replace('#','')))
print(var_diff)