v_list=[]
idx_pointer=0
#stack_len=0
def stack_size(v_num):
	stack_len=0
	for i in range(v_num):
		#v_list.append(None)
		stack_len+=1
	#print(v_list)
	return stack_len

def push_stack_element(value,v_len):
	v_list.append(value)
	idx_pointer=v_list.index(value)
	if len(v_list)>v_len:
		print('Stack is Full',len(v_list))
		return

def pop_stack_element():
	v_list.pop(idx_pointer)


v_len=stack_size(5)
print(v_len)
push_stack_element(5,v_len)
push_stack_element(4,v_len)
push_stack_element(3,v_len)
push_stack_element(2,v_len)
push_stack_element(1,v_len)
#push_stack_element(0,v_len)
print(v_list,idx_pointer)
pop_stack_element()
print(v_list,idx_pointer)
