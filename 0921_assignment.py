def info_to_list(name: str, major: str, student_id: str) -> list:
	res = list()
	### BLANK start ###
	res.append(name)
	res.append(major)
	res.append(student_id)
	if(int(student_id) %2 == 1):
		res.append("ODD")
	else:
		res.append("EVEN")
	### BLANK end   ###
	return res


if __name__ == '__main__':
	### BLANK start ###
	my_name = "김민경"
	my_major = "산업보안학과"
	my_sid = "20191327"
	### BLANK end   ###
	infos = info_to_list(my_name, my_major, my_sid)
	res_for_print = f"Hi! I'm {infos[0]}, and my major is {infos[1]}! \n" \
	                f"My student ID is {infos[2]}, and this number is {infos[3]}"
	print(res_for_print)