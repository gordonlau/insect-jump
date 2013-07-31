#!/usr/bin/python

class InsectJump:
	'''My Non-list comprehension version of insect jump 
		step_set is the possible step for the insect to jump
		target is the total distance to be travelled.

	'''

	def __init__(self):
		''' Nothing to do for init'''
		pass
	def iterate_count(self,step_set,target,count=0):
		''' Count the possible combination for insect jump problem'''
		if target == 0:
			return count +1
		elif target < 0:
			return 
		for step in step_set:
			if step  > target:
				break
			elif step <= target:
				count = self.iterate_count(step_set,target-step,count )
		return count
	
	def iterate_jump(self,step_set,target,single_result=[],result_list= []):
		''' Dispaly all the possible combination in a list of result'''
		if target == 0:
			result_list.append(single_result)
		elif target < 0:
			return 
		for step in step_set:
			if step  > target:
				break
			elif step <= target:
				self.iterate_jump(step_set, target-step,single_result+[step],result_list)
		return result_list

