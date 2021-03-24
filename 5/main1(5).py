def areAnagram(str1, str2):
	num1 = len(str1)
	num2 = len(str2)
	if num1 != num2:
		return 0

	str1 = sorted(str1)
	str2 = sorted(str2)
	for i in range(0, num1):
		if str1[i] != str2[i]:
			return 0

	return 1
str1 = input("enter the string 1")
str2 = input("enter the string 2")


if areAnagram(str1, str2):
	print("True")
else:
	print("False")


