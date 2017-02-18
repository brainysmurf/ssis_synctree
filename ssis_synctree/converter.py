import re, os

comma="&#44"  # moodle knows this is a comma
exclude = ['PEHEAH', 'MAHIGH', 'IBCAS']
grade11n12 = re.compile(r'(11|12)$')
eleven_twelve = re.compile(r'(11|12)')

depart_dict = {
	'hro': 'departHROOM',
	'maa': 'departMATH',
	'mas': 'departMATH',
	'mat': 'departMATH',
	'mah': 'departMATH',
	'kor': 'departWL',
	'chi':'departCHI',
	'cnb':'departCHI',
	'ger': 'departWL',
	'lbc': 'departWL',
	'lbs': 'departWL',
	'jap': 'departWL',
	'spi':'departWL',
	'dan':'departWL',
	'spa': 'departWL',
	'spb':'departWL',
	'fre':'departWL',
	'lib':'departLIB',
	'arm': 'departARTS',
	'art': 'departARTS',
	'arv': 'departARTS',
	'arc': 'departARTS',
	'dra': 'departARTS',
	'arg': 'departARTS',
	'hum': 'departHUM',
	'eco':'departHUM',
	'psy':'departHUM',
	'sse': 'departHUM',
	'env':'departHUM',
	'ssh': 'departHUM',
	'ssg': 'departHUM',
	'ssb': 'departHUM',
	'ssa': 'departHUM',
	'gbs': 'departHUM',
	'com':'departDESIGN',
	'gra':'departDESIGN',
	'tec': 'departDESIGN',
	'hon':'departDESIGN',
	'las': 'departENGLISH',
	'lbe': 'departENGLISH',
	'eng': 'departENGLISH',
	'enb': 'departENGLISH',
	'sci': 'departSCIENCE',
	'bio':'departSCIENCE',
	'scb': 'departSCIENCE',
	'ssp': 'departSCIENCE',
	'ssc': 'departSCIENCE',
	'scc': 'departSCIENCE',
	'phy': 'departPE',
	'phe': 'departPE',
	'peh': 'departPE',
	'tef': 'departDESIGN',
	'des': 'departDESIGN',
	'tem': 'departDESIGN',
	'ted': 'departDESIGN',
	'gra': 'departDESIGN',
	'tok':'departTOK',
	'ibt':'departTOK',
	'std':'departTOK',
	'xst':'departOTHERS',
	'car':'departCAR',
	'ibc':'departCAS'}

department_email_names = {
	'departHUM':'humanitiesdepartment',
	'departARTS':'artsdepartment',
	'departTOK':'tokdepartment',
	'departHROOM':'homeroomteachersALL',
	'departSCIENCE':'sciencedepartment',
	'departENGLISH':'englishdepartment',
	'departLIB':'librarydepartment',
	'departPE':'pedepartment',
	'departWL':'worldlanguagesdepartment',
	'departTOK':'tokdepartment',
	'departDESIGN':'designdepartment',
	'departCHI':'chinesedepartment',
	'departMATH':'mathsdepartment',
 	}

department_heads = {
	# Make lists in case there are multiple needs
	'departMATH': ['garypost'],
	'departWL':   ['reneerehfeldt'],
	'departARTS': ['heidimesser'],
	'departHUM': ['jarrettbrown', 'donpreston'],
	'departENGLISH': ['jenniferlively', 'leeannesmith'],
	'departPE': ['markparratt'],
	'departSCIENCE': ['bryandennie'],
	'departDESIGN': ['jasonreagin'],
	'departCHI': ['rebeccaruan'],
	'departCAS': ['allisonparratt'],
	'departHROOM': ['peterfowles']
	}

def get_head_of_grade(grade):
	return {
	6: ['susancover'],
	7: ['peterguyan'],
	8: ['lucyborden'],
	9: ['ronfrisinger'],
	10: ['benwylie'],
	11: ['byronfarrow'],
	12: ['suemckellor']
	}.get(grade)

def derive_depart(course):
	course = course[:3]
	depart = depart_dict.get(course.lower())
	if depart:
		return depart
	else:
		pass
	#print("unknown department")
	#print("\t{}".format(course))
	return None

def derive_departments(courses):
	results = []
	for course in courses:
		depart = derive_depart(course)
		if depart:
			results.append(depart)
	d = {}
	for x in results:
		d[x] = 1
	return list(d.keys())

