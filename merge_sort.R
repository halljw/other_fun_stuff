#!/usr/bin/env Rscript

merge_sort <- function(lst){

	if(length(lst) == 1){
		return(lst)
	}
	
	l1 = lst[1:round(length(lst)/2)]
	l2 = lst[(round(length(lst)/2)+1):length(lst)]

	l1 = merge_sort(l1)
	l2 = merge_sort(l2)

	return(merge(l1,l2))
}

merge <- function(l1, l2){

	merged <- vector('integer')
	while (length(l1)>0 & length(l2) > 0) {
		if(l1[1] > l2[1]) {
			merged <- c(merged, l2[1])
			l2 <- l2[-1]
		}
		else {
			merged <- c(merged, l1[1])
			l1 <- l1[-1]
		}
	}
	while (length(l1)>0) {
		merged <- c(merged, l1[1])
		l1 <- l1[-1]
	}
	while (length(l2)>0) {
		merged <- c(merged, l2[1])
		l2 <- l2[-1]
	}
	return(merged)
}

a <- c(5,4,3,2, 4, 8, 9, 11, 1)

b <- merge_sort(a)

print(a)
print(b)
