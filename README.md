# 高频二元词组统计

phrase\_count\_stats.py 中 get\_highfreq\_wordtuple 函数实现了统计文本中，出现频率最高的前 10 个「二元词组」，并输出它们的频率。

get\_highfreq\_wordtuple 参数如下：

- file\_path：文件路径
- top\_n：要输出频率最高的 top_n 个词组
- min\_char\_count：至少多少个字才算词

/Data/happiness_seg.txt 中出现频率最高的前 10 个二元词组（1 个字也算词）：

	的 人 921
	他 的 503
	自己 的 479
	上 的 355
	他们 的 334
	人 的 293
	的 时候 261
	就 会 225
	的 东西 207

/Data/happiness_seg.txt 中出现频率最高的前 10 个二元词组（至少两个字才算词）：

	这种 情况 77
	没有 什么 70
	这个 问题 57
	因为 他们 55
	如果 我们 50
	所有 这些 47
	这种 观点 46
	这个 世界 40
	他们 自己 38