def straight_converts(short, long_):
	new_short = {
		'MATHSD11': 'MATHSD',
		'MATHSD12': 'MATHSD',
		'JAPA_07': 'JAPA8',
		'FREB_06': 'FRELA67_PH2',
		'FREB_07': 'FRELA67_PH2',
		'FREB_09': 'FRELA910',
		'HSDMAT10': 'MATST10',
		'PHYHON11': 'SSPHYSH1112',
		'PHYHON12': 'SSPHYSH1112',
		'HSDPSY12': 'SSPSYSH1112',
		'HSDPSY11': 'SSPSYSH1112',
		'HONSPSCI11': 'SEHS11',
		'SPSCIS11': 'SEHS11',
		'JAP_A_07': 'JAP78',
		'JAP_A_08': 'JAP78',
		'LIBRA_10': 'STDSKL10',
		'LIBRA_09': 'STDSKL9',
		'SPANISH5': 'SPA5',
		'SPA_B_06': 'SPALA',
		'SPA_B_07': 'SPALA',
		'SPA_B_08': 'SPALA',
		'SPA_B_09': 'SPALA',
		'SPA_B_10': 'SPALA',
		'MAHIGH11': 'MAHIGH11',
		'ENBSWA9': 'ENGBA9',
		'ENGLIL12': 'ENGLISH1112',
		'ENGLLL11': 'ENGLLSH1112',
		'ENLIHON12': 'ENLIHON12',
		'ENGHON12': 'LBENGSH1112',
		'ENGHON11': 'LBENGSH1112',
		'LBENGS11': 'LBENGSH1112',
		'LBENGH12': 'LBENGSH1112',
		'ENGBSL06': 'ENGLAB',
		'ENGBSL07': 'ENGLAB',
		'ENGBSL08': 'ENGLAB',
		'ENGBSL09': 'ENGLAB',
		'ENGBSL10': 'ENGLAB',
		'HSDENG11': 'ENGLLSH1112',
		'PSYHON11': 'SSPSYSH1112',
		'HSDMUS11': 'ARMUSSH1112',
		'HSDCHE12': 'SCCHESH1112',
		'MADHON12': 'MATHSD',
		'HSDLIT12': 'ENGLISH1112',
		'HSDBUS12': 'SSBAMSH1112',
		'HSDBIO12': 'SCBIOSH1112',
		'MADHON12': 'MADHON12',
		'HSDMAT10': 'HSDMAT10',
		'HSDSCI10': 'HSDMAT10',
		'MASTUS12': 'MATHSD',
		'MADHON12': 'MATHSD',
		'HSDMAA11': 'LBCHIASH1112',
		'HSDMAA12': 'LBCHIASH1112',
	}.get(short)
	if new_short:
		return new_short, long_
	else:
		return None

