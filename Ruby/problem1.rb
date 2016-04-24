def problem1()
	sum=0
	for i in 3..1000
		if i%3==0 || i%5==0 then
			sum+=i
		end
	end
	sum
end
puts problem1()
