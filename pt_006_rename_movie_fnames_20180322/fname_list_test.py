L0 = [ 'Movie.1.720p_[YTS.AG]',
		'Movie.2.720p.2017',
		'Movie.3.720p.2005_[YTS.AG]',
		'Movie.4.720p_[YTS-AG]',
		'Movie.5.720p-[YTS.AM]',
		'Movie.6.720p_[YTS-AM]',
		'Movie.7.720p.2016',
		'Movie.8.1080p-[YTS.AG]',
		'Movie.9.1080p.2013-[YTS.AM]'
]

def fname_dict(flist):
	new_dict = {}
	for el in flist:
		nel = el + "_NEW"
		new_dict[el] = nel
	return new_dict
	
NNN = fname_dict(L0)

for k in NNN:
	print(k, "-->", NNN[k])

