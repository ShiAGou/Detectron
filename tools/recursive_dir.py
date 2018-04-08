import os
import glob

def search(dir, ftype='jpg'):
	filelist = os.listdir(dir)
	g = list(glob.iglob(dir+'/*.'+ftype))
	for f in filelist:
		dir_tmp = os.path.join(dir, f)
		if os.path.isdir(dir_tmp):
			g_tmp = search(dir_tmp, ftype)
			g = g+g_tmp
	return g

if __name__ == '__main__':
	g = search('/Users/redrock/github/Detectron')
	for gf in g:
		print(gf)