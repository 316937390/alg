# -*- coding: utf-8 -*-

"""
"""
class DecisionTreeNode(object):
	"""决策树节点 DecisionTreeNode"""
	def __init__(self):
		super(DecisionTreeNode, self).__init__()
		self.isRoot = False
		self.childs = []
		self.isLeaf = False
		self.tag = {}
		self.matchFunc = None # 特征测试函数

	def addChild(self, node):
		assert self.isLeaf == False
		assert isinstance(node, DecisionTreeNode)
		self.childs.append(node)

	def featureTest(self, data):
		"""特征测试"""
		for _,child in enumerate(self.childs):
			if self.matchFunc(data, child.tag):
				return child
		return None




def match1(data, tags):
	if data['age'] <= tags['age'][1] and data['age'] > tags['age'][0]:
		return True
	return False

root = DecisionTreeNode()
root.matchFunc = match1
root.isRoot = True

youngNode = DecisionTreeNode()
youngNode.tag = {'age':[10,28]}
adultNode = DecisionTreeNode()
adultNode.tag = {'age':[30,50]}
seniorNode = DecisionTreeNode()
seniorNode.tag = {'age':[60,80]}

root.addChild(youngNode)
root.addChild(adultNode)
root.addChild(seniorNode)

nextNode = root.featureTest({'age':35, 'gender':'male', 'income': 5, 'class':'high'})
print(nextNode.__dict__)
print('root:{}'.format(root.__dict__))



"""
从根节点出发，对节点计算所有特征的信息增益，选择信息增益比最大的特征作为节点特征，根据该特征的不同取值建立子节点；
对每个子节点都递归调用以上算法生成新的子节点，直到信息增益都很小或没有特征可以选择为止。
"""

def constitueTree(dataSource):
	"""
	构建决策树，使用熵模型
	"""
	# dataSource = [{},{}, ...]
	Y = {}
	for i in dataSource:
		if Y.get(i['class']) == None:
			Y[i['class']] = 1
		else:
			Y[i['class']] += 1
	F = { f:False for f in dataSource[0].keys()}
	B = sum(Y.values())
	H_Y = sum([-math.log2(v*1.0/B)*(v*1.0/B) for k,v in Y.items()])
	root = DecisionTreeNode()
	root.isRoot = True
	X_Y_C = {}
	for f,v in F.items():
		for i in dataSource:
			if X_Y_C.get('{}_{}_{}'.format(f,i[f],i['class'])) == None:
				X_Y_C['{}_{}_{}'.format(f,i[f],i['class'])] = 1
			else:
				X_Y_C['{}_{}_{}'.format(f,i[f],i['class'])] += 1
	H_Y_X = 0
	for f,v in F.items():
		X_C = {}
		for k,n in X_Y_C.items():
			if k.split('_')[0] == f:
				x = f + '_' + k.split('_')[1]
				cal_x_p(x, X_Y_C)

			else:
				continue

