function merge_sort(left_part,right_part) 
{
	var i = 0, j = 0;
	var results = [];

	while (i < left_part.length || j < right_part.length) {
		if (i === left_part.length) {
			results.push(right_part[j]);
			j++;
		} 
      else if (j === right_part.length || left_part[i] <= right_part[j]) {
			results.push(left_part[i]);
			i++;
		} else {
			results.push(right_part[j]);
			j++;
		}
	}
	return results;
}