import csv
name = 'data.csv'
l = []
X = 0
Y = 0
with open(name) as file:
	reader = csv.DictReader(file)
	for row in reader:
		l.append(row)

def tarification(list,sum_sms,sum_calls):
	i = 0
	output_calls = 0
	input_calls = 0
	sms = 0
	k_input = 1
	k_output = 1
	while i < len(l):
		if(l[i]['msisdn_origin'] == '915642913'):
			output_calls += float(l[i]['call_duration'])
			sum_calls += output_calls*k_output
			sms += float(l[i]['sms_number'])
			if((sms - 10) > 0):
				sms = sms - 10
				sum_sms += 2*sms
				sms = 10
			else: break
			if((sms-5) > 0 and sms <= 10):
				sms = sms - 5
				sum_sms += 1*sms
			else: break
		elif(l[i]['msisdn_dest'] == '915642913'):
			input_calls += float(l[i]['call_duration'])
			sum_calls += input_calls*k_input	
		i +=1
	return sum_sms,sum_calls
Y, X = tarification(l,Y,X)
print('Y = %f, X = %f' % (Y,X))
