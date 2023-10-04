// A iterative binary search function. It returns location
// of x in given array arr[l..r] if present, otherwise -1

int binarySearch(int arr[], int low, int high, int x)
{
	while (low <= high) {

		// Find index of middle element
		int mid = (low + high) / 2;

		// Check if x is present at mid
		if (arr[mid] == x)
			return mid;

		// If x greater, ignore left half
		if (arr[mid] <= x)
			low = mid + 1;

		// If x is smaller, ignore right half
		else
			high = mid - 1;
	}

	// If we reach here, then element was not present
	return -1;
}
