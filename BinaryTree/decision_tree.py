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
		self.matchFunc = None

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

nextNode = root.featureTest({'age':35, 'gender':'male'})
print(nextNode.__dict__)
print('root:{}'.format(root.__dict__))




