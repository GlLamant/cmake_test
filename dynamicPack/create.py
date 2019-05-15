import os

head = '''
#ifndef __FUN{0}_H__
#define __FUN{0}_H__

__declspec(dllexport) void {1}();

#endif
'''

src = '''
#include \"{0}.h\"
#include <stdio.h>

void {1}(){{
	printf("{2}");
}}
'''

for num in range(1,6):
	Dir = 'fun'+str(num)
	print(Dir)
	try:
		os.mkdir(Dir)
	except:
		pass
	cpp = Dir + '/' + Dir + '.cpp'
	h = Dir + '/' + Dir + '.h'
	fp = open(cpp,'w')
	s = src.format(Dir,Dir,Dir)
	fp.write(s)
	fp.close
	fp = open(h,'w')
	fp.write(head.format(str(num),Dir))
	fp.close
