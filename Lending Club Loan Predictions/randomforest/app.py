from flask import Flask,render_template,request
import pickle


app=Flask(__name__)


file=open('randomprediction.pkl','rb')
rf=pickle.load(file)
file.close()



@app.route('/' , methods=['GET','POST'])
def hello():
	if request.method == 'POST':
		myDict = request.form
		credit=float(myDict['credit.policy'])
		intrate=float(myDict['int.rate'])
		installment=float(myDict['installment'])
		log_annual=float(myDict['log.annual.inc'])
		dti=float(myDict['dti'])
		fico=float(myDict['fico'])
		dayscrline=myDict['days.with.cr.line']
		revolbal=float(myDict['revol.bal'])
		revolutil=float(myDict['revol.util'])
		inqlast=float(myDict['inq.last.6mths'])
		delinq=float(myDict['delinq.2yrs'])
		publicrec=float(myDict['pub.rec'])
		purposecredit=float(myDict['purpose_credit_card'])
		purposedebtconsolidation=float(myDict['purpose_debt_consolidation'])
		purposeeducational=float(myDict['purpose_educational'])
		purposehomeimprovement=float(myDict['purpose_home_improvement'])
		purposemajorpurchase=float(myDict['purpose_major_purchase'])
		purposesmallbusiness=float(myDict['purpose_small_business'])
	
		input_features=[credit,intrate,installment,log_annual,dti,fico,dayscrline,revolbal,revolutil,inqlast,delinq,publicrec,purposecredit,purposedebtconsolidation,purposeeducational,purposehomeimprovement,purposemajorpurchase,purposesmallbusiness]
		infprob=rf.predict([input_features])[0]
		print(infprob)
		return render_template('show.html',inf=infprob)

	return render_template('index.html')

	#return 'hello' + str(infprob)




if __name__ == '__main__':
	app.run(debug=True)