def map_codes(short, grade, higher_lower):
	"""
	Meeting department needs requires an elaborate mapping system applied to some courses
	This routine meets those needs
	"""
	grade = str(grade)
	higher_lower = str(higher_lower).upper()
	result = {
		# MATHS DEPT needs certain things at the IB level
		# From head of department:
		#Hon Math SL/HL (11/12) can be removed. It is used to distinguish those students taking the IB exam. The course is exactly the same as Maths SL
		#Mathematics Applications (11) should be rewritten as HSD Mathematics Applications (11)
		#In Place of the 2 same named courses (IB Mathematics SL/HL (11/12)) We need; IB Mathematics SL (11), IB Mathematics SL (11), IB Mathematics HL (11) and IB Mathematics HL (12). Making this distinction is very important. The G11 and G 12 cohorts are large, the courses and IA's are different, and we submit course specific information to the IB on line
		#In place of IB Maths Studies SL/HL (11/12) there should be IB Maths Studies SL (11) and IB Maths Studies SL (12). For the same reason as above. There is no HL course for Studies Hon Math Studies (11/12) can be removed. It is used to distinguish those students taking the IB exam. The course is exactly the same as Maths Studies.

		# Convert hon maths studies to maths studies, respecting H/L, grade divisions
		'LIBRA00': 'LIBRASH1112',   # LIBRA00 is HSD Library for some reason
		'MADHONSH1112': 'MASTUS'+grade,
		'MASHONSH1112': 'MASTAS'+grade,
		# Divide IB maths by H/L, grade
		'MASTASH1112':  'MASTA'+higher_lower+grade,
		# Divide maths studies by H/L, grade
		'MASTUSH1112':  'MASTU'+higher_lower+grade,

		'MAHIGH1112': 'MAHIGH'+grade,

		# SWA Study Skills are really just learning support stuff
		'STUDYSWA10': 'STDSKL10',
		'STUDYSWA9': 'STDSKL9',
		'STUDYSWA9': 'STDSKL08',
        'STUDYSWA9': 'STDSKL07',
		'STUDYSWA9': 'STDSKL9',
        
		'ENBSWA9': 'ENGBS9',
		'ENBSWA8': 'ENGBS8',
		'ENBSWA7': 'ENGBS7',
		'ENBSWA6': 'ENGBS6',
		'ENBSWA10': 'ENGBA10',

		'ENGIB6': 'ENGI6',
		'ENGIA6': 'ENGI6',

		'ENGIB7': 'ENGI7',
		'ENGIA7': 'ENGI7',

		
		# Straight conversions
		'ENLHONSH1112': 'ENGLLSH1112',  # English A Lang & Lit
		'ENGHONSH1112': 'LBENGSH1112',  # English B
		'CNLHONSH1112': 'CHILLSH1112',  # Chinese
		'CNBHONSH1112': 'LBCHISH1112',  # Mandarin
		'KRLHONSH1112': 'KORLISH1112',  # Korean
		'KORLISH11': 'KORLISH1112', # Korean Hons
		'CNIHONSH1112': 'LBCHISH1112',  # Chinese ab initio
		'ARVHONSH1112': 'ARVISSH1112',  # Visual Arts
		'JPLHONSH1112': 'JAPLISH1112',   # Japanese
		'SPBHONSH1112': 'LBSPASH1112',  # Spanish
		'SPIHONSH1112': 'LBSPAASH1112', # spanish ab initio

		'ECOHONSH1112': 'SSECOSH1112', # Economics
		'BAMHONSH1112': 'SSBAMSH1112', # Business & Management

		'COMHONSH1112': 'TECOMSH1112', # Computer Science
		'ENVHONSH1112': 'SSENVSH1112', # Environmental Systems, one course
		
		'HONTEDSH1112': 'TEDESSH1112', # Design Technology
		'CNBHONSH1112': 'LBCHISH1112', # Chinese
		
		'BIOHONSH1112': 'SCBIOSH1112',   # Biology honors

		'PSYHON1112': 'SSPSYS12' if grade == '12' else 'SSPSYSH1112',
		'SSPSYSH1112': 'SSPSYS12' if higher_lower == 'S' and grade == '12' else 'SSPSYSH1112',
		'PEHEAHS1': 'PEHEASH1112',

						 #'DESIG9': 'GRAPHICDESIGN9',
						 #'DESIG10': 'GRAPHICDESIGN10'   TECOM10, TECOM9 deleted, TECOMSH1112 becomes TECOM1112CLARK, TEFOO9 TEFOO10 have been killed, TEMAT10 & 9 have been killed, TEFOOHS1 has been killed (and probably never ran)

		'HUMAN6': 'ENGA6',
		'HUMAN7': 'ENGA7'
		
		# 

	}.get(short)

	if not result:
		return short
	return result

def map_codes_names(short):

	return {
		'MASTAS11': "IB Mathematics SL (11)",
		'MASTAS12': "IB Mathematics SL (12)",
		
		'MASTUS11': "IB Math Studies SL (11)",
 		'MASTUH11': "IB Math Studies HL (11)", # doesn't exist though
		'MASTUS12': "IB Math Studies SL (12)",
		'MASTUH12': "IB Math Studies HL (12)",  # doesn't exist though

		'MAHIGH11': "IB Mathematics HL (11)",
		'MAHIGH12': "IB Mathematics HL (12)"

		}.get(short)

def convert_short_long(short, long):
	# First do any defined straight conversions
	short_circuit = straight_converts(short, long)
	if short_circuit is not None:
		return short_circuit

	# Second do blanket conversions
	short = re.sub(r'[^a-zA-Z0-9]', '', short)    # take out nonalpha
	short = re.sub(r'0([1-9]+)$', '\\1', short)   # take out leading zeroes
	grade = re.sub(r'[^0-9]+', '', short)         # get the grade
	short = short.replace('_', '')

        # Decision: We want our IB Diploma and HS Diploma courses to be collapsed
        # into the same shared course page.
        # The following logic ensures that by adjusting the short and long name.
        # This works because in powerschool the only difference in name and ID is
        # their ending.
	standard_higher = None   # we need to know which standard and higher later
	if grade11n12.search(short):
		stem, suffix, _ = re.split('(S?11|H?11|S?12|H?12)$', short)
		standard_higher = re.sub(r'[0-9]', '', suffix)
		grade = int(re.sub(r'[A-Z]', '', suffix))
		if not standard_higher:
			standard_higher = "S"
		long  = eleven_twelve.sub('11/12', long)
		long  = long.replace(",", comma).replace('  ', ' ')
		short = stem + 'SH1112'

	short = map_codes(short, grade, standard_higher)
	change = map_codes_names(short)
	if change:
		long = change
	return short, long

