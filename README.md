# Guess_What
猜数字。

首先设定答案的位数n（1≤n≤10，位数越多，游戏难度越高，建议3或4）。正确答案数字n位各不相同。最高位有可能是0，即四位数答案有可能是“0123”。

每键入一次猜测的答案，系统将返回猜测答案与正确答案的相关性：Golden代表猜测答案中存在于正确答案且位置相同的位的个数，Blue代表猜测答案中存在于正确答案但位置不同的位的个数。

例如：  
正确答案为168，此时：
- 键入012，系统返回“Golden:0,Blue:1”，因为“1”存在于“168”中但不在第一位；
- 键入345，系统返回“Golden:0,Blue:0”，因为“3”“4”“5”都不存在于“168”中；
- 键入678，系统返回“Golden:1,Blue:1”，因为“6”存在于“168”中但不在第一位，“8”存在于“168”中且同样是第三位；*（此时可以推测出：3、4、5、9都不存在于正确答案中，）*
- 键入304，系统返回“Golden:0,Blue:0”；*（可推：0也不存在于正确答案中）*
- 键入134，系统返回“Golden:1,Blue:0”；*（可推：“1”在正确答案第1位，且“678”中的“6”不是Golden项，“7”与“8”有一个是Golden项）*
- 键入178，系统返回“Golden:2,Blue:0”；*（可推：“678”中的“6”是Blue项，“678”中的“7”与“8”中有一个是废项）*
*（若“678”中的“7”是废项，则“8”为Golden项，第二位为“6”，答案为“168”；若“678”中的“8”是废项，则“7”为Golden项，第三位为“6”，答案为“176”）*
- 键入168，系统返回“Bingo！”，代表回答正确，游戏结束。
