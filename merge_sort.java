
public class merge_sort{


	public static int[] merge_sort(int[] L){

		if(L.length == 1){
			return L;
		}

		int[] l1 = new int[L.length/2];
		for(int i=0; i<l1.length; i++){
			l1[i] = L[i];
		}

		int len;
		if(L.length%2 == 1){
			len = 1+L.length/2;
		}
		else{
			len = L.length/2;
		}
		int[] l2 = new int[len];
		for(int i=0; i<len; i++){
			l2[i] = L[i+L.length/2];
		}

		l1 = merge_sort(l1);
		l2 = merge_sort(l2);

		return merge(l1, l2);
	}

	public static int[] merge(int[] l1, int[] l2){
		int[] merged = new int[l1.length + l2.length];
		int l1_i = 0;
		int l2_i = 0;
		int merged_i = 0;
		while(l1_i < l1.length && l2_i < l2.length){
			if(l1[l1_i] > l2[l2_i]){
				merged[merged_i] = l2[l2_i];
				merged_i++;
				l2_i++;
			}

			else{
				merged[merged_i] = l1[l1_i];
				merged_i++;
				l1_i++;
			}
		}

		while(l1.length > l1_i){
			merged[merged_i] = l1[l1_i];
			merged_i++;
			l1_i++;
		}
		while(l2.length > l2_i){
			merged[merged_i] = l2[l2_i];
			merged_i++;
			l2_i++;
		}
		return merged;
	}


	public static void main(String args[]){
		int[] L = {4, 6, 1, 8, 2, 3, 9};
		L = merge_sort(L);
		String lst = "";
		for(int i = 0; i<L.length; i++){
			if(i==L.length-1){
				lst = lst.concat(L[i]+".");
			}
			else{
				lst = lst.concat(L[i]+", ");
			}
		}
	System.out.println(lst);
	}
}