def no_whitespace_all_lower(base):
	return re.sub(r'[^a-z]', '', base.replace(' ', '').lower())


class Categories:
	def __init__(self, shortname):
		self.declare()
		shortname = shortname.lower()[:3]
		self._s = self.__dict__[shortname] if shortname in self.__dict__.keys() else ""

	def __str__(self):
		return self._s

	def declare(self):
		wl = "World Languages"
		ch = "Chinese"
		at = "Arts"
		hm = "Humanities"
		en = "English"
		sc = "Science"
		lb = "Others"
		ma = "Math"
		pe = "Physical Education"
		ds = "Design"
		ss = "Others"
		tk = "Others"
		self.maa = self.academics(ma)
		self.mas = self.academics(ma)
		self.mat = self.academics(ma)
		self.mah = self.academics(ma)
		self.hmr = self.homeroom()
		self.chi = self.academics(ch)
		self.kor = self.academics(wl)
		self.ger = self.academics(wl)
		self.lbc = self.academics(wl)
		self.lbs = self.academics(wl)
		self.jap = self.academics(wl)
		self.spa = self.academics(wl)
		self.fre = self.academics(wl)
		self.dan = self.academics(wl)
		self.ibc = self.academics("Others")
		self.arm = self.academics(at)
		self.art = self.academics(at)
		self.arv = self.academics(at)
		self.arc = self.academics(at)
		self.dra = self.academics(at)
		self.arg = self.academics(at)
		self.hum = self.academics(hm)
		self.sse = self.academics(hm)
		self.ssh = self.academics(hm)
		self.ssg = self.academics(hm)
		self.ssb = self.academics(hm)
		self.ssa = self.academics(hm)
		self.gbs = self.academics(hm)
		self.las = self.academics(en)
		self.lbe = self.academics(en)
		self.eng = self.academics(en)
		self.enb = self.academics(en)
		self.sci = self.academics(sc)
		self.scb = self.academics(sc)
		self.ssp = self.academics(sc)
		self.ssp = self.academics(sc)
		self.ssc = self.academics(sc)
		self.scc = self.academics(sc)
		self.env = self.academics(sc)
		self.lib = self.academics(lb)
		self.phy = self.academics(pe)
		self.phe = self.academics(pe)
		self.peh = self.academics(pe)
		self.com = self.academics(ds)
		self.tef = self.academics(ds)
		self.des = self.academics(ds)
		self.tem = self.academics(ds)
		self.ted = self.academics(ds)
		self.gra = self.academics(ds)
		self.tec = self.academics(ds)
		self.std = self.academics(ss)
		self.ibt = self.academics(tk)
		self.car = self.academics("Others")
		self.xst = self.academics(ss)
		self.hro = self.academics("Others")
		self.lib = self.academics("Others")

	def homeroom(self):
		return "Homeroom"

	def academics(self, code):
		return "Teaching & Learning / {0}".format(code)

def put_in_order(what):
    trans = {'L':1,'E':2,'A':3,'R':4,'N':5,'S':6,'SWA':7}
    if '6' in what:
        result = 100 + trans[re.sub('[0-9]', '', what)]
    elif '7' in what:
        result =  200 + trans[re.sub('[0-9]', '', what)]
    elif '8' in what:
        result =  300 + trans[re.sub('[0-9]', '', what)]
    elif '9' in what:
        result =  400 + trans[re.sub('[0-9]', '', what)]
    elif '10' in what:
        result = 500 + trans[re.sub('[0-9]', '', what)]
    elif '11' in what:
        result = 600 + trans[re.sub('[0-9]', '', what)]
    elif '12' in what:
        result = 700 + trans[re.sub('[0-9]', '', what)]
    return result


if __name__ == "__main__":

	courses = [
	('SSBAML11', 'BAM?'),
	('SSECOH12', 'something or other'),
	('LIBRA00', 'LIbrary!'),
	('PEHEAH12', 'Some PE class I dunno'),
	('MASHON11', 'Maths Honors something'),
	('SSBIOHS1', 'I dunno'),
	('MASTAS12', "Mathematics Amazing (12)"),
	('ENGA__11', 'English for Adults (11)'),
	('PYISCI_08', 'Physical Science 8'),
	]

	for short, long in courses:
		print('start {} {}'.format(short, long))
		short, long = convert_short_long(short, long)
		print('end {} {}'.format(short, long))		