#include <stdio.h>

int main() {
	char pass[26];
	pass[0] = 0x02;
	pass[1] = 0xEA;
	pass[2] = 0x02;
	pass[3] = 0xE8;
	pass[4] = 0xFC;
	pass[5] = 0xFD;
	pass[6] = 0xBD;
	pass[7] = 0xFD;
	pass[8] = 0xF2;
	pass[9] = 0xEC;
	pass[10] = 0xE8;
	pass[11] = 0xFD;
	pass[12] = 0xFB;
	pass[13] = 0xEA;
	pass[14] = 0xF7;
	pass[15] = 0xFC;
	pass[16] = 0xEF;
	pass[17] = 0xB9;
	pass[18] = 0xFB;
	pass[19] = 0xF6;
	pass[20] = 0xEA;
	pass[21] = 0xFD;
	pass[22] = 0xF2;
	pass[23] = 0xF8;
	pass[24] = 0xF7;
	pass[25] = 0x00;

	int i;
	for (i = 0; i < 25; i++)
		pass[i] += 119;
	printf("%s\n", pass);

	return 0;
}
